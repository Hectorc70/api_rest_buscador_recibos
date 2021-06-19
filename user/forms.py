from django.contrib.auth.forms import UserChangeForm, UserCreationForm


from user.models import NewUser


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = NewUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = NewUser
