from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Buying


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password_2 = request.POST['password2']

        if password_2 == password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Error username is taken")
                print("username is taken")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Error email already exists")
                print("email is taken")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username, email=email, password=password, )
                user.save()
                print('user created successfully')
                return redirect("log")

        else:
            messages.info(request, "passwords do not match")
            print('password does not match')
    else:
        return render(request, 'signup.html')


def homepage(request):
    return render(request, 'index.html')


@login_required
def logoutpage(request):
    auth.logout(request)
    return redirect('home')


def logpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')


@login_required
def about(request):
    return render(request, "about.html")


@login_required
def blog(request):
    return render(request, "blog.html")


@login_required
def property(request):
    return render(request, "property.html")


@login_required
def contact(request):
    return render(request, "contact.html")


@login_required
def testimonial(request):
    return render(request, "testimonial.html")


@login_required
def rent(request):
    return render(request, "rental details.html")

def view_house_purchase(request):
    houses = Buying.objects.all()
    context = {'houses': houses}
    return render(request, 'rental details.html', context)
def buying_det(request):
    if request.method == 'POST':
        esto = request.POST.get('name')
        owner = request.POST.get('Owners name')
        units = request.POST.get('units')

        query = Buying(estate_name=esto, owners_name=owner, units=units)
        query.save()
        messages.success(request, 'Buying success')
        return redirect("view")
    messages.error(request, 'error')
    return render(request, "property.html")

def delete(request, id):
    hos = Buying.objects.get(id=id)
    hos.delete()
    return redirect("view")

def Edit(request, id):
    if request.method == 'POSt':
        est = request.POST.get




