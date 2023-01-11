from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CreateManagerForm, CreateMentorForm, CreateStudentForm
from .models import (
    Academy,
    Manager,
    Mentor,
    Student
)


def index(request):
    if request.user.is_authenticated:
        academys = Academy.objects.all()

        context = {
            'academys': academys
        }

        return render(request, 'main/index.html', context)
    return redirect('account:login')


def academy_view(request, pk):
    academys = Academy.objects.all()

    academy = Academy.objects.get(id=pk)
    manager = Manager.objects.filter(id=pk)
    mentor = Mentor.objects.filter(id=pk)
    student = Student.objects.filter(id=pk)

    managers = Manager.objects.filter(academy=academy)
    mentors = Mentor.objects.filter(academy=academy)
    students = Student.objects.filter(academy=academy)

    context = {
        'academys': academys,
        'managers': managers,
        'mentors': mentors,
        'students': students,
        'manager': manager,
        'mentor': mentor,
        'student': student,

    }

    return render(request, 'main/academy/academy.html', context)


def create_manager_view(request):
    if request.method == 'POST':
        form = CreateManagerForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:index')
        else:
            return HttpResponse('ERROR')
    form = CreateManagerForm
    context = {
        'form': form
    }
    return render(request, 'main/manager/create_manager.html', context)


def update_manager_view(request, pk):
    manager = Manager.objects.get(id=pk)
    if request.method == 'POST':
        form = CreateManagerForm(request.POST, instance=manager)
        if form.is_valid():
            form.save()
            return redirect('main:index')

        return HttpResponse('Invalid data')
    form = CreateManagerForm(instance=manager)

    context = {
        'form': form
    }
    return render(request, 'main/manager/create_manager.html', context)


def delete_manager_view(request, pk):
    manager = Manager.objects.get(id=pk)
    manager.delete()
    return redirect('main:index')


def create_mentor_view(request):
    if request.method == 'POST':
        form = CreateMentorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:index')
        else:
            return HttpResponse('ERROR')
    form = CreateMentorForm
    context = {
        'form': form
    }
    return render(request, 'main/mentor/create_mentor.html', context)


def update_mentor_view(request, pk):
    mentor = Mentor.objects.get(id=pk)
    if request.method == 'POST':
        form = CreateMentorForm(request.POST, instance=mentor)
        if form.is_valid():
            form.save()
            return redirect('main:index')

        return HttpResponse('Invalid data')
    form = CreateMentorForm(instance=mentor)

    context = {
        'form': form
    }
    return render(request, 'main/mentor/create_mentor.html', context)


def delete_mentor_view(request, pk):
    mentor = Mentor.objects.get(id=pk)
    mentor.delete()
    return redirect('main:index')


def create_student_view(request):
    if request.method == 'POST':
        form = CreateStudentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:index')
        else:
            return HttpResponse('ERROR')
    form = CreateStudentForm
    context = {
        'form': form
    }
    return render(request, 'main/student/create_student.html', context)


def update_student_view(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        form = CreateStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('main:index')

        return HttpResponse('Invalid data')
    form = CreateStudentForm(instance=student)

    context = {
        'form': form
    }
    return render(request, 'main/student/create_student.html', context)


def delete_student_view(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect('main:index')
