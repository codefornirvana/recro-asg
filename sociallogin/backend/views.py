from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .components.phone_number_form import PhoneNumberForm
from django.shortcuts import redirect, reverse
from .models import CustomUser
from django.contrib.auth import authenticate, login


def signin(request):
    return render(request, 'login.html')


@login_required
def home(request):
    return render(request, 'index.html')


def phone_number_form(request, **kwargs):
    if request.method == 'POST':
        print(' ~~~~~~~~')
        print(kwargs.get('backend'))
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            request.session['phone_number'] = form.cleaned_data['phone_number']
            request.session['password'] = form.cleaned_data['password']
            return redirect(reverse('social:complete', args=(kwargs.get('backend'),)))
    else:
        form = PhoneNumberForm()
    return render(request, 'complete_signup.html', {'form': form})


def get_all_users(request):
    users = CustomUser.objects.all()
    return render(request, 'all_users.html', {'users': users})

def get_user_details(request, **kwargs):
    print(request.user)
    print(' ------ from the view ----- ')
    print(kwargs)
    userid = kwargs.get('id')
    users = CustomUser.objects.filter(id=userid)
    print(users)
    return render(request, 'user_details.html', {'user': users[0] if len(users) > 0 else None})


def search_user(request):
    phone_number = request.GET.get('q')
    print(phone_number)
    users = CustomUser.objects.filter(phonenumber=phone_number)
    return render(request, 'search_user.html', {'users': users})

def set_password(request):
    new_password = request.data.get('new_password')
    request.user.set_password(new_password)
    request.user.save()


def signin_user(request, **kwargs):
    if request.method == 'POST':
        phonenumber = request.POST['phone_number']
        password = request.POST['password']
        user = authenticate(request, username=phonenumber, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
           return "Invalid Credentials"
    else:
        return "Wrong Method"