from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter post title', 'style': 'font-size:1rem'}),
            'body': forms.Textarea(attrs={'placeholder': 'Write your post here...', 'style': 'font-size:1rem'}),
        }
