from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=20, required=False, help_text='First Name')
    last_name = forms.CharField(
        max_length=20, required=False, help_text='Last Name')
    email = forms.EmailField(
        max_length=254, help_text='Email')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username',)

# The Journal submission form
class EntrySumbission(forms.Form):
    submission = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Type in your Journal Entry',
        'class':'form-control',
        'id':'journal_entry',
        'rows':'7',
        'onkeydown':'countChars()',
        'onkeyup':'countChars()',
        'onmouseout':'countChars()'
    }))
