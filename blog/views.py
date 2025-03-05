from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required

from django.utils import timezone
from .models import Post,User,Category,Tag,Comment
from django.shortcuts import render, get_object_or_404
from .forms import PostForm , UserSignUpForm  ,UserloginForm , ProfileForm, EditProfileForm
from django.contrib.auth.hashers import make_password
from django. contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse



from .import forms

# Create your views here.


def post_list(request):

    # posts =Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, slug):

    if request.method == "POST":
        reply = request.POST.get('reply',None)
        parent = request.POST.get('comment',None)
        name = request.POST.get('name',None)
        email= request.POST.get('email',None)
        text = request.POST.get('message',None)
        post = get_object_or_404(Post, slug=slug)
        try:
            comment = Comment.objects.filter(id=int(parent)).first()
            # print(comment, "comment>>>>>>>>>>>>")
            Comment.objects.create(text=reply, post=post,parent=comment,name=name)
        except Exception as e:
            Comment.objects.create(name=name,email=email,text=text, post=post)
        return redirect(reverse('post_detail', kwargs={'slug': post.slug}))        
    else:
        post = get_object_or_404(Post, slug=slug)
        comment = Comment.objects.filter(post=post,  parent__isnull= True)
        Categories = Category.objects.all()
        tags = Tag.objects.all()
    # comments = Comment.objects.all()
    # print(post.post_image,"ddddddddddddddddddddddddddddddddddddd")
        return render(request, 'post_detail.html', {'post': post,'comment':comment,'Categories': Categories,'tags': tags,})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:

        form = PostForm(request.POST)

    return render(request, 'post_edit.html', {'form': form})
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})


@csrf_exempt
def signup_page(request):
        form =  UserSignUpForm(request.POST, request.FILES) 
        if request.method == 'POST':

            if form.is_valid():
        
                user = form.save(commit=False)
                user.password = make_password(user.password)
                user.save()

            messages.success(request, 'Account created successfully! You can now log in.')

            return redirect('login_page')
        

        else:
            form =  UserSignUpForm()
                
        return render(request, 'sign_up.html',  context={'form': form})


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username,password, "password>>>>>>>>>>>>>>>>>")
        user = authenticate(username=username, password=password)
        # print(user, "user>>>>>>>>>>>>>>>>>>>>>>>>>")
        if user is not None:   
            # print("----====------")
            login(request,user=user)
            messages.success(request,"You are now logged in as {username}")
            return redirect("post_list")
    form = UserloginForm()
    return render(request, "log_in.html", {"form": form})

@login_required
def logout_page(request):
    logout(request)
    return redirect('post_list')


@login_required
def profile_page(request):
    user = request.user
    image = request.user.image
    # print(image,"wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
    return render(request, 'profile.html',{'user':user, 'image':image})

def edit_profile_page(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile_page')  # Update this line
    else:
        form = ProfileForm()
    return render(request, 'edit_profile.html', {'form': form})

def category_list(request ,slug):
    categories = get_object_or_404(Category,slug=slug)
    # print( categoryy, "hhhhhhhhhhhhhhhhhhhhhhhhhh")
    posts = Post.objects.filter(category=categories)
    context = {'category': categories,'posts':posts}
    return render(request, 'category_list.html',context)

def tag_list(request,slug):
    tags= get_object_or_404(Tag,slug=slug)
    posts = Post.objects.filter(tags=tags)
    context = {'tags':tags,'posts':posts}
    return render(request,'tag_list.html',context)