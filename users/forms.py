from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name',
                  'last_name', 'password1', 'password2')


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name',)
