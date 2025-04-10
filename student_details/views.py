from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Student 
from .forms import StudentForm, SignupForm


# signup view
def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after signup
            return redirect('student_list')  # Redirect after successful signup
    else:
        form = SignupForm()  # ✅ Only create a new form if the request is GET

    return render(request, 'signup.html', {'form': form}) 
# Login_view

def login_view(request):
    form = AuthenticationForm(request, data=request.POST) if request.method == "POST" else AuthenticationForm()

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('student_list')  # Redirect after successful login

    # Always return a response (even if login fails or it's a GET request)
    return render(request, 'login.html', {'form': form})
    
# logout 
def logout_view(request):
    logout(request)
    return redirect('login')

# Student List View
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html' , {'students':students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form':form})

# Update Student View
@login_required
def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'update_student.html', {"form": form})
    
@login_required
def delete_student(request, student_id):
    student = Student.objects.get(id = student_id)
    student.delete()
    return redirect('student_list')


# Create your views here.
