from django.shortcuts import render
from app1.models import Users,Mails
from django.db.models import Q
# Create your views here.

def home(request):
    response=render(request,'app1/home.html')
    return response

def main(request):
    b=request.GET['b']
    if b=="Create account":
        response=render(request,'app1/createacc.html')
    elif b=="Login":
        response=render(request,'app1/login.html')
    elif b=="get all users":
        qs=Users.objects.all()
        response=render(request,'app1/alldata.html',context={'qs':qs})
    elif b=="delete account":
        response=render(request,'app1/delacc.html')
    return response

def createacc(request):
    fn=request.POST['fn']
    ln=request.POST['ln']
    age=request.POST['age']
    gender=request.POST['gender']
    dob=request.POST['dob']
    mail=request.POST['mail']
    pwd=request.POST['pwd']
    try:
        qs=Users.objects.filter(mailid=mail) 
        if len(qs)==0:
            values=Users.objects.create(first_name=fn,last_name=ln,age=age,gender=gender,DOB=dob,mailid=mail,password=pwd)
            values.save()
            msg='Mail Created Go back and Login....'
            response=render(request,'app1/createacc.html',context={'msg':msg})
        else:
            msg='Mail already exists use another One...'
            response=render(request,'app1/createacc.html',context={'errormsg':msg})
    except:
        msg='Error in Creating mail try again'
        response=render(request,'app1/createacc.html',context={'errormsg':msg})
    return response

def login(request):
    mail=request.POST['mail']
    pwd=request.POST['pwd']
    try:
        qs=Users.objects.get(Q(mailid=mail)&Q(password=pwd))
        response=render(request,'app1/userdashboard.html',context={'qs':qs})
        request.session['mail']=mail
    except:
        msg='Invalid Mail or Password'
        response=render(request,'app1/login.html',context={'msg':msg})
    return response

def logout(request):
    if 'mail' in request.session:
        del request.session['mail']
        response=render(request,'app1/home.html')
    else:
        response=render(request,'app1/home.html')
    return response

def compose_temp(request):
    response=render(request,'app1/compose.html')
    return response

def compose(request):
    fr=request.session['mail']
    to=request.POST['to_mail']
    msg=request.POST['message']
    try:
        to_mail=Users.objects.filter(mailid=to)
        if to_mail:
            mailobj=Mails(from_user=fr,content=msg,to_user_id=to)
            mailobj.save()
            msg='Mail sent successfull'
            response=render(request,'app1/compose.html',context={'msg':msg})
        else:
            msg='Mail not found'
            response=render(request,'app1/compose.html',context={'errmsg':msg})
    except:
        msg='Error in sending mail'
        response=render(request,'app1/compose.html',context={'errmsg':msg})
    return response

def inbox(request):
    to=request.session['mail']
    qs=Mails.objects.filter(to_user_id=to).order_by('sent_at')
    response=render(request,'app1/inbox.html',context={'qs':qs})
    return response

def delete(request):
    mail=request.POST['mail']
    pwd=request.POST['pwd']
    try:
        qs=Users.objects.filter(mailid=mail,password=pwd)
        if qs.exists():
            qs.delete()
            msg='User Deleted '
            response=render(request,'app1/delacc.html',context={'msg':msg})
        else:
            msg='User not found'
            response=render(request,'app1/delacc.html',context={'msgmsg':msg})
    except:
        msg='error in deleting...'
        response=render(request,'app1/delacc.html',context={'errmsg':msg})
    return response