from django.shortcuts import render , redirect
from .models import user,prd

# Create your views here.
def login(request):
    return render(request,'login.html')



def registration(request):
    return render(request,'registration.html')




def home(request):
    data=prd.objects.all()
    for i in data:
        print(i.prd_name)
    return render(request,'home.html',{'data':data})


def login_btn(request):
    print("bbbbbbbbbbbb")
    if request.method=="POST":
        name = request.POST.get('name')
        pas = request.POST.get('password')
        print(name)
        print(pas)
        if user.objects.filter(name=name , password=pas).exists():
            return redirect('home')
        else: 
            return redirect('login')

    return render(request,'login.html')


def register(request):

    if request.method == "POST":
        name = request.POST.get('un')
        password = request.POST.get('pass')  
        email = request.POST.get('em')  
        country = request.POST.get('cn')
        phno =  request.POST.get('ph')
        print(name)
        print(password)
        print(email)
        print(country)
        print(phno)
        user.objects.create(name=name , password=password , email=email , phno= phno, country=country)

    return render(request,'registration.html')


