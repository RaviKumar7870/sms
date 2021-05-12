from django.urls import path
from . import views
from . import student_views
urlpatterns = [
    path("", views.hod_dashboard, name='hod_dashboard'),

    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),

    path('add_user/', views.register_user_view, name='register_user'),
    #     path('add_staff/', views.add_staff, name='add_staff'),
    path('test/', views.test_view, name='test-view'),
    path('result/', views.result_view, name='result-view'),
    path('charts/', views.charts_view, name='charts_view'),
    path('login/', views.login_view, name='login_view'),
    path('tables/', views.tables_view, name='tables_view'),
    path('manage_student/', views.manage_student_view, name='manage_student_view'),
    path('manage_staff/', views.manage_staff_view, name='manage_staff_view'),
    path('manage_courses/', views.manage_courses_view, name='manage_courses_view'),
    path('add_course/', views.add_course_view, name='add_course_view'),
    path('manage_subjects/', views.manage_subjects_view,
         name='manage_subjects_view'),
    path('manage_sessions/', views.manage_sessions_view,
         name='manage_sessions_view'),
    path('view_attendance/', views.view_attendance, name='view_attendance'),
    path('staff_feedback/', views.staff_feedback_view, name='staff_feedback_view'),
    path('students_feedback/', views.students_feedback_view,
         name='students_feedback_view'),
    path('staff_leave/', views.staff_leave_view, name='staff_leave_view'),
    path('student_leave/', views.student_leave_view, name='student_leave_view'),
    path('add_student/', views.add_student_view, name='add_student'),
    path('add_staff/', views.add_staff_view, name='add_staff'),
     path('add_subjects/', views.add_subjects_view, name='add_subjects'),
     path('add_session/', views.add_session_view, name='add_session'),
    path('update_student/<str:pk>',
         views.update_student_view, name='update_student'),
    path('update_staff/<str:pk>',
         views.update_staff_view, name='update_staff'),
    path('delete_student/<str:pk>',
         views.delete_student_view, name='delete_student'),
    path('delete_staff/<str:pk>', views.delete_staff_view, name='delete_staff'),
    path('see_detail/<str:pk>', views.see_detail_view, name='see_detail'),
    path('see_detail_staff/<str:pk>',
         views.see_detail_staff_view, name='see_detail_staff'),










#urls for students -----------------------------------------------------------------
#urls for students -----------------------------------------------------------------
     path("student_home", student_views.student_home_view, name='student_home'),
     path("student_view_attendence", student_views.student_view_attendence_view, name='student_view_attendence'),
     path("student_result", student_views.student_result_view, name='student_result'),
     path("student_apply_leave/<str:pk>", student_views.student_apply_leave_view, name='student_apply_leave'),
     path("student_send_feedback", student_views.student_send_feedback_view, name='student_send_feedback'),
]
