from app.views import home_page, car_page, student_page, laptop_page, animal_page, fruit_page, vegetable_page, \
    create_car, create_student, create_laptop, create_animal, create_fruit, create_vegetable
from django.urls import path

urlpatterns = [
    path("", home_page, name="home_page"),
    path("car/", car_page, name="car_page"),
    path("student/", student_page, name="student_page"),
    path("laptop/", laptop_page, name="laptop_page"),
    path("animal/", animal_page, name="animal_page"),
    path("fruit/", fruit_page, name="fruit_page"),
    path("vegetable/", vegetable_page, name="vegetable_page"),
    path("create-car/", create_car, name="create_car"),
    path("create-student/", create_student, name="create_student"),
    path("create-laptop/", create_laptop, name="create_laptop"),
    path("create-animal/", create_animal, name="create_animal"),
    path("create-fruit/", create_fruit, name="create_fruit"),
    path("create-vegetable/", create_vegetable, name="create_vegetable")

]