from django.shortcuts import render, redirect
from .models import AttackLog

def fake_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        ip = request.META.get('REMOTE_ADDR')
        user_agent = request.META.get('HTTP_USER_AGENT')

        AttackLog.objects.create(
            username=username,
            password=password,
            ip_address=ip,
            user_agent=user_agent
        )

        return redirect('fake_dashboard')  # redirect attacker to fake dashboard

    return render(request, 'honeypot/login.html')


def dashboard(request):
    logs = AttackLog.objects.all().order_by('-timestamp')
    return render(request, 'honeypot/dashboard.html', {'logs': logs})


def fake_dashboard(request):
    return render(request, 'honeypot/fake_dashboard.html')
