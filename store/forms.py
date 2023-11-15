from django import forms
from .models import *
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.forms import ModelForm,TextInput,ChoiceField,Textarea

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="رمز عبور", widget=forms.PasswordInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'رمز عبور'
                }))
    password2 = forms.CharField(
        label="تکرار رمز عبور", widget=forms.PasswordInput(
            attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'تکرار رمز عبور'
                }
        )
    )
    username=forms.CharField(label='نام کاربری',widget=TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'نام کاربری'
                }))
    class Meta:
        
        model = CustomUser
        fields = ["username",'first_name','last_name','password1','password2']
        widgets = {
            'first_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'نام'
                }),
            'last_name': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'نام خانوادگی'
                }),
            'address': Textarea(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'ادرس'
                }),
            'post_id': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'کد پستی'
                }),
            
            }

    def clean_username(self):
        username=self.cleaned_data.get("username")
        user_name=CustomUser.objects.filter(username=username)
        if user_name.exists():
            raise ValidationError('نام کاربری تکراری میباشد')
        else:
            return username
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):

        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ['first_name','last_name', "password"]



class WorkOrderForm(forms.ModelForm):
    class Meta:
        model=WorkOrder
        fields=['page_num','description','file']
        widgets = {
            'page_num': forms.NumberInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'rows': 4,
            }),
            'file': forms.FileInput(attrs={
                'class': 'form-control-file',
                'style': 'max-width: 300px;',
            }),
        }
        labels={
            'page_num':'تعداد صفحه',
            'description':'توضیحات',
            'file':'فایل',
        }