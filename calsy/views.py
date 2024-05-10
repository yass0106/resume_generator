from urllib import request
from django.shortcuts import redirect, render
from django.http import JsonResponse
from calsy.models import  *
# from translate import Translator
from django.contrib.auth import logout
import datetime


from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
def calculator(request):
    
    return render(request, 'calculator.html')
a=''
b='b'
c=''
z=1
def register_page(request):
    if  request.method == 'POST':
        name=request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        # a=name
        # b=email/
        # c=password
        user_details.objects.create(name=name,email=email,password=password)
        return redirect('login')
    return render(request,'register.html')

def login_page(request):
    if  request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        if user_details.objects.filter(email=email , password=password):
            a=user_details.objects.filter(password=password).values('name','id')
            # a=user_details.objects.filter(password=password).values()
            print(a,"--------2--------")
            # welcome(a)
            request.session['userid']=a[0]['id']
            print(request.session.get('userid'),"-------3------")
            return redirect('welcome')
            
            # return render(request,'welcome.html',{ 'n':a })
        else:
            return redirect('register')
            # return render(request,'register.html')
    return render(request,'login.html')

# print(a[0])
def homepage(request):

    return render(request,'homepage.html')

def welcome(request):

    return render(request,'index.html')

def form(request):
    print("hai")
    if(request.method == "POST"):
        print("---------------")
        name= request.POST['name']
        PhoneNo= request.POST['PhoneNo']
        address= request.POST['address']
        # dob= request.POST['DOB']
        linkedin= request.POST['linkedin']
        AboutMe= request.POST['AboutMe']
        EmailId= request.POST['EmailId']
        Skills1= request.POST['Skillsone']
        Skills2= request.POST['Skills2']
        Skills3= request.POST['Skills3']
        Skills4= request.POST['Skills4']
        Skills5= request.POST['Skills5']
        LanguagesKnown1= request.POST['LanguagesKnownone']
        LanguagesKnown2= request.POST['LanguagesKnown2']
        LanguagesKnown3= request.POST['LanguagesKnown3']
        Interest1= request.POST['Interest1']
        Interest2= request.POST['Interest2']
        Interest3= request.POST['Interest3']
        Interest4= request.POST['Interest4']
        sslc= request.POST['sslc']
        sslcyear= request.POST['sslcyear']
        sslcmark= request.POST['sslcm']
        hsc= request.POST['hsc']
        hscyear= request.POST['hscyear']
        hscmark= request.POST['hscm']
        degree= request.POST['Degree']
        # degreecourse= request.POST['degreecourse']
        CollegeName= request.POST['CollegeName']
        year= request.POST['year']
        cgpa= request.POST['cgpa']
        ProjectTitle1= request.POST['ProjectTitleone']
        ProjectTitle2= request.POST['ProjectTitle2']
        Description1= request.POST['Descriptionone']
        Description2= request.POST['Description2']
        AchievementType1= request.POST['AchievementTypeone']
        AchievementType2= request.POST['AchievementType2']
        AchievementType3= request.POST['AchievementType3']
        # a=details.objects.latest('id')
        # b=a.id+1
        details.objects.create(name=name, PhoneNo=PhoneNo,
                               address=address,
                               linkedin=linkedin,AboutMe=AboutMe,
                               EmailId=EmailId,Skills1=Skills1,
                                Skills2=Skills2,Skills3=Skills3,
                                Skills4=Skills4,Skills5=Skills5,
                                LanguagesKnown1=LanguagesKnown1,
                                LanguagesKnown2=LanguagesKnown2,
                                LanguagesKnown3=LanguagesKnown3,
                                Interest1=Interest1,
                                Interest3=Interest3,
                                Interest2=Interest2,
                                Interest4=Interest4,
                                sslc=sslc,
                            sslcyear=sslcyear,
                            sslcmark=sslcmark,
                            hsc=hsc,
                            hscyear=hscyear,
                            hscmark=hscmark,
                            degree=degree,
                            CollegeName=CollegeName,
                            year=year,
                            cgpa=cgpa,
                            ProjectTitle1=ProjectTitle1,
                            ProjectTitle2=ProjectTitle2,
                            Description1=Description1,
                            Description2=Description2,
                            AchievementType1=AchievementType1,
                            AchievementType2=AchievementType2,
                            AchievementType3=AchievementType3,
                            created_by_id=request.session.get('userid')

                            )
        # if(request.user.is_authenticated()):
    #     # return HttpResponseRedirect('/profile') 
    # else:
    #     print("error")
    #     t = loader.get_template('index.html')
    #     html = t.render({'form': form})

    return render(request,"homepage.html")

def restemp(request):
    # print(a[0])
    if  request.method=="POST":
        a=details.objects.latest('id')
        print(a.id)
        aa=details.objects.filter(id=a.id,created_by_id=request.session.get('userid')).values()[0]
        # print(aa['name'])
        datass={
            'name':aa['name'], 
             'about':   aa['AboutMe'], 
             'pno':  aa['PhoneNo'], 
             'linkedin':  aa['linkedin'], 
             'address':   aa['address'],
             'email':   aa['EmailId'],
             'skills1':   aa['Skills1'],
             'skills2':   aa['Skills2'],
             'skills3':   aa['Skills3'],
             'skills4':   aa['Skills4'],
             'skills5':   aa['Skills5'],
             'langknown1':aa['LanguagesKnown1'],
             'langknown2':aa['LanguagesKnown2'],
             'langknown3':aa['LanguagesKnown3'],
             'sslc':       aa['sslc'],
             'sslcyear':   aa['sslcyear'],
             'sslcm':      aa['sslcmark'],
             'hsc':        aa['hsc'],
             'hscm':       aa['hscmark'],
             "hscyear":    aa['hscyear'],
             'degree':     aa['degree'],
             "College":aa['CollegeName'],
             "year":     aa['year'],
             "cgpa":     aa['cgpa'],
             "Interest1":aa['Interest1'],
             "Interest3":aa['Interest3'],
             "Interest2":aa['Interest2'],
             "Interest4":aa['Interest4'],
             'projecttitle1':      aa['ProjectTitle1'],
             'projectdescription1':aa['Description1'],
             "ProjectTitle2":      aa['ProjectTitle2'],
             "projectdescription2":aa['Description2'],
             "AchievementType1":aa['AchievementType1'],
             "AchievementType2":aa['AchievementType2'],
             "AchievementType3":aa['AchievementType3'],
        }
        print(datass)
        return JsonResponse(datass, safe=False)
    return render(request,'res_temp.html')

# def login(request):
#     if  request.method == "POST":
#         email = request.POST['email']
#         password = request.POST['password']
#         if  (email=='admin@gmail.com' and password=='123456'):
#             print('33333')
#             return render(request,"form.html")
        
#         else:
#             peinr('222222')
#             # data="error"
#             # return JsonResponse(data, safe=False)
#             return redirect('login/')
#     return render(request, "login.html")
    
def resumeM1(request):

    return render(request,'resumeM1.html')

def resumeM2(request):

    return render(request,'resumeM2.html')


def resumeM3(request):

    return render(request,'resumeM3.html')


def resumeM4(request):

    return render(request,'resumeM4.html')

def todos(request):
    print("---------")
    if request.method=="POST": 
        print("---------")
        check=request.POST['index']
        if check=="":
            task=request.POST["topic"]
            description=request.POST["description"]
            deadline=request.POST["deadline"]
            todo.objects.create(task=task,description=description,date=deadline,created_by_id=request.session.get('userid'))
            a=todo.objects.filter(created_by_id=request.session.get('userid')).values()
            context=[{
                'tasks':data['task'],'desc':data['description'],'dates':data['date']
            }for  data in a
            ]
            # print(context)
            return JsonResponse(context,safe=False)
        elif check=="all":
            print("checked")
            a=todo.objects.filter(created_by_id=request.session.get('userid')).values()
            # print(a)
            context=[{
                'tasks':data['task'],'desc':data['description'],'dates':data['date'],'id':str(data['id'])
            }for  data in a
            ]
            return JsonResponse(context,safe=False)
            
        # time_left=(deadline - now).days
        # t={
        #     'task':task,
        #     'description':description,
        #     'time left':time_left,
        # }
        elif check=='delete':
            deleting_id=int(request.POST['delete'])
            print(type(deleting_id))
            todo.objects.filter(id=deleting_id).delete()
            
    return render(request,"todo.html")

def log_out(request):
    logout(request)
    # return redirect('register')
    return render(request,'login.html')

# def translate(request):  
#     print("-----")
#     if(request.method=='POST'):
#         text = request.POST["text"]
#         language = request.POST["language"]
#         translator= Translator(from_lang="ta", to_lang=language) 
#         translation = translator.translate(text)
#         print(translation)
#         return JsonResponse(translation,safe=False)

#     return render(request,"translator.html")

# def email(request):
#     if request.method == "POST":
#         subject = request.POST['emailss']
#         print(subject)
#         subject = 'welcome to GFG world'
#         message = f'Hi thank you for registering in geeksforgeeks.'
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = [subject, ]
#         send_mail( subject, message, email_from, recipient_list )

#     return render(request,"email.html")