from django.shortcuts import render,redirect

from .forms import PersonForm
from .models import Person
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/a2/lgv/")
def pview(request):
    form = PersonForm()
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")

    return render(request,"app1/Person.html",{"form":form})
@login_required(login_url="/a2/lov/")
def sview(request):
    obj = Person.objects.all()
    print(obj)
    return render(request,"app1/show.html",{"obj":obj})

def uview(request,pk):
    obj = Person.objects.get(pid=pk)
    form = PersonForm(instance=obj)
    if request.method=="POST":
        form = PersonForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")

    return render(request,"app1/Person.html",{"form":form})


def dview(request,k):
    obj = Person.objects.get(pid=k)
    if request.method=="POST":
        obj.delete()
        return redirect("/a1/sv/")
    return render(request,"app1/success.html",{"obj":obj})

