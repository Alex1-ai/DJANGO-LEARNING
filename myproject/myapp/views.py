from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Feature
# using it to save to our database
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.


def index(request):


    # WHEN WE HAVE NOT CREATED OUR DATABASE AND ADMIN PANEL

    # return HttpResponse('<h1> Hey, Welcome</h1>')
    #name = 'Patrick'
    # context = {
    #     'name': 'Patrick',
    #     'age': 23,
    #     'nationality': 'British',

    # }
    # return render(request, 'index.html', context)
    # feature1 = Feature()
    # feature1.id = 0
    # feature1.name = 'Fast'
    # feature1.is_true = True
    # feature1.details = 'Our service is very quick'
    
    # feature2 = Feature()
    # feature2.id = 2
    # feature2.is_true = True
    # feature2.name = 'Reliable'
    # feature2.details = 'Our service is very Reliable'

    # feature3 = Feature()
    # feature3.id = 3
    # feature3.is_true = True
    # feature3.name = 'Easy to Use'
    # feature3.details = 'Our service is very Easy to Use'

    # feature4 = Feature()
    # feature4.id = 4
    # feature4.is_true=False
    # feature4.name = 'Affordable'
    # feature4.details = 'Our service is very Affordable'

    
    # features = [feature1, feature2, feature3, feature4]
    features = Feature.objects.all()
   
    return render(request, 'index.html', {'features': features})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email  = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')

            else:
                # creating the user
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')

        else:
            messages.info(request, 'Password Not The Same')
            return redirect('register')
    
    else:
        return render(request, 'register.html')


    
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Credentials invalid')
            return redirect('login')
    
    else:
        return render(request,'login.html')




def logout(request):
    # to logout a user
    auth.logout(request)
    return redirect('/')



def post(request,pk):
    return render(request,'post.html', {'pk':pk})



def counter(request):
    # text = request.POST['text']
    # amount_of_words = len(text.split())
    posts=[1,2,3,4,5,'tim', 'tom', 'john']
    return render(request, 'counter.html', {'posts':posts})
