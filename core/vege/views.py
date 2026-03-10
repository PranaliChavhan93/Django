from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .models import *

from django.contrib.auth.models import *

# Create your views here.

def recepies(request):

    if request.method == "POST":    
        
        data=request.POST

        recp_name = data.get('recp_name')
        recp_desc = data.get('recp_desc')
        recp_imag = request.FILES.get('recp_imag')

        # print(recp_name)
        # print(recp_desc)
        # print(recp_imag)

        Receipe.objects.create(
            recp_name = recp_name,
            recp_desc = recp_desc,
            recp_imag = recp_imag,
            )

        return redirect('/recepies/')

    queryset = Receipe.objects.all()

    if request.GET.get('search') :
        queryset = queryset.filter(recp_name__icontains = request.GET.get('search') )


    context = {'recepies' : queryset }
    
    messages.success(request, "Added successfully!")

    return render(request, 'recepies.html', context)


def update_recepie(request, id):
    queryset = Receipe.objects.get(id = id)

    if request.method == "POST":

        data=request.POST

        recp_name = data.get('recp_name')
        recp_desc = data.get('recp_desc')
        recp_imag = request.FILES.get('recp_imag')

        queryset.recp_name = recp_name
        queryset.recp_desc = recp_desc

        if recp_imag :
            queryset.recp_imag = recp_imag

        queryset.save()
        return redirect('/recepies/')

    context={'recepie': queryset}    

    return render(request, 'update_recepie.html', context)


def delete_recepie(request, id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()

    messages.success(request, "Item Deleted successfully!")

    return redirect('/recepies/')


def login_page(request):
    return render(request, 'login.html')


def register(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "Username already taken!")
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name ,
            username = username
        )

        user.set_password(password)
        user.save()

        messages.info(request, "Account Created Successfully !")

        return redirect('/register/')

    return render(request, 'register.html')