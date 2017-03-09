from django.db import models

from django.utils import timezone
from django.template.defaultfilters import slugify

from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string

# Create your models here.
class Category(models.Model):
    slug = models.SlugField(max_length=100, unique=True,
        help_text='my-first-blog if category name is my first blog')
    category_name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', blank=True, null=True,
        related_name='child')

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['category_name']

    def __unicode__(self):
        p_list = self._recurse_for_parents(self)
        p_list.append(self.category_name)
        return self.get(separator().join(p_list))

    def _recurse_for_parents(self, cat_obj):
        p_list = list()
        if cat_obj.parent_id:
            p = cat_obj.get_parent()
            p_list.append(p.category_name)
            more = self._recurse_for_parents(p)
            p_list.extend(more)
        if cat_obj == self and p_list:
            p_list.reverse()
        return p_list

    def get_separator(self):
        return ' :: '

    def _parents_repr(self):
        p_list = self._recurse_for_parents(self)
        return self.get_separator().join(p_list)
    _parents_repr.short_description = "Category parents"

    def save(self):
        self.slug = slugify(self.category_name)
        p_list = self._recurse_for_parents(self)
        if self.category_name in p_list:
            raise "You must not save a category in itself!"
        super(Category, self).save()

    def __repr__(self):
        p_list = self._recurse_for_parents(self)
        p_list.append(self.category_name)
        return self.get_separator().join(p_list)

    @models.permalink
    def get_absolute_url(self):
        return ('category_index', (), {'category': self.slug })

    def __str__(self):
        return self.category_name

class Comment(models.Model):
    post = models.ForeignKey('fips.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['created_date']
        verbose_name_plural = 'Comments'

class User(AbstractUser):
    # default things
    # password
    # last_login
    # username
    # first_name
    # last_name
    # email
    # is_staff
    # is_active
    # date_joined
    # is_superuser
    # groups
    # user_permissions

    user_id = models.AutoField(primary_key=True, verbose_name='User ID', auto_created=True)
    ref_code = models.CharField(get_random_string(length=6), max_length=10)
    referrer = models.TextField(help_text="Referrers' identifiers")

    def __str__(self):
        return self.username

    class Meta():
        verbose_name_plural = 'Users'

class Post(models.Model):
    subject = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']
        verbose_name_plural = 'Posts'
