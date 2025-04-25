from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

MyUser = get_user_model()


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label=_("Enter your password"),
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(label=_("Enter the same password"), widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ("email", "username")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValueError(_("passwords don't match"))

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.save()

        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ("email", "username", "is_active", "is_admin")

    # def clean_password(self):

    #     return self.initial['password']
