from allauth.account.forms import LoginForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms
from django.template.defaultfilters import filesizeformat
from django.conf import settings

class MyCustomLoginForm(LoginForm):
    """ Login Form """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({'class':'form-control', 'placeholder':'login'})
        self.fields['password'].widget.attrs.update({'class':'form-control', 'placeholder':'password'})

class UserForm(forms.ModelForm):
    """ User form """

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилия'

class ProfileForm(forms.ModelForm):
    """ Profile form """

    avatar = forms.ImageField(label='Загрузить аватар', required=False, error_messages = {'invalid': "Image files only"}, widget=forms.FileInput)
    class Meta:
        model = Profile
        fields = ('about', 'avatar',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['about'].label = 'О себе'
        self.fields['about'].widget.attrs.update({'rows':4, 'cols':15})
    
    def clean_avatar(self):
        """ Validate uploaded file type and size """
        
        content = self.cleaned_data['avatar']
        try:
            content_type = content.content_type.split('/')[0]
            if content_type in settings.CONTENT_TYPES:
                if content.size > int(settings.MAX_UPLOAD_SIZE):
                    raise forms.ValidationError( 'Please keep filesize under %s. Current filesize %s' % (filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(content.size)))
            else:
                raise forms.ValidationError('File type is not supported')
        except AttributeError:
            pass
        return content
