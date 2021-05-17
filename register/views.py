from django.shortcuts import render,redirect,HttpResponseRedirect
from .forms import UserRegistration
from .models import User 
# Create your views here.
def add_view(request):
    if request.method == 'POST':
        fm = UserRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = UserRegistration()
            return redirect(add_view)
    else:
        fm = UserRegistration()
    emp = User.objects.all()
    return render(request,'register/adduser.html',{'form':fm,'em':emp})

def del_user(request,id):
    if request.method=='POST':
        t = User.objects.get(pk=id)
        t.delete()
    return redirect(add_view)


def update_user(request,id):
    t = User.objects.get(pk=id)
    fm = UserRegistration(request.POST,instance=t)
    if request.method=='POST':
        fm = UserRegistration(request.POST,instance=t)
        if fm.is_valid():
            fm.save()
            return redirect(add_view)
    return render(request,'register/updateuser.html',{'id':id,'form':fm})