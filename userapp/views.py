import csv
import os

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import UpdateView

from .forms import companyform, jobform, candidateform
from .models import Company, Job, Candidate, Category, Gender, Profiles


# Create your views here.
def home(req):
    request = req
    template_name = 'userapp/home.html'
    context = {}
    return render(request, template_name, context)

@login_required()
def company(request):
    if request.method=='POST':
        comp=companyform(request.POST)
        if comp.is_valid():
            comp.save()
        return redirect('/home/vcom/')

    else:
        comp=companyform()
        template_name='userapp/add_comp.html'
        context= {'form':comp}
        return render (request,template_name,context)

class updatecomp(UpdateView):
    model = Company
    fields = '__all__'


def job(request):
    if request.method=='POST':
        job=jobform(request.POST)
        if job.is_valid():
            job.save()
        return redirect('/home/vjob/')
    else:
        job=jobform()
        template_name='userapp/add_job.html'
        context= {'form':job}

        return render (request,template_name,context)

@login_required()
def candidate(request):
    if request.method == 'POST':
        can=candidateform(request.POST)
        if can.is_valid():
            can.save()
        return redirect('/home/vcan')

    else:
        can=candidateform()
        template_name='userapp/add_can.html'
        context= {'form':can}
        return render (request,template_name,context)

@login_required()
def view_company(request):
    all_comp = Company.objects.all()
    template = 'userapp/show_comp.html'
    context = {'company':all_comp}
    return render(request,template,context)

@login_required()
def view_job(request):
    all_job = Job.objects.all()
    template = 'userapp/show_job.html'
    context = {'jobs':all_job}
    return render(request,template,context)

@login_required()
def view_candidate(request):
    all_cand = Candidate.objects.all()
    template = 'userapp/show_cand.html'
    context = {'candidate':all_cand}
    return render(request,template,context)



import csv, io
from django.shortcuts import render
from django.contrib import messages



def profile_upload(request):
    # declaring template
    template = "userapp/upload.html"
    data = Profiles.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be name, email, address,    phone, profile',
        'profiles': data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):

        company = Company.objects.get_or_create(co_name=column[5]),

        _, created = Profiles.objects.update_or_create(
            name=column[0],
            email=column[1],
            address=column[2],
            phone=column[3],
            profile=column[4],
            company=company,
            )
    context = {}
    return render(request, template, context)
