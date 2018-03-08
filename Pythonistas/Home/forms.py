from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateform(UserCreationForm):
    class Meta:
        fields = ( "username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs={ 'type': 'text', 'id': 'name', 'name': 'user_name', 'placeholder': 'User name'}
        self.fields["email"].widget.attrs={ 'type': 'email', 'id': 'email', 'name': 'user_email', 'placeholder': 'Email'}
        self.fields["password1"].widget.attrs={ 'type': 'password', 'id': 'password','name': 'user_password', 'placeholder': 'ENTER YOUR PASSWORD HERE'}
        self.fields["password2"].widget.attrs={ 'type': 'password', 'id': 'password', 'placeholder': 'REPEAT YOUR PASSWORD HERE'}
