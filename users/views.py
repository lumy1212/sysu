from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

from .models import Person
from .forms import PersonForm


def logout_view(request):
    """Log the user out."""
    logout(request)
    return HttpResponseRedirect(reverse('app1:index'))


def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.password = request.POST['password1']
            # Log the user in, and then redirect to home page.
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('app1:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)


@login_required
def myspace(request):
    person = Person.objects.filter(owner=request.user)
    posts = request.user.post_set.order_by('-date_added')
    if len(person) == 0:
        person = Person.objects.create(name=request.user.username,
                                       student_id=16000000, owner=request.user)
        person.name = request.user.username
        person.owner = request.user
        context = {'person':person,'posts':posts}
    else:
        context = {'person':person[0],'posts':posts}

    return render(request, 'users/myspace.html', context)


@login_required
def edit_space(request):
    person = Person.objects.get(owner=request.user)

    if request.method != 'POST':
        form = PersonForm(instance=person)
    else:
        form = PersonForm(instance=person, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:myspace'))
    context = {'username': person.name, 'student_id': person.student_id, 'major':person.major,'grade':person.grade,'email':person.email, 'form': form}
    return render(request, 'users/edit_space.html', context)
