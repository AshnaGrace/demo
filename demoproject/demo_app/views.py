from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from demo_app.forms import Todoform
from demo_app.models import shop
def hello(request):
    return HttpResponse("hellooo")

def demo(request):
    product=shop.objects.all()
    return render(request,"home.html",{'product':product})

def details(request,book_id):
    product1=shop.objects.get(id=book_id)
    return render(request,'details.html',{'product':product1})

def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc = request.POST.get('desc')
        price = request.POST.get('price')
        img=request.FILES['img']
        s=shop(name=name,desc=desc,img=img,price=price)
        s.save()
        print("product added")
    return render(request,"add.html")

def update(request,id):
    obj=shop.objects.get(id=id)
    form=Todoform(request.POST or None,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"update.html",{'obj':obj,'form':form})

def delete(request,taskid):
    task=shop.objects.get(id=taskid)
    if request.method == "POST":
        task.delete()
        return redirect('/')
    return render(request,'gelete.html',{'taask':task})