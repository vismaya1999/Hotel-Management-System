from django.urls import path

from hostelapp import views, admin_views, student_views, parent_views

urlpatterns = [
    path('',views.mainpage,name='mainpage'),

    path('logout_view',views.logout_view,name='logout_view'),

    path('loginpage',views.loginpage,name='loginpage'),

    path('register',views.register,name='register'),

    path('adminpage',views.adminpage,name='adminpage'),

    path('student',views.student,name='student'),

    path('parent',views.parent,name='parent'),

    path('stud_reg',views.stud_reg,name='stud_reg'),
    path('parent_reg',views.parent_reg,name='parent_reg'),

    path('stud_viewf',admin_views.stud_viewf,name='stud_viewf'),
    path('parent_viewf',admin_views.parent_viewf,name='parent_viewf'),

    path('approval_student/<int:id>/',admin_views.approval_student,name='approval_student'),
    path('reject_student/<int:id>/',admin_views.reject_student,name='reject_student'),

    path('approval_parent/<int:id>/',admin_views.approval_parent, name='approval_parent'),
    path('reject_parent/<int:id>/',admin_views.reject_parent, name='reject_parent'),

    path('add_hostel',admin_views.add_hostel, name='add_hostel'),
    path('view_hostel',admin_views.view_hostel, name='view_hostel'),
    path('update_hostel/<int:id>/',admin_views.update_hostel, name='update_hostel'),
    path('delete_hostel/<int:id>/',admin_views.delete_hostel, name='delete_hostel'),

    path('add_food', admin_views.add_food, name='add_food'),
    path('view_food', admin_views.view_food, name='view_food'),
    path('update_food/<int:id>/',admin_views.update_food, name='update_food'),
    path('delete_food/<int:id>/',admin_views.delete_food, name='delete_food'),

    path('add_fee', admin_views.add_fee, name='add_fee'),
    path('view_fee', admin_views.view_fee, name='view_fee'),
    # path('view_payment', admin_views.view_payment, name='view_payment'),
    path('update_fee/<int:id>/',admin_views.update_fee, name='update_fee'),
    path('delete_fee/<int:id>/',admin_views.delete_fee, name='delete_fee'),

    path('view_complaints', admin_views.view_complaints, name='view_complaints'),
    path('reply_complaint/<int:id>/', admin_views.reply_complaint, name='reply_complaint'),

    path('add_notification', admin_views.add_notification, name='add_notification'),
    path('view_notification', admin_views.view_notification, name='view_notification'),
    path('update_notification/<int:id>/',admin_views.update_notification, name='update_notification'),
    path('delete_notification/<int:id>/',admin_views.delete_notification, name='delete_notification'),

    path('add_attendance', admin_views.add_attendance, name='add_attendance'),
    path('view_attendance', admin_views.view_attendance, name='view_attendance'),
    path('update_attendance/<int:id>/',admin_views.update_attendance, name='update_attendance'),
    path('delete_attendance/<int:id>/',admin_views.delete_attendance, name='delete_attendance'),

    path('add_staff', admin_views.add_staff, name='add_staff'),
    path('view_staff', admin_views.view_staff, name='view_staff'),
    path('update_staff/<int:id>/',admin_views.update_staff, name='update_staff'),
    path('delete_staff/<int:id>/',admin_views.delete_staff, name='delete_staff'),

    path('add_room', admin_views.add_room, name='add_room'),
    path('view_room', admin_views.view_room, name='view_room'),
    path('update_room/<int:id>/',admin_views.update_room, name='update_room'),
    path('delete_room/<int:id>/',admin_views.delete_room, name='delete_room'),
    path('approval_booking/<int:id>/', admin_views.approval_booking, name='approval_booking'),
    path('reject_booking/<int:id>/', admin_views.reject_booking, name='reject_booking'),

    path('view_reviews', admin_views.view_reviews, name='view_reviews'),

    path('add_adminpay', admin_views.add_adminpay, name='add_adminpay'),
    path('view_payment', admin_views.view_payment, name='view_payment'),
    path('pay_delete/<int:id>', admin_views.pay_delete, name='pay_delete'),
    path('pay_update/<int:id>', admin_views.pay_update, name='pay_update'),


    # ------------Student--------------
    path('stud_hostel', student_views.stud_hostel, name='stud_hostel'),

    path('stud_food', student_views.stud_food, name='stud_food'),

    path('stud_complaint', student_views.stud_complaint, name='stud_complaint'),
    path('stud_viewcomplaint', student_views.stud_viewcomplaint, name='stud_viewcomplaint'),

    path('stud_fee', student_views.stud_fee, name='stud_fee'),

    path('stud_attendance', student_views.stud_attendance, name='stud_attendance'),

    path('stud_room', student_views.stud_room, name='stud_room'),
    path('stud_viewroom', student_views.stud_viewroom, name='stud_viewroom'),
    path('approval_booking/<int:id>/', student_views.approval_booking, name='approval_booking'),
    path('reject_booking/<int:id>/', student_views.reject_booking, name='reject_booking'),

    path('stud_profile', student_views.stud_profile, name='stud_profile'),

    path('update_profile', student_views.update_profile, name='update_profile'),

    path('stud_reviews', student_views.stud_reviews, name='stud_reviews'),

    path('student_delete', student_views.student_delete, name='student_delete'),

    path('view_studpay', student_views.view_studpay, name='view_studpay'),
    path('approve_payment/<int:id>', student_views.approve_payment, name='approve_payment'),
    path('reject_payment/<int:id>', student_views.reject_payment, name='reject_payment'),


    # ----------------Parent-----------------------
    path('parent_hostel', parent_views.parent_hostel, name='parent_hostel'),

    path('parent_attendance', parent_views.parent_attendance, name='parent_attendance'),

    path('parent_room', parent_views.parent_room, name='parent_room'),

    path('parent_staff', parent_views.parent_staff, name='parent_staff'),

    path('parent_delete', parent_views.parent_delete, name='parent_delete'),

    path('parent_view_pay', parent_views.parent_view_pay, name='parent_view_pay'),
]
