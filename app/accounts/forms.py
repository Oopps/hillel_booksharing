from django import forms
from accounts.tasks import send_activate_account_email
from accounts.models import User
from booksharing.tokens import account_activation_token


class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(min_length=6)
    password2 = forms.CharField(min_length=6)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password1'] != cleaned_data['password2']:
            raise forms.ValidationError('Passwords have match!')
        return cleaned_data

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if User.objects.filter(email__iexact=email).exists():
    #         login_url = reverse('login')
    #         raise forms.ValidationError(
    #             f'Seems that you already have account! Please visit {login_url}')
    #     return email.lower()

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.is_active = False
        instance.set_password(self.cleaned_data['password1'])

        if commit:
            instance.save()
        token = account_activation_token.make_token(instance.username)
        send_activate_account_email.delay(instance.username, token)

        return instance
