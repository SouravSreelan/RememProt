from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render , redirect
from django.core.mail import send_mail

from .forms import ContactsForm

def contacts(request):
    form = ContactsForm()
    if request.method == 'POST':
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            message_name = request.POST['name']
            message_email = request.POST['email']
            message = request.POST['message']

            try:
                send_mail(
                    'Email from VirhostlncR website user:'+' '+message_email,
                    message,
                    message_email,
                    ['rajrrnbt@gmail.com','rexprem@yenepoya.edu.in','nisar.bb91@gmail.com']
                    )

                messages.info(request, 'Thank you for your feedback. We will get back to you ASAP.')
                return redirect('contact')

            except Exception:
                messages.info(request, 'Thank you for your feedback. We will get back to you ASAP.')
                return redirect('contact')


        else:
            messages.error(request, 'please enter valid information')

    context  = {'form': form }
    return render(request, 'contact/contactus.html',context)



