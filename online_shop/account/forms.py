from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'address', 'phone_no', 'first_name', 'last_name']