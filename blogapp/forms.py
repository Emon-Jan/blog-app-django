from django.contrib.auth import get_user_model
from django.forms import ModelForm, TextInput, Textarea, PasswordInput, EmailInput
from django.contrib.auth.forms import UserCreationForm
from django import forms
from blogapp.models import Post, Comment


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'image']

        widgets = {
            'title': TextInput(attrs={'class': 'textinputclass'}),
            'text': Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
        }


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['author', 'text']

        widgets = {
            'author': TextInput(attrs={'class': 'textinputclass'}),
            'text': Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', ]

