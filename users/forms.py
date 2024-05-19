from django import forms
from django.core.exceptions import ValidationError
from users.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=5,
        widget=forms.TextInput(attrs={"placeholder": "5자이상"}),
        label="아이디",
    )
    password = forms.CharField(
        min_length=5,
        widget=forms.PasswordInput(attrs={"placeholder": "5자이상"}),
        label="비밀번호",
    )


class SignupForm(forms.Form):
    username = forms.CharField(label="아이디")
    password1 = forms.CharField(widget=forms.PasswordInput, label="비밀번호")
    password2 = forms.CharField(widget=forms.PasswordInput, label="비밀번호 확인")

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise ValidationError(f"입력한 사용자명{{username}}은 이미 사용중입니다")
        return username

    def clean(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            self.add_error("password2", "비밀번호와 비밀번호 확인값이 다릅니다.")

    def save(self):
        username = self.cleaned_data["username"]
        password1 = self.cleaned_data["password1"]
        user = User.objects.create_user(
            username=username,
            password=password1,
        )
        return user
