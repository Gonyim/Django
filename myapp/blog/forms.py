# blog/forms.py
from django import forms
from .models import Post, Comment

# From: html에 있는 form 태그
# Model Form: model을 사용하는 form
class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'content',) # Model Form 임 장고에서 유효성검사함 왜 why? 
        # field = ('title', 'writer',)
        # widget = {
        #     'content': forms.widgets.Textarea
        # }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']