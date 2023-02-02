from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from hostelapp.forms import hostel_dd, food_dd, notification_dd, attendance_dd, staff_dd, room_dd, \
    complaints_dd, reply, paymentform, fee_dd
from hostelapp.models import student, parent, hostel, food, fee, complaints, notification, attendance, staff, room, \
    reviews, payment


# ----Student view----
@login_required(login_url='loginpage')
def stud_viewf(request):
    data= student.objects.all()
    return render(request,'view.html',{'data':data})

# ---Parent View----
@login_required(login_url='loginpage')
def parent_viewf(request):
    data= parent.objects.all()
    return render(request,'parent_view.html',{'data':data})

# ------------------------------------------------------------------------------------------------------------------------
# *******ADMIN SIDE*******
# ------------------------------------------------------------------------------------------------------------------------

# ----approve/reject student----
@login_required(login_url='loginpage')
def approval_student(request,id):
    student1 = student.objects.get(user_id=id)
    student1.approval_status = 1
    student1.save()
    messages.info(request, 'Approved Successfully')
    return HttpResponseRedirect(reverse('stud_viewf'))

@login_required(login_url='loginpage')
def reject_student(request,id):
    student1 = student.objects.get(id=id)
    student1.approval_status = 2
    student1.save()
    messages.info(request,'Rejected Successfully')
    return redirect('stud_viewf')

# ----Approve/Reject Parent----
@login_required(login_url='loginpage')
def approval_parent(request,id):
    parent1 = parent.objects.get(user_id=id)
    parent1.approval_status = 1
    parent1.save()
    messages.info(request, 'Approved Successfully')
    return HttpResponseRedirect(reverse('parent_viewf'))

@login_required(login_url='loginpage')
def reject_parent(request,id):
    parent1 = parent.objects.get(user_id=id)
    parent1.approval_status = 2
    parent1.save()
    messages.info(request,'Rejected Successfully')
    return redirect('parent_viewf')


# ----Hostal details----
@login_required(login_url='loginpage')
def add_hostel(request):
    form=hostel_dd()
    if request.method=='POST':
        form=hostel_dd(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_hostel')
    return render(request,'add_hostel.html',{'form': form})

@login_required(login_url='loginpage')
def view_hostel(request):
    data=hostel.objects.all()
    return render(request,'view_hostel.html',{'data':data})

@login_required(login_url='loginpage')
def update_hostel(request,id):
    hostel1 = hostel.objects.get(id=id)
    form = hostel_dd(instance=hostel1)
    if request.method == "POST":
        form = hostel_dd(request.POST, instance=hostel1)
    if form.is_valid():
        form.save()
        return redirect('view_hostel')
    return render(request, 'add_hostel.html', {'form': form})

@login_required(login_url='loginpage')
def delete_hostel(request, id):
    hostel.objects.get(id=id).delete()
    return redirect('view_hostel')

# ---- Food_details----

@login_required(login_url='loginpage')
def add_food(request):
    form=food_dd()
    if request.method=='POST':
        form=food_dd(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_food')
    return render(request, 'add_food.html',{'form': form})

@login_required(login_url='loginpage')
def view_food(request):
    data=food.objects.all()
    return render(request,'view_food.html',{'data':data})

@login_required(login_url='loginpage')
def update_food(request,id):
    food1 = food.objects.get(id=id)
    form = food_dd(instance=food1)
    if request.method == "POST":
        form = food_dd(request.POST, instance=food1)
    if form.is_valid():
        form.save()
        return redirect('view_food')
    return render(request, 'add_food.html', {'form': form})

@login_required(login_url='loginpage')
def delete_food(request, id):
    food.objects.get(id=id).delete()
    return redirect('view_food')

# ----fee details---

@login_required(login_url='loginpage')
def add_fee(request):
    form = fee_dd()
    if request.method == 'POST':
        form = fee_dd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_fee')
    return render(request,'add_fee.html',{'form':form})


@login_required(login_url='loginpage')
def view_fee(request):
    data=fee.objects.all()
    return render(request,'view_fee.html',{'data':data})

@login_required(login_url='loginpage')
def update_fee(request,id):
    fee1 = fee.objects.get(id=id)
    form = fee_dd(instance=fee1)
    if request.method == "POST":
        form =fee_dd(request.POST, instance=fee1)
    if form.is_valid():
        form.save()
        return redirect('view_fee')
    return render(request, 'add_fee.html', {'form': form})

@login_required(login_url='loginpage')
def delete_fee(request, id):
    fee.objects.get(id=id).delete()
    return redirect('view_fee')

# ----Manage Complaints----

@login_required(login_url='loginpage')
def view_complaints(request):
    data=complaints.objects.all()
    return render(request,'view_complaints.html',{'data':data})

def reply_complaint(request,id):
    f=complaints.objects.get(id=id)
    if request.method == 'POST':
        r=request.POST.get('reply')
        f.reply=r
        f.save()
        return redirect('view_complaints')
    return render(request, 'reply_complaint.html', {'f': f})


# ----Notification----

@login_required(login_url='loginpage')
def add_notification(request):
    form = notification_dd()
    if request.method == 'POST':
        form = notification_dd(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_notification')
    return render(request, 'add_notification.html', {'form': form})

@login_required(login_url='loginpage')
def view_notification(request):
    data=notification.objects.all()
    return render(request,'view_notification.html',{'data':data})

@login_required(login_url='loginpage')
def update_notification(request,id):
    notification1 = notification.objects.get(id=id)
    form = notification_dd(instance=notification1)
    if request.method == "POST":
        form = notification_dd(request.POST, instance=notification1)
    if form.is_valid():
        form.save()
        return redirect('view_notification')
    return render(request, 'add_notification.html', {'form': form})

@login_required(login_url='loginpage')
def delete_notification(request, id):
    notification.objects.get(id=id).delete()
    return redirect('view_notification')

# ----attendance----

@login_required(login_url='loginpage')
def add_attendance(request):
    form = attendance_dd()
    if request.method == 'POST':
        form = attendance_dd(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_attendance')
    return render(request, 'add_attendance.html', {'form': form})

@login_required(login_url='loginpage')
def view_attendance(request):
    data=attendance.objects.all()
    return render(request,'view_attendance.html',{'data':data})

@login_required(login_url='loginpage')
def update_attendance(request,id):
    attendance1 = attendance.objects.get(id=id)
    form = attendance_dd(instance=attendance1)
    if request.method == "POST":
        form = attendance_dd(request.POST, instance=attendance1)
    if form.is_valid():
        form.save()
        return redirect('view_attendance')
    return render(request, 'add_attendance.html', {'form': form})

@login_required(login_url='loginpage')
def delete_attendance(request, id):
    attendance.objects.get(id=id).delete()
    return redirect('view_attendance')

# ----Staff----

@login_required(login_url='loginpage')
def add_staff(request):
    form = staff_dd()
    if request.method == 'POST':
        form = staff_dd(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_staff')
    return render(request, 'add_staff.html', {'form': form})

@login_required(login_url='loginpage')
def view_staff(request):
    data=staff.objects.all()
    return render(request,'view_staff.html',{'data':data})

@login_required(login_url='loginpage')
def update_staff(request,id):
    staff1 = staff.objects.get(id=id)
    form = staff_dd(instance=staff1)
    if request.method == "POST":
        form = staff_dd(request.POST, instance=staff1)
    if form.is_valid():
        form.save()
        return redirect('view_staff')
    return render(request, 'add_staff.html', {'form': form})

@login_required(login_url='loginpage')
def delete_staff(request, id):
    staff.objects.get(id=id).delete()
    return redirect('view_staff')

# ----RoomBooking-----

@login_required(login_url='loginpage')
def add_room(request):
    form = room_dd()
    if request.method == 'POST':
        form = room_dd(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_room')
    return render(request, 'add_room.html', {'form': form})

@login_required(login_url='loginpage')
def approval_booking(request,id):
    student1 = room.objects.get(id=id)
    student1.approval_status = 1
    student1.save()
    messages.info(request, 'Approved Successfully')
    return HttpResponseRedirect(reverse('view_room'))

@login_required(login_url='loginpage')
def reject_booking(request,id):
    student1 = room.objects.get(id=id)
    student1.approval_status = 2
    student1.save()
    messages.info(request,'Rejected Successfully')
    return redirect('view_room')

@login_required(login_url='loginpage')
def view_room(request):
    data=room.objects.all()
    return render(request,'view_room.html',{'data':data})

@login_required(login_url='loginpage')
def update_room(request,id):
    room1 = room.objects.get(id=id)
    form = room_dd(instance=room1)
    if request.method == "POST":
        form = room_dd(request.POST, instance=room1)
    if form.is_valid():
        form.save()
        return redirect('view_room')
    return render(request, 'add_room.html', {'form': form})

@login_required(login_url='loginpage')
def delete_room(request, id):
    room.objects.get(id=id).delete()
    return redirect('view_room')

# -----reviews----
@login_required(login_url='loginpage')
def view_reviews(request):
    data=reviews.objects.all()
    return render(request,'view_reviews.html',{'data':data})

# ----------payment details----------


@login_required(login_url='Login')
def add_adminpay(request):
    form = paymentform()
    if request.method == "POST":
        form = paymentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_payment')
    return render(request,'add_adminpay.html',{'form':form})


@login_required(login_url='Login')
def view_payment(request):
    data=payment.objects.all()
    return render(request,'view_payment.html',{'data':data})



@login_required(login_url='Login')
def pay_update(request,id):
    payment1=payment.objects.get(id=id)
    form=paymentform(instance=payment1)
    if request.method=="POST":
        form=paymentform(request.POST,instance=payment1)
    if form.is_valid():
        form.save()
        return redirect('view_payment')
    return render(request,'add_adminpay.html',{'form':form})


@login_required(login_url='Login')
def pay_delete(request,id):
    payment.objects.get(id=id).delete()
    return redirect('view_payment')