from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.

@login_required
def people_list(request):
    people = Person.objects.all()
    return render(request, 'people_list.html', {'people':people})

@login_required
def person_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('people_list')
    return render(request, 'person_form.html', {'form': form})

@login_required
def person_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('people_list')

    return render(request, 'person_form.html', {'form': form})

@login_required
def person_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('people_list')

    return render(request, 'person_delete.html', {'person': person})