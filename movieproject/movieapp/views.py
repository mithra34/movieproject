from django.http import HttpResponse
from django.shortcuts import render, redirect
from  .models import  movie
from  .forms import movieform

# Create your views here.
def index(request):

    mov=movie.objects.all()
    context={ 'movie_list':mov}

    return render(request,"index.html",context)

def detail(request,movie_id):
    m1=movie.objects.get(id=movie_id)

    return render(request,'detail.html',{'m2':m1})

def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc = request.POST.get('desc')
        year= request.POST.get('year')
        img = request.FILES['img']
        mov=movie(name=name,desc=desc,year=year,img=img)
        mov.save()
    return render(request, 'add_movie.html')
def update(request,id):
    mov=movie.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES,instance=mov)
    if form.is_valid():
        form.save()
        return redirect('/')
    return  render(request,'edit.html',{'form':form,'mov':mov})
def delete(request,id):
    if request.method=="POST":
        mov=movie.objects.get(id=id)
        mov.delete()
        return redirect('/')
    return  render(request,'delete.html')