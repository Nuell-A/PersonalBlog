from django import forms
from .models import Post

'''
User created file.

This file will be used to style the CSS on our add_post.html file.
'''

# CSS class
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        # The dictionary below is used to pass CSS classes.
        widgets = {
            # TextInput is used for short inputs, Select for dropdowns, and 
            # TextArea for large content bodies

            # You can add multiple HTML tags.
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Placeholder test in forms.py'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }