from django import forms
from user.models import User
from captcha.fields import CaptchaField

class LoginForm(forms.ModelForm):
    captcha = CaptchaField(label='验证码')
    class Meta:
        model = User
        fields = ('user_name', 'user_password')
        labels = {
            'user_name':'用户名',
            'user_password':'密码'
        }
        widgets = {
            'user_name':forms.TextInput(attrs={'class':'','required':'', 'autofocus':''}),
            'user_password':forms.PasswordInput(attrs={'class':'', 'required':''})
        }
        # error_messages = {
        #     'user_name':{'required':"用户名不能为空",},
        #     'user_password':{'required':"密码不能为空",},
        # }