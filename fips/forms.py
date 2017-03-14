from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('subject', 'title', 'text')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['subject'].widget.attrs.update({'id': 'subject_id'})
        self.fields['title'].widget.attrs.update({'id': 'title_id'})
        self.fields['text'].widget.attrs.update({'id': 'text_id'})
