from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.views.generic import FormView
from contacts.forms import ContactForm
import json

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        sender = form.cleaned_data['sender']
        message = form.cleaned_data['message']
        copy = form.cleaned_data['copy']

        recipients = ['borodaa@gmail.com']
        if copy:
            recipients.append(sender)
        try:
            send_mail(subject, message, 'borodaa@gmail.com', recipients)
        except BadHeaderError:
            return HttpResponse('Invalid header found')
        return render(self.request, 'thanks.html')



