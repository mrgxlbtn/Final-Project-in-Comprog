from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from community_website.settings import EMAIL_HOST_USER
from .models import Complaint
from .forms import ComplaintForm

def home(request):
    submitted = False
    dataLength = Complaint.objects.count() 
    submitData = Complaint.objects.all()[dataLength - 1]
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        subject = form['subject'].value()
        name = form['name'].value()
        recepient = form['email'].value()
        address = form['address'].value()
        message = form['message'].value()
        admin_message = 'Complainant: ' + name + '\nAddress: ' + address + '\n' + message
        user_message = 'We successfully received your complaint. We will reach you out as soon as possible. Below is the summary of your complaint.\n' + 'Complainant: ' + name + '\nAddress: ' + address + '\n' + message
        send_mail(
            subject, 
            admin_message, 
            EMAIL_HOST_USER, 
            [EMAIL_HOST_USER], 
            fail_silently = False
        )
        send_mail(
            subject, 
            user_message, 
            EMAIL_HOST_USER, 
            [recepient], 
            fail_silently = False
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
        
    else:
        form = ComplaintForm
        if 'submitted' in request.GET:
            submitted= True
    
    return render(request, 'home.html', {
        'form': form,
        'submitted': submitted,
        'submitData': submitData,
    })
