from django.db import models

from django.utils import timezone
from django.template.defaultfilters import slugify

from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string

# Create your models here.
class Category(models.Model):
    slug = models.SlugField(max_length=100, unique=True,
        help_text='nickname of category name')
    category_name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', blank=True, null=True,
        related_name='child')

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['category_name']

    def __unicode__(self):
        p_list = self._recurse_for_parents(self)
        p_list.append(self.category_name)
        return self.get_separator().join(p_list)

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
        ordering = ['-created_date']
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
    ref_code = models.CharField(default=get_random_string(length=10),
        max_length=10, verbose_name='Reference ID')
    referrer = models.TextField(help_text="identifier1-identifier2-identifier3",
        verbose_name='Referrers')

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
    hits = models.IntegerField(default=0)

    def get_subj_name(self):
        return self.subject.category_name

    def get_prev_post(self):
        return Post.objects.filter(id__lt=self.id).order_by('-id').first()

    def get_next_post(self):
        return Post.objects.filter(id__gt=self.id).order_by('id').first()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def image_comments(self):
        return self.image_comments.filter(approved_comment=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']
        verbose_name_plural = 'Posts'

class UploadFile(models.Model):
    subject = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    upload_file = models.FileField() # default media
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    hits = models.IntegerField(default=0)

    def get_prev_upload(self):
        return UploadFile.objects.filter(id__lt=self.id).order_by('-id').first()

    def get_next_upload(self):
        return UploadFile.objects.filter(id__gt=self.id).order_by('id').first()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']
        verbose_name_plural = 'Upload Files'

class ImageComment(models.Model):
    post = models.ForeignKey('fips.Post', related_name='image_comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    approved_comment = models.BooleanField(default=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-created_date']
        verbose_name_plural = 'Image Comments'
