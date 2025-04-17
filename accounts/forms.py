from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=CustomUser
        fields=UserCreationForm.Meta.Fields = ('name',)

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model=CustomUser
        fields=UserChangeForm.Meta.fields
