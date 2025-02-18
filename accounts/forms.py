# accounts/forms.py
from django import forms
from .models import CustomUser

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        # Check if user exists
        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            raise forms.ValidationError("Invalid username or password")

        # Verify password
        if not user.check_password(password):
            raise forms.ValidationError("Invalid username or password")

        cleaned_data['user'] = user  # Add the user to the cleaned data
        return cleaned_data
