from django.db import models


# Create your models here.
class Departments(models.Model):
    dep_name= models.CharField( max_length=100)
    dep_description=models.TextField()

    def __str__(self):
       return self.dep_name

class Occations(models.Model):
    occa_name= models.CharField( max_length=255)
    # occ_spec=models.CharField(max_length=255)
    occ_name=models.ForeignKey(Departments, on_delete=models.CASCADE)
    occ_image= models.ImageField(upload_to="occations")
    
    # def __str__(self):
    #     return self.occa_name+ ' - (' + self.occ_spec + ')'


class Booking(models.Model):
    c_name = models.CharField(max_length=255)
    c_phone = models.CharField(max_length=10)
    c_email = models.EmailField()
    occa_name = models.ForeignKey(Departments,on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)
    
    
 
  
