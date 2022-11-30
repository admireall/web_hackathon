from django.db import models

# Create your models here.
class student(models.Model):
    First_Name=models.CharField( max_length=50)
    Last_Name=models.CharField(max_length=50)
    Birthday_Date=models.IntegerField()
    Birthday_Month=models.CharField(max_length=50)
    Birthday_Year=models.IntegerField()
    Gender=models.CharField( max_length=50)
    Mobile_Number=models.IntegerField()
    Email_Id=models.EmailField( max_length=254)
    Roll_no=models.IntegerField()
    Class_Name=models.CharField( max_length=50)
    Section_name=models.CharField( max_length=50)
    Address=models.CharField(max_length=50)
    City=models.CharField(max_length=50)
    Pin_Code=models.IntegerField()
    State=models.CharField(max_length=50)
    
    hobbies=models.CharField( max_length=50)
    sem1=models.IntegerField()
    sem2=models.IntegerField()
    
    dm=models.IntegerField()
    uhv=models.IntegerField()
    bee=models.IntegerField()
    aec=models.IntegerField()
    java=models.IntegerField()
    cvt=models.IntegerField()
    softskills=models.IntegerField()
    sem3=models.IntegerField()
    comments=models.CharField(max_length=50)
    attendance=models.IntegerField()
    def __str__(self):
        return f"The name of the person is {self.First_Name}"
    
    