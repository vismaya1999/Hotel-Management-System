from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from hostelapp.forms import room_dd
from hostelapp.models import hostel, attendance, staff, payment


@login_required(login_url='loginpage')
def parent_hostel(request):
    data=hostel.objects.all()
    return render(request,'parent_hostel.html',{'data':data})

@login_required(login_url='loginpage')
def parent_attendance(request):
    data=attendance.objects.all()
    return render(request,'parent_attendance.html',{'data':data})

@login_required(login_url='loginpage')
def parent_room(request):
    form = room_dd()
    if request.method == 'POST':
        form = room_dd(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('parent')
    return render(request, 'parent_room.html', {'form': form})

@login_required(login_url='loginpage')
def parent_staff(request):
    data=staff.objects.all()
    return render(request,'parent_staff.html',{'data':data})

@login_required(login_url='loginpage')
def parent_delete(request):
    user=request.user
    if request.method == 'POST':
        user.delete()
        messages.info(request,"Your Account Deleted Successfully")
        return redirect('loginpage')
    return render(request,'parent_delete.html')


@login_required(login_url='loginpage')
def parent_view_pay(request):
    data=payment.objects.all()
    return render(request,'parent_view_pay.html',{'data':data} )

@login_required(login_url='loginpage')
def parent_fee(request):
    data=staff.objects.all()
    return render(request,'parent_fee.html',{'data':data})
