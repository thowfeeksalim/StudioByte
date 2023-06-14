from django import forms

from .models import Booking

class DateInput(forms.DateInput):
    input_type ='date'

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'

        widgets = {
            'booking_date':DateInput(),
        }
        labels ={
            'c_name':"Customer Name ",
            'c_phone':"Customer Phone Number ",
            'c_email':"Customer email id ",
            'occa_name':"Ocaation",
            'booking_date':"Booking Date ",
            
        }