from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
import datetime

def Home(request):
    data2=Add_Car.objects.all()
    da=""
    data1=Categary.objects.all()
    error=False
    if request.method=='POST':
        b=request.POST['brand']
        m=request.POST['carmodel']
        t=request.POST['cartype']
        car = Categary.objects.get(brand=b)
        da=Add_Car.objects.filter(brand=car,carmodel=m,cartype=t)
        error=True

    d={'data':da,'data2':data2,'error':error}
    return render(request, 'user_home.html',d)
def Logout(request):
    if not request.user.is_authenticated:
        return redirect('login')
    logout(request)
    return redirect('home')
def about(request):
    data = 0
    try:
        data=About.objects.get(id=1)
    except:
        pass
    error = False
    if request.method=='POST':
        t=request.POST['title']
        d=request.POST['des']
        i1 = request.FILES['img1']
        i2 = request.FILES['img2']
        if data:
            data.title=t
            data.des = d
            data.img1 = i1
            data.img2 = i2
            data.save()
            error=True
        else:
            About.objects.create(title=t,des=d,img1=i1,img2=i2)
            error=True
    d = {'error':error}
    return render(request,'about.html',d)

def contact_update(request):
    data = 0
    try:
        data=Contact.objects.get(id=1)
    except:
        pass
    error = False
    if request.method=='POST':
        t=request.POST['email']
        d=request.POST['time1']
        i1 = request.POST['contact']
        i2 = request.POST['add']
        if data:
            data.email=t
            data.office_time = d
            data.contact = i1
            data.address = i2
            data.save()
            error=True
        else:
            Contact.objects.create(office_time=d,contact=i1,address=i2,email=t)
            error=True
    d = {'error':error}
    return render(request,'update_contact.html',d)

def view_about(request):
    data=About.objects.get(id=1)
    d={'data':data}
    return render(request,'view_about.html',d)

def Contact1(request):
    data = Contact.objects.get(id=1)
    d = {'data': data}
    return render(request, 'contact.html',d)
def Admin_Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "yes"
                return redirect('admin_home')
            else:
                error = "not"
        except:
            error="not"
    d = {'error': error}
    return render(request,'login.html',d)
def Admin_Home(request):
    if not request.user.is_staff:
        return redirect('login')
    book=Add_Car.objects.all()
    book1=Categary.objects.all()
    book2=Customer.objects.all()
    b=0
    for i in book:
        b+=1
    b1=0
    for i in book1:
        b1+=1
    b2=0
    for i in book2:
        b2+=1

    d={'b':b,'b1':b1,'b2':b2}
    return render(request, 'admin_home.html',d)

def Add_car(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = False
    data=Categary.objects.all()
    if request.method == "POST":
        cn = request.POST['carname']
        t = request.POST['cartype']
        bd = request.POST['bodycover']
        cm = request.POST['carmodel']
        bt = request.POST['bodytype']
        b= request.POST['brand']
        p = request.POST['carprice']
        num = request.POST['carnumber']
        l= request.POST['carlength']
        w = request.POST['carwidth']
        h = request.POST['carheight']
        s= request.POST['seatingcapacity']
        fu = request.POST['fueltype']
        de= request.POST['displacement']
        m = request.POST['maxpower']
        mt= request.POST['maxtorque']
        ml = request.POST['milage']
        tr = request.POST['transmissiontype']
        n= request.POST['noofgear']
        ac= request.POST['aircondition']
        cp= request.POST['carpowerwindow']
        ct= request.POST['carcenterlocking']
        ca= request.POST['carabs']
        ab= request.POST['airbags']
        ft= request.POST['frontype']
        rt= request.POST['reartype']
        cd= request.POST['cardescription']
        fc= request.POST['fuelcapacity']
        bs= request.POST['bootspace']
        fl= request.POST['foglamps']
        e= request.POST['enginedisplay']
        cl= request.POST['centrallocking']
        ld= request.POST['lastupdationdate']
        i1= request.FILES['img1']
        i2= request.FILES['img2']
        i3= request.FILES['img3']
        i4= request.FILES['img4']
        br=Categary.objects.filter(brand=b).first()
        Add_Car.objects.create(brand=br,carname=cn,cartype=t,bodycover=bd,carmodel=cm,bodytype=bt,carprice=p,carnumber=num,carlength=l,carwidth=w,carheight=h,seatingcapacity=s,fueltype=fu,displacement=de,maxpower=m,maxtorque=mt,milage=ml,transmissiontype=tr,noofgear=n,aircondition=ac,carpowerwindow=cp,carcenterlocking=ct,carabs=ca,airbags=ab,frontype=ft,reartype=rt,cardescription=cd,fuelcapacity=fc,bootspace=bs,foglamps=fl,enginedisplay=e,centrallocking=cl,lastupdationdate=ld,img1=i1,img2=i2,img3=i3,img4=i4)
        error = True
    d={'data':data,'error':error}
    return render(request,'add_car.html',d)
def Add_company(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = False
    if request.method=="POST":
        b=request.POST['brand']
        i= request.FILES['image']
        Categary.objects.create(brand=b,image=i)
        error=True
    d ={'error':error}
    return render(request,'add_company.html',d)

def View_Company(request):
     if not request.user.is_authenticated:
        return redirect('login')
     data=Categary.objects.all()
     d={'data':data}
     return render(request,'view_company.html',d)
def View_Car(request):
     if not request.user.is_authenticated:
        return redirect('login')
     data=Add_Car.objects.all()
     d={'data':data}
     return render(request,'view_car.html',d)

def edit_car(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    data=Categary.objects.all()
    error=False
    detail=Add_Car.objects.get(id=pid)
    if request.method == "POST":
        cn = request.POST['carname']
        t = request.POST['cartype']
        bd = request.POST['bodycover']
        cm = request.POST['carmodel']
        bt = request.POST['bodytype']
        b= request.POST['brand']
        p = request.POST['carprice']
        num = request.POST['carnumber']
        l= request.POST['carlength']
        w = request.POST['carwidth']
        h = request.POST['carheight']
        s= request.POST['seatingcapacity']
        fu = request.POST['fueltype']
        de= request.POST['displacement']
        m = request.POST['maxpower']
        mt= request.POST['maxtorque']
        ml = request.POST['milage']
        tr = request.POST['transmissiontype']
        n= request.POST['noofgear']
        ac= request.POST['aircondition']
        cp= request.POST['carpowerwindow']
        ct= request.POST['carcenterlocking']
        ca= request.POST['carabs']
        ab= request.POST['airbags']
        ft= request.POST['frontype']
        rt= request.POST['reartype']
        cd= request.POST['cardescription']
        fc= request.POST['fuelcapacity']
        bs= request.POST['bootspace']
        fl= request.POST['foglamps']
        e= request.POST['enginedisplay']
        cl= request.POST['centrallocking']
        ld= request.POST['lastupdationdate']
        try:
            i1= request.FILES['img1']
            detail.img1=i1
            detail.save()
        except:
            pass
        try:
            i2= request.FILES['img2']
            detail.img2=i2
            detail.save()
        except:
            pass
        try:
            i3= request.FILES['img3']
            detail.img1=i3
            detail.save()
        except:
            pass
        try:
            i4= request.FILES['img4']
            detail.img1=i4
            detail.save()
        except:
            pass
        detail.carname=cn
        detail.cartype=t
        detail.bodycover=bd
        detail.carmodel=cm
        detail.bodytype=bt
        detail.brand.brand=b
        detail.carprice=p
        detail.carnumber=num
        detail.carlength=l
        detail.carwidth=w
        detail.carheight=h
        detail.seatingcapacity=s
        detail.fueltype=fu
        detail.displacement=de
        detail.maxpower=m
        detail.maxtorque=mt
        detail.milage=ml
        detail.transmissiontype=tr
        detail.noofgear=n
        detail.aircondition=ac
        detail.carpowerwindow=cp
        detail.carcenterlocking=ct
        detail.carabs=ca
        detail.airbags=ab
        detail.frontype=ft
        detail.reartype=rt
        detail.cardescription=cd
        detail.fuelcapacity=fc
        detail.bootspace=bs
        detail.enginedisplay=e
        detail.foglamps=fl
        detail.centrallocking=cl
        detail.lastupdationdate=ld
        detail.save()
        error=True
    d={'detail':detail,'data':data,'error':error}
    return render(request,'edit_car.html',d)

def edit_company(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    data=Categary.objects.get(id=pid)
    error=False
    if request.method=="POST":
        b=request.POST['brand']
        try:
            i= request.FILES['image']
            data.image=i
            data.save()
        except:
            pass
        data.brand=b
        data.save()
        error=True
    d={'data':data,'error':error}
    return render(request,'edit_company.html',d)


def car_list(request):
    error=False
    data3=Categary.objects.all()
    data2=Add_Car.objects.all()
    data1=Add_Car.objects.all()
    if request.method=="POST":
        s =request.POST['carname']
        m =request.POST['carmodel']
        f =request.POST['fueltype']
        data = Add_Car.objects.filter(carname=s,carmodel=m,fueltype=f)
        if data:
            data1 = data
            error=True
    d={'data2':data2,'data1':data1,'error':error,'data3':data3,}
    return render(request,'car_list.html',d)

def car_detail(request,pid):
    error = False
    data=Add_Car.objects.get(id=pid)
    rt = datetime.datetime.now()
    rd = datetime.date.today()
    rt1 = str(rt).split(":")
    rt2 = "".join(rt1)
    order_id1 = rt2.split("-")
    order_id2 = "".join(order_id1)
    order_id3 = order_id2.split(" ")
    order_id4 = "".join(order_id3)
    order_id = order_id4.replace("2020","")
    if request.method=="POST":
        n=request.POST['name']
        e=request.POST['email']
        c=request.POST['con']
        m=request.POST['msg']
        user=User.objects.create_user(username=n,email=e)
        customer=Customer.objects.create(user=user,contact=c,msg=m,enquery=order_id,Name=data,enquery_date=rd,remark='null',remark_date='null',status='unseen')
        error = True

    d={'data':data,'error':error}
    return render(request,'car_detail.html',d)
def company_list(request):
    data=Categary.objects.all()
    data2 = Add_Car.objects.all()
    d={'data':data,"data2":data2}
    return render(request,'company_list.html',d)
def company_detail(request,pid):
    data=Categary.objects.get(id=pid)
    data1=Add_Car.objects.filter(brand=data)
    d={'data1':data1,'data':data}
    return render(request,'company_detail.html',d)
def view_enquery(request):
    data=Customer.objects.all()
    d={'data':data}
    return render(request,'view_enquery.html',d)
def enquery_detail(request,pid):
    data=Customer.objects.get(id=pid)
    date=datetime.date.today()
    if request.method=='POST':
        n=request.POST['name']
        e=request.POST['email']
        c=request.POST['con']
        m=request.POST['msg']
        r=request.POST['remark']
        r1=request.POST['enquery_date']
        data.name=n
        data.email=e
        data.contact=c
        data.msg=m
        data.remark=r
        data.enquery_date=r1
        data.status="seen"
        data.remark_date=date
        data.save()
        return redirect('view_enquery')
    d={'data':data}
    return render(request,'enquery_detail.html',d)

def view_seenenquery(request):
    data=Customer.objects.all()
    d={'data':data}
    return render(request,'view_seenenquery.html',d)
def seen_enquery(request,pid):
    data=Customer.objects.get(id=pid)
    d={'data':data}
    return render(request,'seen_enquery.html',d)
def search_enquery(request):
    data=Customer.objects.all()
    error=""
    if request.method=='POST':
        n=request.POST['enquery']
        da=Customer.objects.filter(enquery=n)
        if da:
            data=da
            error=True
    d={'data':data,'error':error}
    return render(request,'search_enquery.html',d)
def delete_company(request,pid):
    data=Categary.objects.get(id=pid)
    data.delete()
    return redirect('view_company')

def delete_car(request,pid):
    data=Add_Car.objects.get(id=pid)
    data.delete()
    return redirect('view_car')
