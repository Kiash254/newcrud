from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from matplotlib.style import context
from .models import Detail
from .forms import Detailform
# Create your views here.


def home(request):
    user=Detail.objects.all()
    data={
        "user":user
    }
    return render (request,"home.html",data)



    #create in Crud

def Create(request):
    form=Detailform()
    if request.method=="POST":
        form=Detailform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("crud:home")
    context={"form":form}
    return render (request ,"create.html",context)

def Detailview(request,id):
   
    user=Detail.objects.get(pk=id)
    context = {
        'user':user
    }
    return render(request, 'detail.html', context)

def Updateview(request,pk):
    user=get_object_or_404(Detail,pk=id)
    form=Detailform(instance=user)
    if request.method=="POST":
        form=Detailform(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('crud:detail',kwargs={'pk',user.id}))

    context={
        'form':form
    }
    return render (request,"create.html",context)

def Deleteview(request,pk):
    user=get_object_or_404(Detail,pk=id)
    if request.method=="POST":
        user.delete()
        return HttpResponseRedirect(reverse('crud:home'))
    context={'user':user}
    return render (request,'delete.html',context)
        

