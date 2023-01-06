from django import forms
from loginsystem.models import User


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                                'class': 'form-control',
                                                                'name':'first_name',
                                                                }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                                'class': 'form-control',
                                                                'name':'last_name',
                                                                }))
    username = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                            'class': 'form-control',
                                                            'name':'username',
                                                            }))
    email = forms.EmailField(required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                            'class': 'form-control',
                                                            'name':'email',
                                                            }))
    password = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                    'class': 'form-control',
                                                                    'data-toggle': 'password',
                                                                    'id': 'password',
                                                                    'name':'password'
                                                                    }))
    password_confirm = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                    'class': 'form-control',
                                                                    'data-toggle': 'password',
                                                                    'id': 'password',
                                                                    'name':'password_confirm'
                                                                    }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    email = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                            'class': 'form-control',
                                                            'name':'email',
                                                            'type':'email',
                                                            }))
    password = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                'class': 'form-control',
                                                                'data-toggle': 'password',
                                                                'id': 'password',
                                                                'name': 'password',
                                                                }))
    # remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password']