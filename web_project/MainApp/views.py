from django.shortcuts import render , get_object_or_404 , redirect
from .models import Category , Post , Feedback
from django.conf import settings
from django.contrib.auth.models import Group , User
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate , logout 

# Create your views here.
def home(request , category_slug=None):
    category_page = None
    posts = None
    if category_slug != None :
        category_page = get_object_or_404(Category , slug=category_slug)
        posts = Post.objects.filter(Category=category_page)
    else :
        posts = Post.objects.all()
    
    #paginator = Paginator(posts, 4)
    #try :
    #    page = int(request.GET.get('page, 1'))
    #except :
    #   page = 1
    #try :
    #    posts = paginator.page(page)
    #except (EmptyPage , InvalidPage) :
    #    posts = paginator.page(paginator.num_pages)

    return render(request , 'home.html' , {'Category':category_page , 'posts':posts} )

def details_page (request , category_slug , post_slug) :
    try :
        post = Post.objects.get(Category__slug=category_slug , slug=post_slug)
    except Exception as e :
        raise e 
    if request.method == "POST" and request.user.is_authenticated and request.POST['content'].strip() != '' :

        Feedback.objects.create(post=post , 
                                user=request.user , 
                                content=request.POST['content'])
    feedbacks = Feedback.objects.filter(post=post) 
  
    return render(request , 'detail_page.html' , {'post':post , 'feedbacks' : feedbacks })


#SingUp_View
def sign_up(request) :
    if request.method == "POST" :
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signUp_user = User.objects.get(username=username)
            customer_group = Group.objects.get(name='registered_users')
            customer_group.user_set.add(signUp_user)
            messages.success(request,('your account created suceesfully'))
            return redirect('sign_in')
    else :
        form = SignUpForm()
    return render(request, 'signUp.html' , {'form' : form})


#SingIn_View
def sign_in(request):
    if request.method == "POST" :
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username , password=password)
            #if user exist :
            if user is not None :
                login(request ,user)
                return redirect('home')
            else :
                return redirect('sign_up')
    else :
        form = AuthenticationForm()
    return render(request , 'signIn.html' , {'form': form})

#SignOut_View
def logoutView(request):
    logout(request)
    return redirect('sign_in')

#About_Page
def about(request) :
    return render(request , 'about.html')

#Search_page
def search(request) :
    posts = Post.objects.filter(title__contains=request.GET['title'])
    return render(request, 'home.html' , {'posts':posts})

def contact(request) :
    return render(request , 'contact.html')

