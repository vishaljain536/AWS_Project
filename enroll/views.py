from django.shortcuts import render,HttpResponseRedirect
from .forms import studentregistration
from .models import user
from django.contrib import messages

# Create your views here
#This function will add item and show new item
def add_show(request):
    if request.method == 'POST':
        fm=studentregistration(request.POST)
        if fm.is_valid():
            nm =fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg=user(name=nm,email=em,password=pw)
            reg.save()
            messages.success(request, 'Submitted Sucessfully.')
            fm = studentregistration()

    else:
        fm=studentregistration()
    stud=user.objects.all()

    return render(request,'enroll/Add_Show.html',{'form':fm,'stud':stud})

#this function delete the data
def delete_data(request,id):
    if request.method == 'POST':
        pi=user.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


#this function for update the data
def update_data(request,id):
    if request.method == 'POST':
        pi=user.objects.get(pk=id)
        fm=studentregistration(request.POST,instance=pi)
        if fm.is_valid():
         fm.save()
         messages.success(request, 'Updated Sucessfully.')
    else:
        pi = user.objects.get(pk=id)
        fm=studentregistration(instance=pi)
    return render(request,'enroll/Update_Student.html',{'form':fm})

