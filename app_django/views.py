from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request, 'index.html')

def articles_by_year(request, year):
    return render(request,'articles.html', {'year':year})

def get_age(request, name):
    result_person = get_base(name)
    return render(request,'person.html', {'name':result_person['name'], 'age':result_person['age']})

def get_base(name):
    list_name = [
        {'name': 'Fernado', 'age': 20},
        {'name': 'Camil', 'age': 27},
        {'name': 'Fernanda', 'age': 23}
    ]

    for person in list_name:
        if person['name'] == name:
            return person
    return {'age': 0}