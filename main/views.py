from django.shortcuts import render
from .models import (
    Academy,
    Manager,
    Mentor,
    Student
)


def index(request):
    academys = Academy.objects.all()

    context = {
        'academys': academys
    }

    return render(request, 'main/index.html', context)


def academy(request, pk):
    academys = Academy.objects.all()

    academy = Academy.objects.get(id=pk)
    mentor = Mentor.objects.get(id=pk)
    manager = Manager.objects.get(id=pk)

    managers = Manager.objects.filter(academy=academy)
    mentors = Mentor.objects.filter(academy=academy)
    students = Student.objects.filter(mentor=mentor, manager=manager)

    context = {
        'academys': academys,
        'managers': managers,
        'mentors': mentors,
        'students': students,
    }

    return render(request, 'main/academy.html', context)


def mentor(request, pk):
    managers = Manager.objects.all()

    mentor = Mentor.objects.get(id=pk)
    manager = Manager.objects.get(id=pk)

    students = Student.objects.filter(mentor=mentor, manager=manager)

    context = {
        'managers': managers,
        'students': students,
    }

    return render(request, 'main/mentor.html', context)
