from django.db import models

# Create your models here.
from django.urls import reverse
from import_export import resources

Category = (
    ('Software','Software'),
    ('Finance','Finance'),
    ('Telecom','Telecom'),
    ('Insurance','Insurance'),
    ('Others','Others'),
)
Profile = (
    ('Java Developer','Java Developer'),
    ('Python Developer','Python Developer'),
    ('Fullstack Developer','Fullstack Developer'),
    ('Software Tester','Software Tester'),
    ('Others','Others'),
)

Gender = (

    ('Male','Male'),
    ('Female','Female'),
)


class Company(models.Model):
    co_name=models.CharField(max_length=20,unique=True)
    co_regno = models.IntegerField(default='020')
    co_city=models.CharField(max_length=20)
    co_category=models.CharField(max_length=20, choices= Category)



    def __str__(self):
        return self.co_name

    def get_absolute_url(self):
        return reverse('view_company',kwargs={'pk':self.pk})

class Job(models.Model):
    job_comp = models.ForeignKey(Company,on_delete=models.CASCADE)
    job_profile=models.CharField(max_length=20, choices=Profile)
    job_city=models.CharField(max_length=20)
    tot_exp=models.IntegerField()

    def __str__(self):
        return self.job_profile



class Candidate(models.Model):
    comp = models.ForeignKey(Company,on_delete=models.CASCADE)
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=20, choices=Gender)
    city = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name



class Profiles(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=150,unique=True)
    profile = models.TextField()
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    def __str__(self):
        return self.name



