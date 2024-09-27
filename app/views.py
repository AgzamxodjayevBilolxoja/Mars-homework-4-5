from django.shortcuts import render, redirect
from .models import Car, Student, Laptop, Animal, Fruit, Vegetable


def home_page(request):
    return render(request=request, template_name="home_page.html")

def car_page(request):
    car = Car.objects.all()
    context = {
        "cars": car
    }
    return render(request=request, template_name="car/car_page.html", context=context)

def student_page(request):
    student = Student.objects.all()
    context = {
        "students": student
    }
    return render(request=request, template_name="student/student_page.html", context=context)

def laptop_page(request):
    laptop = Laptop.objects.all()
    context = {
        "laptops": laptop
    }
    return render(request=request, template_name="laptop/laptop_page.html", context=context)

def animal_page(request):
    animal = Animal.objects.all()
    context = {
        "animals": animal
    }
    return render(request=request, template_name="animal/animal_page.html", context=context)

def fruit_page(request):
    fruit = Fruit.objects.all()
    context = {
        "fruits": fruit
    }
    return render(request=request, template_name="fruit/fruit_page.html", context=context)

def vegetable_page(request):
    vegetable = Vegetable.objects.all()
    context = {
        "vegetables": vegetable
    }
    return render(request=request, template_name="vegetable/vegetable_page.html", context=context)

def create_car(request):
    if request.method == "POST":
        brand = request.POST.get("brand")
        model = request.POST.get("model")
        year = request.POST.get("year")
        color = request.POST.get("color")
        photo = request.FILES.get("photo")
        Car.objects.create(
            brand=brand,
            model=model,
            year=year,
            color=color,
            photo=photo
        )
        return redirect('car_page')
    return render(request=request, template_name="car/create_car_page.html")


def create_student(request):
    if request.method == "POST":
        surname = request.POST.get("surname")
        name = request.POST.get("name")
        age = request.POST.get("age")
        Student.objects.create(
            surname=surname,
            name=name,
            age=age
        )
        return redirect('student_page')
    return render(request=request, template_name="student/create_student_page.html")

def create_laptop(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        Laptop.objects.create(
            name=name,
            price=price
        )
        return redirect('laptop_page')
    return render(request=request, template_name="laptop/create_laptop_page.html")

def create_animal(request):
    if request.method == "POST":
        name = request.POST.get("name")
        weight = request.POST.get("weight")
        Animal.objects.create(
            name=name,
            weight=weight
        )
        return redirect('animal_page')
    return render(request=request, template_name="animal/create_animal_page.html")

def create_fruit(request):
    if request.method == "POST":
        name = request.POST.get("name")
        color = request.POST.get("color")
        Fruit.objects.create(
            name=name,
            color=color
        )
        return redirect('fruit_page')
    return render(request=request, template_name="fruit/create_fruit_page.html")

def create_vegetable(request):
    if request.method == "POST":
        name = request.POST.get("name")
        color = request.POST.get("color")
        Vegetable.objects.create(
            name=name,
            color=color
        )
        return redirect('vegetable_page')
    return render(request=request, template_name="vegetable/create_vegetable_page.html")