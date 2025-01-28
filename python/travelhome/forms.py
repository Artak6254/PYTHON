from django import forms
from .models import Booking, Contact


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['place_name', 'guest_num','arrive_date','leave_date']
        




class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email_name', 'email', 'people_num', 'subject', 'message']
