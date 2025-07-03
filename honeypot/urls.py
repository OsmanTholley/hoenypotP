from django.urls import path
from . import views

urlpatterns = [
    # Route for the fake login page (home page)
    path('', views.fake_login, name='login'),

    # Route to the real admin dashboard that shows logged intrusions
    path('dashboard/', views.dashboard, name='dashboard'),

    # Route to the fake dashboard shown to attackers after login
    path('fake-dashboard/', views.fake_dashboard, name='fake_dashboard'),
]
