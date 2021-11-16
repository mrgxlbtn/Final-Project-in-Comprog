from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from community_website.settings import EMAIL_HOST_USER
from .forms import ComplaintForm

def home(request):
    form = ComplaintForm()
    submitted = False
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        subject = str(form['subject'].value())
        recepient = str(form['email'].value())
        address = str(form['address'].value())
        form_message = str(form['message'].value())
        message = 'from ' + recepient + '\n' + address +'\n' + form_message
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
        send_mail(
            subject, 
            message, 
            recepient, 
            [EMAIL_HOST_USER], 
            fail_silently = False
            )
    else:
        form = ComplaintForm
        if 'submitted' in request.GET:
            submitted= True

    return render(request, 'home.html', {
        'form': form,
        'submitted': submitted
        })
