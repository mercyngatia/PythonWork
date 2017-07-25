from django.shortcuts import render

# Create your views here.
def students(request):
    students = Student.objects.all()
    return render(request,'welcome_students.html',students)
