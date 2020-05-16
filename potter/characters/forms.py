from django.forms import ModelForm
from .models import user

class userForm(ModelForm):

    class Meta:
        model = user
        exclude = ()