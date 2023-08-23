from django.shortcuts import render
from . forms import RegistrationForm
from django.shortcuts import redirect, render


def account_register(request):
    # if request.user.is_authenticated:
    #     return redirect('/')

    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.save()
            return redirect('users:login')

    else:
        registerForm = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': registerForm})
