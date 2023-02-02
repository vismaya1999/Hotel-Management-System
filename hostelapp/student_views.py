from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from hostelapp.forms import complaints_dd, room_dd, reviews_dd, student_dd
from hostelapp.models import hostel, food, complaints, fee, attendance, student, room, payment


@login_required(login_url='loginpage')
def stud_hostel(request):
    data=hostel.objects.all()
    return render(request,'stud_hostel.html',{'data':data})


@login_required(login_url='loginpage')
def stud_food(request):
    data=food.objects.all()
    return render(request,'stud_food.html',{'data':data})


@login_required(login_url='loginpage')
def stud_complaint(request):
    form = complaints_dd()
    u=request.user
    if request.method == 'POST':
        form = complaints_dd(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
            return redirect('stud_viewcomplaint')
    return render(request, 'stud_complaint.html', {'form': form})
@login_required(login_url='loginpage')
def stud_viewcomplaint(request):
    data=complaints.objects.filter(user=request.user)
    return render(request,'stud_viewcomplaint.html',{'data':data})

@login_required(login_url='loginpage')
def stud_profile(request):
    data=student.objects.get(user=request.user)
    return render(request,'stud_profile.html',{'data':data})

@login_required(login_url='loginpage')
def update_profile(request):
        student1 = student.objects.get(user=request.user)
        form = student_dd(instance=student1)
        if request.method == "POST":
            form = student_dd(request.POST, instance=student1)
        if form.is_valid():
            form.save()
            return redirect('stud_profile')
        return render(request, 'update_profile.html', {'form': form})

@login_required(login_url='loginpage')
def stud_fee(request):
    data=fee.objects.all()
    return render(request,'stud_fee.html',{'data':data})

@login_required(login_url='loginpage')
def stud_attendance(request):
    u=student.objects.get(user=request.user)
    data=attendance.objects.filter(student_name=u)
    return render(request,'stud_attendance.html',{'data':data})

@login_required(login_url='loginpage')
def stud_room(request):
    form = room_dd()
    if request.method == 'POST':
        form = room_dd(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('stud_viewroom')
    return render(request, 'stud_room.html', {'form': form})

@login_required(login_url='loginpage')
def approval_booking(request,id):
    student1 = room.objects.get(id=id)
    student1.approval_status = 1
    student1.save()
    messages.info(request, 'Approved Successfully')
    return HttpResponseRedirect(reverse('stud_viewroom'))

@login_required(login_url='loginpage')
def reject_booking(request,id):
    student1 = room.objects.get(id=id)
    student1.approval_status = 2
    student1.save()
    messages.info(request,'Rejected Successfully')
    return redirect('stud_viewroom')

@login_required(login_url='loginpage')
def stud_viewroom(request):
    data=room.objects.all()
    return render(request,'stud_viewroom.html',{'data':data})

@login_required(login_url='loginpage')
def stud_reviews(request):
    form = reviews_dd()
    if request.method == 'POST':
        form = reviews_dd(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student')
    return render(request, 'stud_reviews.html', {'form': form})

@login_required(login_url='loginpage')
def student_delete(request):
    user=request.user
    if request.method == 'POST':
        user.delete()
        messages.info(request,"Your Account Deleted Successfully")
        return redirect('loginpage')
    return render(request,'student_delete.html')

@login_required(login_url='loginpage')
def view_studpay(request):
    data=payment.objects.all()
    return render(request,'view_studpay.html',{'data':data} )
@login_required(login_url='Login')
def approve_payment(request,id):
    pay1=payment.objects.get(id=id)
    pay1.status = 1
    pay1.save()
    messages.info(request,"student paid succesfully")
    return redirect('view_studpay')


@login_required(login_url='loginpage')
def reject_payment(request,id):
    pay1=payment.objects.get(id=id)
    pay1.status = 2
    pay1.save()
    messages.info(request,"not paid")
    return redirect('view_studpay')

