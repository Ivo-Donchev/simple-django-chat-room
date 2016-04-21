from django import forms


class MessageForm(forms.Form):
    publisher = forms.CharField(max_length=40,
                                widget=forms.HiddenInput(),
                                required=False)
    message = forms.CharField(max_length=40)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
