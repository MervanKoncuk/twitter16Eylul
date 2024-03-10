from .models import *
from django.forms import ModelForm

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'bio', 'image']
        
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs) # miras alınan sınıfın içindeki __init__ fonksiyonun özelliklerini çektik
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control mb-2'})
        