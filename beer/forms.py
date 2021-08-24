from django import forms
from .models import Comment, Recomment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
        labels = {
            'comment_text': '리뷰내용',
        }

class RecommentForm(forms.ModelForm):
    class Meta:
        model = Recomment
        fields = ['comment_text']
        labels = {
            'comment_text': '댓글내용',
        }