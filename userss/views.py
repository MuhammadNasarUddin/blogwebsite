from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Blogs
from django.contrib.auth.decorators import login_required
from django.db.models import Q  # Make sure to import Q

def home(request):
    try:
        query = request.GET.get('search_query')

        if query is not None:
            # If there is a search query, filter the Blogs queryset
            b = Blogs.objects.filter(
                Q(title__icontains=query) |
                Q(author__username__icontains=query) |  # Assuming author is a User model field
                Q(desc__icontains=query)
            ).order_by('-date')
        else:
            # If no search query, retrieve all blogs
            b = Blogs.objects.all().order_by('-date')

            # Set query to an empty string for consistent handling in the template
            query = ""

        return render(request, 'index.html', {'b': b, 'query': query})

    except Exception as e:
        messages.error(request, str(e))
        return redirect('home')


@login_required
def blog(request):
    try:
        if request.method == "POST":
            title = request.POST['title']
            desc = request.POST['desc']
            b = Blogs(title=title, desc=desc, author=request.user)
            b.save()
            return redirect('home')
        return render(request, 'blog.html')

    except Exception as e:
        messages.error(request, str(e))
        return redirect('blog')


def detail(request, title):
    try:
        blog = get_object_or_404(Blogs, title=title)
        return render(request, 'blog_detail.html', {'b': blog})

    except Exception as e:
        messages.error(request, str(e))
        return redirect('home')


@login_required
def user_blog_detail(request):
    try:
        b = Blogs.objects.filter(author=request.user).order_by('-date')
        return render(request, 'user_blog_detail.html', {'b': b})

    except Exception as e:
        messages.error(request, str(e))
        return redirect('home')


@login_required
def user_blog_edit(request, id):
    try:
        blog = Blogs.objects.get(id=id)

        if request.method == "POST":
            title = request.POST['title']
            desc = request.POST['desc']
            blog.title = title
            blog.desc = desc
            blog.save()
            return redirect('user_blog_detail')

        return render(request, 'user_blog_edit.html', {'b': blog})

    except Exception as e:
        messages.error(request, str(e))
        return redirect('user_blog_detail')


@login_required
def user_blog_delete(request, id):
    try:
        blog = Blogs.objects.get(id=id)
        blog.delete()
        return redirect('user_blog_detail')

    except Exception as e:
        messages.error(request, str(e))
        return redirect('user_blog_detail')


def signin(request):
    try:
        success_message = None
        error_message = None

        if request.user.is_authenticated:
            return redirect('home')

        if request.method == "POST":
            username = request.POST['username']
            pass1 = request.POST['pass1']

            user = authenticate(username=username, password=pass1)

            if user is not None:
                login(request, user)
                success_message = "You have been successfully logged in"
                return redirect('home')
            else:
                error_message = "Invalid credentials, please try again"

        return render(request, 'login.html', {'success_message': success_message, 'error_message': error_message})

    except Exception as e:
        messages.error(request, str(e))
        return redirect('signin')


def signup(request):
    try:
        error_message = None

        if request.method == "POST":
            username = request.POST['username']
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']

            if pass1 != pass2:
                raise ValueError("Passwords do not match")

            if User.objects.filter(username=username).exists():
                raise ValueError("Username already exists")

            if User.objects.filter(email=email).exists():
                raise ValueError("Email already exists")

            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()

            messages.success(request, "Your account has been successfully created")
            return redirect('signin')

    except Exception as e:
        error_message = str(e)
        messages.error(request, error_message)

    return render(request, 'register.html', {'error_message': error_message})


def signout(request):
    try:
        if not request.user.is_authenticated:
            return redirect('signin')
        logout(request)
        messages.success(request, "You have been successfully logged out")
        return redirect('home')

    except Exception as e:
        messages.error(request, str(e))
        return redirect('home')
