from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('subject', 'title', 'text')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['subject'].widget.attrs.update({
                'id': 'subject_id',
                'autofocus':'autofocus',
            })
        self.fields['title'].widget.attrs.update({
                'id': 'title_id',
            })
        self.fields['text'].widget.attrs.update({
                'id': 'text_id',
                'placeholder': 'write post',
            })

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['author'].widget.attrs.update({
                'id': 'author_id',
                'autofocus':'autofocus',
                'placeholdr': 'username or none',
            })
        self.fields['text'].widget.attrs.update({
                'id': 'text_id',
                'placeholder': 'write comment',
            })
