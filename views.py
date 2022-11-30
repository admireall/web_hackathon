from django.shortcuts import render,redirect
from django.urls import reverse
from . import models
from django.contrib.auth import authenticate,login


def details(request):
    all_students=models.student.objects.all()
    con={'all_students':all_students}
    return render(request,'student_app/details.html',context=con)
    """ if request.POST:
        num=request.POST['num']

        all_students=models.student.objects.get(Roll_no=num).all()
        con={'all_students':all_students}
        return render(request,'student_app/details.html',context=con) 
    else:    
        return render(request,'student_app/details.html')
    
"""    
    

def add(request):
    if request.POST:
        First_Name=request.POST['First_Name']
        Last_Name=request.POST['Last_Name']
        Birthday_Date=int(request.POST['Birthday_Date'])
        Birthday_Month=request.POST['Birthday_Month']
        Birthday_Year=int(request.POST['Birthday_Year'])
        Gender=request.POST['Gender']
        Mobile_Number=int(request.POST['Mobile_Number'])
        Email_Id=request.POST['Email_Id']
        Roll_no=int(request.POST['Roll_no'])
        Class_Name=request.POST['Class_Name']
        Section_name=request.POST['Section_name']
        Address=request.POST['Address']
        City=request.POST['City']
        State=request.POST['State']
       
        hobbies=request.POST['hobbies']
        Pin_Code=int(request.POST['Pin_Code'])
        sem1=int(request.POST['sem1'])
        sem2=int(request.POST['sem2'])
        bee=int(request.POST['bee'])
        dm=int(request.POST['dm'])
        uhv=int(request.POST['uhv'])
        aec=int(request.POST['aec'])
        java=int(request.POST['java'])
        cvt=int(request.POST['cvt'])
        softskills=int(request.POST['softskills'])
        sem3=int(request.POST['sem3'])
        attendance=int(request.POST['attendance'])
        comments=request.POST['comments']
        models.student.objects.create(First_Name=First_Name,bee=bee,Last_Name=Last_Name,Birthday_Date=Birthday_Date,Birthday_Month=Birthday_Month,Birthday_Year=Birthday_Year,Gender=Gender,Mobile_Number=Mobile_Number,Email_Id=Email_Id,Roll_no=Roll_no,Class_Name=Class_Name,Section_name=Section_name,Address=Address,City=City,State=State,hobbies=hobbies,Pin_Code=Pin_Code,sem1=sem1,sem2=sem2,dm=dm,uhv=uhv,aec=aec,java=java,cvt=cvt,softskills=softskills,sem3=sem3,attendance=attendance,comments=comments )
        return redirect(reverse('student_app:thankyou'))
    else:
        return render(request,'student_app/add.html')


def address(request):
    return render(request,'student_app/address.html')

def faculty(request):
    return render(request,'student_app/faculty.html')

def thankyou(request):
    return render(request,'student_app/thankyou.html')

def home(request):
    return render(request,'student_app/home.html')

def search(request):
    return render(request,'student_app/search.html')

def login_user(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(reverse('student_app:add'))
        else:
            return render(request,'student_app/login.html')
    else:
        return render(request,'student_app/login.html')


def call(request):
    if request.POST:
        num=request.POST['num']
        try:
            models.student.objects.get(num=num)
            return redirect(reverse('student_app:details'))
        except:
            print("Roll no is not present")
            return redirect(reverse('student_app:call')) 
    else:    
        return render(request,'student_app/call.html')



        
   