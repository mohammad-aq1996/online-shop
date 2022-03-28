from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Comment


class UserCreateForm(UserCreationForm):
    phone_number = forms.CharField(max_length=11)
    address = forms.CharField(max_length=100)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.extra_field = self.cleaned_data["phone_number"]
        user.extra_field = self.cleaned_data["address"]
        if commit:
            user.save()
        return user


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'message']














