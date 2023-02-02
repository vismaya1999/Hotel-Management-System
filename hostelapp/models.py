from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Login(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)

class student(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,primary_key=True,related_name='student')
    name=models.CharField(max_length=30)
    admission_no=models.CharField(max_length=7)
    contact_no=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=50)
    approval_status=models.IntegerField(default=0)
    profile=models.ImageField(upload_to='profile')

    def __str__(self):
        return self.name

class parent(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='parent',primary_key=True)
    student=models.ForeignKey(student,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    contact_no = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=50)
    approval_status = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class hostel(models.Model):
    hostel_name=models.CharField(max_length=10)
    location=models.CharField(max_length=10)
    fee_details=models.CharField(max_length=10)
    room_details=models.CharField(max_length=10)
    contact_no=models.IntegerField()
    hostel_image=models.ImageField(upload_to='view_hostel')

    def __str__(self):
        return self.hostel_name

class food(models.Model):
    Breakfast=models.CharField(max_length=50)
    Lunch=models.CharField(max_length=50)
    Snacks=models.CharField(max_length=50)
    Dinner=models.CharField(max_length=50)

class complaints(models.Model):
    user=models.ForeignKey(Login,on_delete=models.DO_NOTHING)
    date=models.DateField(auto_now=True)
    complaints=models.CharField(max_length=100)
    reply=models.TextField(null=True,blank=True)
    # reply=models.CharField(max_length=100)

class fee(models.Model):
    hostel_name=models.ForeignKey(hostel,on_delete=models.CASCADE)
    mess_fee=models.FloatField(default=0)
    hostel_rent=models.FloatField(default=0)
    amount=models.FloatField(default=0)

    def __str__(self):
        return self.amount

class notification(models.Model):
    date=models.DateField()
    message=models.CharField(max_length=100)

class attendance(models.Model):
    student_name=models.ForeignKey(student,on_delete=models.CASCADE)
    date=models.DateField()
    attendance=models.CharField(max_length=50)
    def __str__(self):
        return self.student_name

class staff(models.Model):
    staff_name=models.CharField(max_length=50)
    age=models.IntegerField()
    contact_no=models.IntegerField()

class room(models.Model):
    student_name=models.ForeignKey(student,on_delete=models.CASCADE)
    room_type = models.CharField(max_length=50)
    booking_date=models.DateField()
    joining_date=models.DateField()
    approval_status=models.IntegerField(default=0)

    def __str__(self):
        return self.student_name

class reviews(models.Model):
    name=models.CharField(max_length=150)
    date=models.DateField()
    review=models.CharField(max_length=100)

class payment(models.Model):
    student_name = models.ForeignKey(student,on_delete=models.CASCADE)
    room_rent = models.IntegerField(default=0)
    mess_bill = models.IntegerField(default=0)
    from_date = models.DateField()
    to_date = models.DateField()
    amount = models.IntegerField(default=0)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.student_name


