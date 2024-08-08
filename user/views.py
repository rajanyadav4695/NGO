from django.shortcuts import render
from.models import *
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def index(request):
    sdata=slider.objects.all().order_by('-id')[0:3]
    uedata=upcomingevent.objects.all().order_by('-id')[0:6]
    vdata = volunteer.objects.all().order_by('email')[0:6]
    ddata=donateus.objects.all().order_by('-id')[0:6]
    mydict={"sd":sdata,"uedata":uedata,"vdata":vdata,"ddata":ddata}
    return render(request,'user/index.html',mydict)

def vissionmission(request):
    return render(request,'user/vissionmission.html')

def donate(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        picture=request.FILES['fu']
        city=request.POST.get('city')
        pincode=request.POST.get('pincode')
        amount=request.POST.get('amount')
        address=request.POST.get('address')
        donateus(name=name,picture=picture,mobile=mobile,email=email,city=city,address=address,pincode=pincode,rupees=amount,ddate=datetime.now().date()).save()
        return HttpResponse("<script>alert('Thanks for donating us...');location.href='/user/donate/'</script>")
    return render(request,'user/donate.html')

def contact(request):
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('email')
        c=request.POST.get('mobile')
        d=request.POST.get('msg')
        contactus(name=a,email=b,mobile=c,message=d).save()
        return HttpResponse("<script>alert('Thanks For Contacting With Us....');location.href='/user/contact/'</script>")


    return render(request,'user/contact.html')

def about(request):
    return render(request,'user/about.html')

def login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        pincode = request.POST.get('pincode')
        address = request.POST.get('address')
        occupation = request.POST.get('occupation')

    return render(request,'user/login.html')

def story(request):
    scdata=schange.objects.all().order_by('-id')
    md={"scdata":scdata}
    return render(request,'user/story.html',md)

def ourvolunteers(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')#techpilelko@gmail.com
        mobile=request.POST.get('mobile')
        address=request.POST.get('address')
        cposition=request.POST.get('cposition')
        picture=request.FILES['fu']
        x=volunteer.objects.filter(email=email).count()#
        if x==0:
            volunteer(name=name,email=email,mobile=mobile,city=address,current_position=cposition,picture=picture).save()
            return HttpResponse("<script>alert('You are registered Successfully..');location.href='/user/volunteers/'</script>")

        else:
            return HttpResponse("<script>alert('you are already registered..');location.href='/user/volunteers/'</script>")
    return render(request,'user/volunteers.html')

def events(request):
    data=upcomingevent.objects.all().order_by('-id')
    md={"eventdata":data}

    return render(request,'user/events.html',md)

def help(request):
    if request.method=="POST":
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        picture=request.FILES['fu']
        htype=request.POST.get('helptype')
        message=request.POST.get('message')
        address=request.POST.get('address')
        nhelp(name=name,mobile=mobile,helptype=htype,message=message,address=address,picture=picture,request_date=datetime.now().date()).save()
        return HttpResponse("<script>alert('Your request added successfully..');location.href='/user/help/'</script>")
    return render(request,'user/help.html')

def viewevent(request):
    eid=request.GET.get('ms')
    data=upcomingevent.objects.filter(id=eid)
    md={"data":data}
    return render(request,'user/viewevent.html',md)

def volunteerslist(request):
    vid=request.GET.get('vid')
    did=request.GET.get('did')
    ddata="";
    vdata="";
    if vid is not None:
        vdata=volunteer.objects.filter(email=vid)
    elif did is not None:
        ddata=donateus.objects.filter(id=did)
    else:
        vdata=volunteer.objects.all()
        ddata=donateus.objects.all().order_by('-id')
    md={
        "vdata":vdata,
        "ddata":ddata
    }
    return render(request,'user/volunteerlist.html',md)

def details(request):
    return render(request,'user/details.html')

def poshans(request):
    return render(request,'user/poshan.html')

def breakfast(request):
    return render(request,'user/breakfast.html')

def feedings(request):
    return render(request,'user/feeding.html')

def mothers(request):
    return render(request,'user/mother.html')
