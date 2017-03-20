from django import forms

from .models import Post, Comment, UploadFile, ImageComment

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

class ImageCommentForm(forms.ModelForm):
    class Meta:
        model = ImageComment
        fields = ('text', 'image')

    def __init__(self, *args, **kwargs):
        super(ImageCommentForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False
        self.fields['text'].widget.attrs.update({
                'id': 'text_id',
                'autofocus':'autofocus',
                'placeholdr': 'write a comment',
            })
        self.fields['image'].widget.attrs.update({
                'id': 'image_id',
                'placeholder': 'upload a image',
            })

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ('subject', 'title', 'upload_file')

    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        self.fields['upload_file'].required = False
        self.fields['subject'].widget.attrs.update({
                'id': 'subject_id',
                'value': 3,
            })
        self.fields['title'].widget.attrs.update({
                'id': 'title_id',
                'autofocus':'autofocus',
            })
        self.fields['upload_file'].widget.attrs.update({
                'id': 'upload_file_id',
                'placeholder': 'upload a file',
            })