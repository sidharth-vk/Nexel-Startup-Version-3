from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.core.mail import EmailMessage
from django.utils.crypto import get_random_string
# Create your views here.



def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dash_home')
            
        else:
            try:
                user = User.objects.get(username=username)
                
                messages.error(request, 'Invalid password')
            except User.DoesNotExist:
                
                messages.error(request, 'Username not found')

            return render(request, 'auth/login.html', {'username': username})
    else:
        return render(request, 'auth/login.html')
    



def custom_logout_view(request):
    logout(request)
    return redirect('login_view')



def forget_password(request):
    if request.method == 'POST':
        if 'username' in request.POST:
            username = request.POST['username']
            try:
                user = User.objects.get(username=username)
                otp = get_random_string(length=6, allowed_chars='1234567890')
                request.session['otp'] = otp
                request.session['username'] = username
                
                email = EmailMessage(
                    'Your OTP Code',
                    f'Your OTP code is {otp}.',
                    to=[user.email]
                )
                email.send()
                return render(request, 'auth/forget_password.html', {'show_otp': True})
            except User.DoesNotExist:
                messages.error(request, 'Username not found.')
                
        elif 'otp' in request.POST:
            otp = request.POST['otp']
            if otp == request.session.get('otp'):
                return render(request, 'auth/forget_password.html', {'show_password_reset': True})
            else:
                messages.error(request, 'Invalid OTP.')
        
        elif 'new_password' in request.POST:
            new_password = request.POST['new_password']
            confirm_password = request.POST['confirm_password']
            if new_password == confirm_password:
                user = User.objects.get(username=request.session.get('username'))
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password has been reset successfully.')
                return redirect('login_view')  # Redirect to the login page
            else:
                messages.error(request, 'Passwords do not match.')
    
    return render(request, 'auth/forget_password.html')