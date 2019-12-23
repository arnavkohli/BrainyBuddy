from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm, EditForm

from .models import User

from quiz.models import Quiz

# Create your views here.
def RegisterView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')

    else:
        form = RegisterForm()

    context = {'form' : form}
    return render(request, 'user/register.html', context=context)

def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        if form.is_valid():
            user = authenticate(username=username, password=password)
            if user != None:
                login(request, user)
                return redirect('/home')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})


def PageNotFound(request):
	return render(request, 'user/404.html')

@login_required
def LogoutView(request):
    logout(request)
    return redirect('/login')

@login_required
def HomeView(request):
    context = {}
    if request.user.is_tutor:
        quizzes = Quiz.objects.filter(user_id__exact=request.user.id)
        context['your_quizzes'] = quizzes
    return render(request, 'user/home.html', context)

@login_required
def EditView(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('/404/')
    user_form = EditForm(request.POST or None, instance=user)
    if user_form.is_valid():
        user_form.save()
        # print (user.is_authenticated)
        return redirect('/home/')
    return render(request, 'user/edit.html', {'form' : user_form})


@login_required
def DeleteView(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('/404/')
    user.delete()
    return redirect('/login/')