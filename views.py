from django.shortcuts import render,redirect
from django.db import models
from django.contrib.auth.models import User
from .models import BUS,ROUTE,Register,Passenger,Bookticket,dum,dum1
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
	return render(request,'hmepage.html')

def loginpage(request):
        return render(request,'lg.html')

@login_required
def adminpage(request):
        return render(request,'adminhp.html')

@login_required
def userpage(request):
        return render(request,'userhmepge.html')
def loginfun(request):
        if request.method=='POST':
                Username=request.POST['name11']
                Password=request.POST['pasd']
                user=authenticate(username=Username,password=Password)
                try:
                      user=authenticate(username=Username,password=Password)
                except:
                        print("err0r")
                try:
                        if user.is_staff:
                                login(request,user)
                                return render(request,'adminhp.html')
                        elif user:
                                login(request,user)
                                return render(request,'userhmepge.html',{'mg':Username})
                except:
                        print("ERR0R")
                global se
                se=Username
                print(se)
                
                return render(request,'userhmepge.html',{'mg':Username})
                
               
                
@login_required       
def Addbus(request):
        if not request.user.is_authenticated:
                return redirect('lg')
        if request.method=='POST':
                a=request.POST['busname']
                b=request.POST['busnum']
                c=request.POST['fcity']
                d=request.POST['tcity']
                e=request.POST['atime']
                f=request.POST['dtime']
                g=request.POST['ttime']
                h=request.POST['dis']
                buslist=BUS(bus_name=a,bus_no=b,from_city=c,to_city=d,arrivaltime=e,departuretime=f,traveltime=g,distance=h)
                buslist.save()
                return render(request,'adminhp.html')
        else:
                return render(request,'addbus.html')
@login_required
def Addroute(request):
        
        if request.method=='POST':
                a=request.POST['bus']
                r=request.POST['rute']
                i=request.POST['dist']
                p=request.POST['price']
                bus1=BUS.objects.filter(id=a).get()
                rutlist=ROUTE(bus=bus1,route=r,distance=i,fare=p)
                rutlist.save()
                return render(request,'adminhp.html')
        else:
                data=BUS.objects.all()
                s={'data':data}
                return render(request,'addrute.html',s)

def viewbus(request):
        d=BUS.objects.all()
        return render(request,'viewbus.html',{'da':d})

@login_required
def Editbus(request,id):
        b=BUS.objects.get(id=id)
        if request.method=='POST':
                bu=request.POST['busname']
                bn=request.POST['busnum']
                fc=request.POST['fcity']
                tc=request.POST['tcity']
                at=request.POST['atime']
                dt=request.POST['dtime']
                tt=request.POST['ttime']
                di=request.POST['dis']
                b.bus_name=bu
                b.bus_no=bn
                b.from_city=fc
                b.to_city=tc
                b.arrivaltime=at
                b.departuretime=dt
                b.traveltime=tt
                b.distance=di
                b.save()
                return render(request,'viewbus.html')
        else:
  
                return render(request,'editb.html',{'b':b})
        

def Deletebus(request,id):
        de=BUS.objects.get(id=id)
        de.delete()
        return render(request,'viewbus.html')
		
def viewroute(request):
        a=ROUTE.objects.all()
        return render(request,'viewroute.html',{'a':a})

@login_required                
def Editroute(request,pid):
        data=ROUTE.objects.get(id=pid)
        if request.method=='POST':
                r=request.POST['rute']
                d=request.POST['dist']
                f=request.POST['price']
                data.route=r
                data.distance=d
                data.fare=f
                data.save()
                return render(request,'viewroute.html')
        else:
                return render(request,'editru.html',{'data':data})
                
def Deleteroute(request,pid):
        ru=ROUTE.objects.get(id=pid)
        ru.delete()
        return render(request,'viewroute.html')

def Reg(request):
        if request.method=='POST':
                f=request.POST['fname']
                l=request.POST['lname']
                ad=request.POST['address']
                e=request.POST['email']
                m=request.POST['mbile']
                g=request.POST['gender']
                da=request.POST['dob']
                u=request.POST['username']
                p=request.POST['password']
                user=User(first_name=f,last_name=l,username=u,password=p,email=e)
                user.save()
                reg=Register(user=user,address=ad,mobile=m,dcb=da,gender=g)
                reg.save()
                return render(request,'lg.html')
        else:
                return render(request,'registerp.html')

def Search_Bus(request):
        
                
        data=ROUTE.objects.all()
        
        dup=dum1.objects.all()
        
        cu=0
        fare3=0
        count=0
        count1=0
        data1=0
        data2=0
        route1=[]
        route=0
        b_no=[]
        b_no1=[]
        bhu=0
        if request.method=='POST':
                f=request.POST["fcity"]
                t=request.POST["tcity"]
                da=request.POST["date"]
                data1=ROUTE.objects.filter(route=f)
                data2=ROUTE.objects.filter(route=t)
                for i in data1:
                        for j in data2:
                                if i.bus.bus_no==j.bus.bus_no:
                                        route1.append(BUS.objects.filter(bus_no=i.bus.bus_no))
                for i in data1:
                        fare1=i.fare
                        count+=1
                        b_no.append(i.bus.bus_no)
                for i in data2:
                        fare2=i.fare
                        count1+=1
                        b_no1.append(i.bus.bus_no)
                fare3=fare2-fare1
                if fare3<5 and fare3>0:
                        fare3=5
                elif fare3<0:
                        fare3=fare3*(-1)
                elif fare3==0:
                        fare3=fare3
                route=f+"to"+t
                
                dum2=dum1(fare=fare3,bus_name="bus2",date3=da)
                dum2.save()
                for i in dup:
                        cu=cu+1
                print(cu) 
        return render(request,'searchbus.html',{"data2":data,"route1":route1,"fare3":fare3,"cu":cu,"route":route,'mg':se})

@login_required
def Book_detail(request,cu,pid,route):
        print(cu)
        
        data=dum1.objects.get(id=cu)
        data2=BUS.objects.get(id=pid)
        user2=User.objects.filter(username=se).get()
        user1=Register.objects.filter(user=user2).get()
        pro=Passenger.objects.filter(user=user1)
        book=Bookticket.objects.filter(user=user1)
        total=0
        print(total)
        passenger=0
        if request.method=="POST":
                f=request.POST["pname"]
                ag=request.POST["page"]
                ge=request.POST["gender"]
                passenger=Passenger(user=user1,bus=data2,route=route,name=f,age=ag,gender=ge,fare=data.fare,date1=data.date3)
                passenger.save()
                print(passenger)
                total=total+data.fare
                print(total)
                global t
                t=total
                
                Bookti=Bookticket(user=user1,route=route,fare=total,passenger=passenger,date2=data.date3)
                Bookti.save()
        
        return render(request,'bookdetails.html',{'mg':se,"data":data,"data2":data2,"pro":pro,"book":book,"route":route,"cu":cu,"pid":pid,'total':total,'passenger':passenger})

def Deletepassenger(request,pid):
        data=Passenger.objects.get(id=pid)
        data.delete()
        '''ase=dum.objects.all()
        coun=7
        for i in ase:
                coun=coun+1'''
        return render(request,'userhmepge.html',{'mg':se})

@login_required
def Carddetails(request,cu,route,pid):
        #print(t)
        data=dum.objects.get(id=cu)
        data2=BUS.objects.get(id=pid)
        user2=User.objects.filter(username=se).get()
        user1=Register.objects.filter(user=user2).get()
        pro=Passenger.objects.filter(user=user1)
        print(pro)
        book=Bookticket.objects.filter(user=user1)
        count=0
        pro1=0
        if request.method=="POST":
                cnu=request.POST['cnum']
                cn=request.POST['cname']
                cvn=request.POST['cvnum']
                en=request.POST['em']
                e=request.POST['ey']
                
        total1=t
        #print(t)
        
        return render(request,'carddetails.html',{'mg':se,'user':user1,'data':data2,'pro':pro,'pro1':pro1,'total':total1,'book':book,'route':route,'cu':cu,'total1':t})

def Mybooking(request):
        user2=User.objects.filter(username=se).get()
        user1=Register.objects.filter(user=user2).get()
        pro=Passenger.objects.filter(user=user1)
        book=Bookticket.objects.filter(user=user1)
        return render(request,'mybooking.html',{'mg':se,'user':user1,'pro':pro,'book':book})

def Deletemybooking(request,pid):
        pr=Passenger.objects.filter(id=pid)
        pr.delete()
        return render(request,'searchbus.html',{'mg':se})

def logoutview(request):		
	logout(request)
	return render(request,'hmepage.html')



                        
                                        
        
