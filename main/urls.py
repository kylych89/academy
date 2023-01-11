from django.urls import path
from .views import (
    index,
    academy_view,
    create_manager_view,
    update_manager_view,
    delete_manager_view,
    create_mentor_view,
    update_mentor_view,
    delete_mentor_view,
    create_student_view,
    update_student_view,
    delete_student_view

)

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),

    # academy
    path('academy/<int:pk>/', academy_view, name='academy'),

    # managers
    path('create_manager/', create_manager_view, name='create_manager'),
    path('update_manager/<int:pk>/', update_manager_view, name='update_manager'),
    path('delete_manager/<int:pk>/', delete_manager_view, name='delete_manager'),

    # mentors
    path('create_mentor/', create_mentor_view, name='create_mentor'),
    path('update_mentor/<int:pk>/', update_mentor_view, name='update_mentor'),
    path('delete_mentor/<int:pk>/', delete_mentor_view, name='delete_mentor'),

    # students
    path('create_student/', create_student_view, name='create_student'),
    path('update_student/<int:pk>/', update_student_view, name='update_student'),
    path('delete_student/<int:pk>/', delete_student_view, name='delete_student'),

]
