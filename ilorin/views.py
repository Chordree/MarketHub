from django.shortcuts import render, redirect, HttpResponse
from .models import Category, Product
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
# Create your views here.


def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('vendor')

    return render(request, 'ilorin/login_register.html', {'page': page})


def logoutUser(request):
    logout(request)
    return redirect('login')  #redirect shop or home custom this that way later on 


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()  # see if other aspects like name and co can be added 

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # see what this commit does 
            user.save()

            if user is not None:
                login(request, user)
                return redirect('vendor')

    context = {'form': form, 'page': page}
    return render(request, 'ilorin/login_register.html', context)


@login_required(login_url='login')
def storeView(request):
    user = request.user
    category = request.GET.get('category')
    if category == None:
        pics = Product.objects.filter(category__user=user)
    else:
        pics = Product.objects.filter(category__name=category, category__user=user)

    categories = Category.objects.filter(user=user)
    context = {'categories': categories, 'products': pics}
    return render(request, 'ilorin/store.html', context)


# @login_required(login_url='login')
def viewProduct(request, pk):
    pic = Product.objects.get(id=pk)
    return render(request, 'ilorin/product.html', {'product': pic})


@login_required(login_url='login')
def addPhoto(request):
    user = request.user

    categories = user.category_set.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')  # this is for a multi part upload of images  
        # the for loop below still works theres just one item to upload, for future design..
        #  where one product can have multiple images 
        price = data['price']
        if price.isdigit():
            price = price
        else:
            price = 3    

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(user=user, name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Product.objects.create(
                category=category,
                description=data['description'],
                image=image,
                price=price
            )

        return redirect('vendor')   # add succes url here then remain there ..instead of redirecting 

    context = {'categories': categories}
    return render(request, 'ilorin/add.html', context)

def shopView(request, name):  # check how to use this name parameter to validate the id 
   
    try:
        vendor = User.objects.get(username= name)
    # try using the.get or 404 method
    # see to handle the exception with the weather app correctly also  
    except User.DoesNotExist:
        return HttpResponse('No such user')
    
    print(vendor) 
    if vendor :
        category = request.GET.get('category')
        if category == None:
            pics = Product.objects.filter(category__user=vendor.id)
        else:
            pics = Product.objects.filter(category__name=category, category__user=vendor.id)

        categories = Category.objects.filter(user=vendor.id)
        context = {'categories': categories, 'products': pics , 'nom':vendor}
        
        return render(request, 'ilorin/shop.html', context)
    # return HttpResponse('this user does not exist')
    return render(request, 'ilorin/shop.html',)


# remeber to delete den admin 
# TOdo : see how to filter based on pk input,
# if username not in the list ..use exception 
# error messages on registration and log in failures 
# clean up and organise new code .. check all functionalties ..host on aws 
# link for user instagram handles and all 
# links for editing and deleting products




# make two versions ..one with s3 and the other neutral
# check the issue with the big AUto field..
# and see if it would work without naking any migrations 

# add adition view similar to gallery but without ..restrictions ..and carousel display
# purchase should lead to a custom page with vendor contact details 
# view to be able to edit product details .. login requred also ..
# make it work perfectly see how to connect it to AWS