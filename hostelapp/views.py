from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
from hostelapp.forms import loginreg, student_dd, parent_dd


def mainpage(request):
    return render(request,'index.html')



def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None and user.is_staff:
            login(request,user)
            return redirect('adminpage')
        elif user is not None and user.is_student:
            if user.student.approval_status==True:
                login(request,user)
                return redirect('student')
            else:
                messages.info(request, 'User not Approved')
        elif user is not None and user.is_parent:
            if user.parent.approval_status==True:
                login(request,user)
                return redirect('parent')
            else:
                messages.info(request,'User not Approved')

        else:
            messages.info(request,'Invalid Credentials')
    return render(request,'login.html')



def register(request):
    return render(request,'register.html')

@login_required(login_url='loginpage')
def adminpage(request):
    return render(request,'admin.html')

@login_required(login_url='loginpage')
def student(request):
    return render(request,'student.html')

@login_required(login_url='loginpage')
def parent(request):
    return render(request,'parent.html')


def stud_reg(request):
    u_form = loginreg()
    s_form = student_dd()
    if request.method == 'POST':
        u_form = loginreg(request.POST)
        s_form = student_dd(request.POST,request.FILES)
        if u_form.is_valid() and s_form.is_valid():
            user = u_form.save(commit=False)
            user.is_student = True
            user.save()
            student = s_form.save(commit=False)
            student.user = user
            student.save()
            messages.info(request, 'Student Registered Successfully')
            return redirect('loginpage')
    return render(request,'stud_register.html',{'u_form':u_form,'s_form':s_form})


def parent_reg(request):
    form = loginreg()
    p_form = parent_dd()
    if request.method == 'POST':
        form = loginreg(request.POST)
        p_form = parent_dd(request.POST)
        if form.is_valid() and p_form.is_valid():
            user = form.save(commit=False)
            user.is_parent = True
            user.save()
            parent = p_form.save(commit=False)
            parent.user = user
            parent.save()
            messages.info(request, 'Parent Registered Successfully')
            return redirect('loginpage')
    return render(request,'parent_register.html',{'form':form,'p_form':p_form})

@login_required(login_url='loginpage')
def logout_view(request):
    logout(request)
    return redirect('loginpage')

