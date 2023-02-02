import datetime
import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from hostelapp.models import student, parent, Login, hostel, food, fee, complaints, notification, attendance, staff, \
    room, reviews, payment


class DateInput(forms.DateInput):
    input_type = 'date'

def phone_number_validator(value):
    if not re.compile(r'^[6-9]\d{9}$').match(value):
        raise ValidationError('Enter a valid phone number')

class loginreg(UserCreationForm):
    class Meta:
        model=Login
        fields=('username','password1','password2')

class student_dd(forms.ModelForm):
    contact_no=forms.CharField(validators=[phone_number_validator])
    email=forms.CharField(validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[com]+$',message='Invalid id')])
    class Meta:
        model = student
        exclude = ('user','approval_status',)
    def clean_name(self):
        username=self.cleaned_data["name"]
        pname=parent.objects.filter(name=username)
        sname=student.objects.filter(name=username)
        if pname.exists():
            raise forms.ValidationError("This name already registered")
        if sname.exists():
            raise forms.ValidationError("This name already registered")
        return username
    def clean_email(self):
        mail=self.cleaned_data["email"]
        pmail=parent.objects.filter(email=mail)
        smail=student.objects.filter(email=mail)
        if pmail.exists():
            raise forms.ValidationError("This email already registered")
        if smail.exists():
            raise forms.ValidationError("This email already registered")
        return mail
    def clean_contact_no(self):
        no=self.cleaned_data["contact_no"]
        pno=parent.objects.filter(contact_no=no)
        sno=student.objects.filter(contact_no=no)
        if pno.exists():
            raise forms.ValidationError("This contact number already registered")
        if sno.exists():
            raise forms.ValidationError("This contact number already registered")
        return no

class parent_dd(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])
    email = forms.CharField(validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[com]+$', message='Invalid id')])
    class Meta:
            model = parent
            exclude = ('user','approval_status',)
    def clean_email(self):
        mail=self.cleaned_data["email"]
        pmail=parent.objects.filter(email=mail)
        smail=student.objects.filter(email=mail)
        if pmail.exists():
            raise forms.ValidationError("This email already registered")
        if smail.exists():
            raise forms.ValidationError("This email already registered")
        return mail
    def clean_contact_no(self):
        no=self.cleaned_data["contact_no"]
        pno=parent.objects.filter(contact_no=no)
        sno=student.objects.filter(contact_no=no)
        if pno.exists():
            raise forms.ValidationError("This contact number already registered")
        if sno.exists():
            raise forms.ValidationError("This contact number already registered")
        return no
class hostel_dd(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])
    class Meta:
        model=hostel
        fields='__all__'

class food_dd(forms.ModelForm):
    class Meta:
        model= food
        fields='__all__'

class fee_dd(forms.ModelForm):
    # date=forms.DateField(widget=DateInput)
    class Meta:
        model= fee
        fields='__all__'

class complaints_dd(forms.ModelForm):
    date=forms.DateField(widget=DateInput)
    class Meta:
        model= complaints
        exclude=('reply','user')

class reply(forms.ModelForm):
    class Meta:
        model= complaints
        exclude='user','date','complaints',


class notification_dd(forms.ModelForm):
    date=forms.DateField(widget=DateInput)
    class Meta:
        model= notification
        fields='__all__'

attendance_choice = (
    ('Present','Present'),
    ('Absent','Absent')
)

class attendance_dd(forms.ModelForm):
    date=forms.DateField(widget=DateInput)
    attendance=forms.ChoiceField(choices=attendance_choice,widget=forms.RadioSelect)
    class Meta:
        model= attendance
        fields='__all__'

class staff_dd(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])
    class Meta:
        model= staff
        fields='__all__'


room_type_choice = (
    ('Select Room Type','Select Room Type'),
    ('Single Room','Single Room'),
    ('Double Room','Double Room'),
    ('Triple Room','Triple Room'),
    ('Quad Room','Quad Room'),
)
class room_dd(forms.ModelForm):
    booking_date = forms.DateField(widget=DateInput)
    joining_date = forms.DateField(widget=DateInput)
    room_type=forms.CharField(label='Room Type',widget=forms.Select(choices=room_type_choice))
    class Meta:
        model= room
        exclude='approval_status',

class reviews_dd(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model= reviews
        fields='__all__'


class paymentform(forms.ModelForm):
    from_date = forms.DateField(widget=DateInput)
    to_date = forms.DateField(widget=DateInput)
    class Meta:
        model = payment
        fields ="__all__"
        exclude = ('status',)