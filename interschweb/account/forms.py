from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
	email = forms.EmailField(required=True, widget =
		forms.EmailInput(attrs = {'class':'form-control',
			'placeholder':'이메일을 적어주세요.', 'required':'True',}))
	phone = forms.DecimalField(required=True, widget =
		forms.NumberInput(attrs = {'class':'form-control',
			'placeholder':'숫자만 적어주세요.', 'required':'True',}))

	class Meta:
		model = User
		fields = ["username", "email", "phone", "password1", "password2",]
