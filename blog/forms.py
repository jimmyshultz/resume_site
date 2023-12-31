from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']
        labels = {'name': 'Name', 'text': 'Comment'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}