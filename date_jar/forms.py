from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from date_jar.models import Event


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=False)


class NewEvent(forms.ModelForm):
    name = forms.CharField(required=True, max_length=40)

    class Meta:
        model = Event
        fields = ('name', 'description','category','location','url', 'address', 'image', )

class AddEvent(forms.ModelForm):
    name = forms.CharField(required=True, max_length=40)

    class Meta:
        model = Event
        fields = ('name', 'description','category','location','url', 'address', 'image', )



class RemoveEvent(forms.ModelForm):
    name = forms.CharField(required=True, max_length=40)

    class Meta:
        model = Event
        fields = ('name', 'description','category','location','url', 'address', 'image', )


# class RandomEvent(forms.ModelForm):


# class EditProfile(forms.ModelForm):
    # username = None
    # password1 = None
    # password2 = None

    # class Meta:
    #     model = User
    #     fields = (
    #         'username'
    #         'email',
    #         'first_name',
    #         'last_name',
    #     )