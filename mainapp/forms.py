from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import DateInput

from .models import Consultation, Employment, Customer, PlaceOfWork


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ("name", "email",  "message")
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Есіміңіз"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Почтаңыз"}),
            "message": forms.Textarea(
                attrs={"class": "form-control", "cols": 30, "rows": 7, "placeholder": "Сұрағыңыз...", }),

        }


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='Есіміңіз',
                                 widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Есіміңіз"}))
    fatherland = forms.CharField(label='Әкеңіздің аты', widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Әкеңіздің аты"}))
    last_name = forms.CharField(label='Тегіңіз',
                                widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Тегіңіз"}))
    jsn = forms.CharField(label='ЖСН', widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "ЖСН"}))
    birthday = forms.DateField(label='Туылған күніңіз', widget=DateInput(
        attrs={"class": "form-control", "placeholder": "Туылған күніңіз"}))
    education = forms.CharField(label='Біліміңіз',
                                widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Біліміңіз"}))
    profession = forms.CharField(label='Кәсіби мамандығы', widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Кәсіби мамандығы"}))
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Логин"}))
    email = forms.EmailField(label='Почта',
                             widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Почта"}))
    password1 = forms.CharField(label='password1',
                                widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Құпия сөз"}))
    password2 = forms.CharField(label='password2',
                                widget=forms.PasswordInput(
                                    attrs={"class": "form-control", "placeholder": "Құпия сөзді қайталаңыз"}))

    class Meta:
        model = User
        fields = (
            'first_name', 'fatherland', 'last_name',
            'jsn', 'birthday', 'education', 'profession',
            'username', 'email',
            'password1', 'password2',)


class LoginForm(forms.ModelForm):
    login = forms.CharField(label='Логин',
                            widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Логин"}))
    password = forms.CharField(label='Құпия сөз',
                               widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Құпия сөз"}))

    class Meta:
        model = User
        fields = ('login', 'password',)


class EmploymentForm(forms.ModelForm):
    def __init__(self, place, *args, **kwargs):
        super(EmploymentForm, self).__init__(*args, **kwargs)
        self.fields['customer'] = forms.ModelChoiceField(
            queryset=Employment.objects.filter(customer=kwargs['instance'].customer), initial=True,
            widget=forms.Select(attrs={"class": "form-control", "readonly": "readonly"}))
        self.fields['place_of_work'] = forms.ModelChoiceField(
            queryset=place, initial=True,
            widget=forms.Select(attrs={"class": "form-control", "readonly": "readonly"}))

    class Meta:
        model = Employment
        fields = ("place_of_work", "position", "data_created", "data_ended", "command", "file")

        widgets = {
            "position": forms.TextInput(attrs={"class": "form-control", "placeholder": "Лауазымы"}),
            # "data_created": DateInput(attrs={"class": "form-control", 'type': 'date'}),
            # "data_ended": DateInput(attrs={"class": "form-control", 'type': 'date'}),
            "data_created": DateInput(attrs={"class": "form-control", "placeholder": "жыл-ай-күн"}),
            "data_ended": DateInput(attrs={"class": "form-control", "placeholder": "жыл-ай-күн"}),
            "command": forms.TextInput(attrs={"class": "form-control", "placeholder": "Құжат,күні"}),
            "file": forms.FileInput(attrs={"class": "form-control", }),
        }


class AddEmploymentForm(forms.ModelForm):
    def __init__(self, user, place, staff, *args, **kwargs):
        super(AddEmploymentForm, self).__init__(*args, **kwargs)
        if staff:
            q_place = PlaceOfWork.objects.all()
            q_customer = Customer.objects.all()
        else:
            q_place = PlaceOfWork.objects.filter(id=place)
            q_customer = Customer.objects.filter(user=user)
        self.fields['customer'] = forms.ModelChoiceField(
            queryset=Customer.objects.all(), initial=True,
            widget=forms.Select(attrs={"class": "form-control", "readonly": "readonly"}))
        self.fields['place_of_work'] = forms.ModelChoiceField(
            queryset=q_place, initial=True,
            widget=forms.Select(attrs={"class": "form-control", "readonly": "readonly"}))

    class Meta:
        model = Employment
        fields = ('customer', "place_of_work", "position", "data_created", "data_ended", "command")

        widgets = {
            "position": forms.TextInput(attrs={"class": "form-control", "placeholder": "Лауазымы"}),
            # "data_created": DateInput(attrs={"class": "form-control", 'type': 'date'}),
            # "data_ended": DateInput(attrs={"class": "form-control", 'type': 'date'}),
            "data_created": DateInput(attrs={"class": "form-control", "placeholder": "жыл-ай-күн"}),
            "data_ended": DateInput(attrs={"class": "form-control", "placeholder": "жыл-ай-күн"}),
            "command": forms.TextInput(attrs={"class": "form-control", "placeholder": "Құжат,күні"}),
        }


class PlaceOfWorkForm(UserCreationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Логин"}))
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Мекеме аты"}))
    bin = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "БСН(БИН)"}))
    password1 = forms.CharField(label='password1',
                                widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Құпия сөз"}))
    password2 = forms.CharField(label='password2',
                                widget=forms.PasswordInput(
                                    attrs={"class": "form-control", "placeholder": "Құпия сөзді қайталаңыз"}))

    class Meta:
        model = User
        fields = ('username', 'name', 'bin', 'password1', 'password2')
