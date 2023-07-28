# django imports
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm

from .services import clean_password

# user object
User = get_user_model()


class UserRegistrationForm(UserCreationForm):
    """
    Custom User Registration Form.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields["password2"].required = False
        
    email = forms.EmailField(
        label="",
        required=True,
        widget=forms.TextInput(attrs={
            "name": "email",
            "type": "email",
            "id": "email",
            "placeholder": "Email",
            "class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        })
    )

    username = forms.CharField(
        label="",
        required=False,
        widget=forms.TextInput(attrs={
            "name": "username",
            "id": "username",
            "placeholder": "Username",
        })
    )

    password1 = forms.CharField(
        label="",
        required=True,
        widget=forms.PasswordInput(attrs={
            "type": "password",
            "name": "password1",
            "id": "password1",
            "placeholder": "••••••••",
            "class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        })
    )
    
    password2 = forms.CharField(
        label="",
        required=True,
        widget=forms.PasswordInput(attrs={
            "type": "password",
            "name": "password2",
            "id": "password2",
            "placeholder": "••••••••",
            "class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        })
    )

    class Meta:
        model = User
        fields = ("email", "password1", "password2")

    def clean_password1(self, *args, **kwargs):
        password = self.cleaned_data.get("password1")

        return clean_password(password)


class LoginForm(AuthenticationForm):
    """ Custom Authentication/Login form """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].widget.attrs.update({
            "placeholder": "••••••••••",
            "id": "password",
            "name": "password",
            "class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        })
        
    username = forms.CharField(
        label="",
        required=False,
        widget=forms.TextInput(attrs={
            "type": "email",
            "name": "email",
            "id": "email",
            "placeholder": "name@company.com",
            "class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        })
    )

    class Meta:
        model = User
        fields = ("username", "password")


class ResetPasswordForm(PasswordResetForm):
    """ Custom PasswordResetForm """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    email = forms.EmailField(
        label="",
        required=True,
        widget=forms.TextInput(attrs={
            "name": "email",
            "type": "email",
            "id": "email",
            "placeholder": "Email"
        })
    )
    
    class Meta:
        model = User
        fields = ("email",)


class SetNewPasswordForm(SetPasswordForm):
    """ Custom SetPasswordForm """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    new_password1 = forms.CharField(
        label="",
        required=True,
        widget=forms.PasswordInput(attrs={
            "type": "password",
            "name": "new_password1",
            "placeholder": "Password"
        })
    )
    
    new_password2 = forms.CharField(
        label="",
        required=True,
        widget=forms.PasswordInput(attrs={
            "type": "password",
            "name": "new_password2",
            "placeholder": "Confirm Password"
        })
    )
    
    class Meta:
        model = User
        fields = ("new_password1", "new_password2")
        
    def clean_new_password1(self, *args, **kwargs):
        password = self.cleaned_data.get("new_password1")

        return clean_password(password)

