from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
class person:
    def __init__(self, username, password):
        self.username = username
        self.password = password


people=[]

def add(request):
    if request.method == 'POST':
     username = request.POST.get('username')
     password = request.POST.get('password')
     new_person=person(username,password)
     people.append(new_person)
     return redirect(reverse('home'))
    
    return render(request,'peopleApp/add.html')


def home(request):
   return render(request,'peopleApp/home.html', {people:'people'})

