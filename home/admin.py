from django.contrib import admin

# Register your models here.
from .models import Departments,Occations,Booking

admin.site.register(Departments)
admin.site.register(Occations)
class BookingAdmin(admin.ModelAdmin):
    list_display = ( 'id','c_name','c_phone','c_email','occa_name','booking_date','booked_on')
admin.site.register(Booking,BookingAdmin)