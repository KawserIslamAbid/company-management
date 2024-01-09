from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.
class CustomUser(AbstractUser):
    USER_TYPE = (
        ('Admin/HR','Admin/HR'),
        ('System Engineer','System Engineer'),
        ('Project Manager','Project Manager'),
        ('Backend Developer','Backend Developer'),
        ('Ui/Ux Designer','Ui/Ux Designer'),
        ('Staff','Staff'),
        ('Finance Officer','Finance Officer'),
    )
    GENDER=(
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others'),
    )
    BLOOD_GROUP=(
        ('A+','A+'),
        ('A-','A-'),
        ('AB+','AB+'),
        ('AB-','AB-'),
        ('B+','B+'),
        ('B-','B-'),
        ('O+','O+'),
        ('O-','O-'),
    )
    phone_number= models.CharField(max_length=15,null=True,blank=True)
    date_of_birth = models.DateField()
    address= models.CharField(max_length=200)
    user_type= models.CharField(choices=USER_TYPE,max_length=30)
    gender= models.CharField(choices=GENDER,max_length=10)
    blood_group= models.CharField(choices=BLOOD_GROUP,max_length=5)
    bio= models.CharField(max_length=300)
    image= models.ImageField(upload_to='profile_pic',null=True)
    
    def __str__(self):
        return self.username 
    
class Admin_Profile(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True, related_name='AdminHR')
    
    def __str__(self):
        return self.username
 
class System_Engineer_Profile(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True, related_name='SystemEngineer')
    
    def __str__(self):
        return self.username   
    
class Project_Manager_Profile(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True, related_name='ProjectManager')
    
    def __str__(self):
        return self.username
    
class Backend_Developer_Profile(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True, related_name='BackendDeveloper')
    
    def __str__(self):
        return self.username
    
class Ui_Ux_Designer_Profile(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True, related_name='Ui_UxDesigner')
    
    def __str__(self):
        return self.username
    
class Staff_Profile(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True, related_name='Staff')
    
    def __str__(self):
        return self.username
    
class Finance_Officer_Profile(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True, related_name='FinanceOfficer')
    
    def __str__(self):
        return self.username