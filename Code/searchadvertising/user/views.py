import uuid

from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from adagency.models import uploadmodel
from user.forms import registrationform, viewdetailsform
from user.models import registrationmodel, viewdetailsmodel


def user(request):
    return render(request, "user/user.html")

def userpage(request):
    return render(request,'user/userpage.html')


def userlogincheck(request):
    if request.method == 'POST':
        usid = request.POST.get('loginid')
        print(usid)
        pswd = request.POST.get('password')
        print(pswd)
        try:
            check = registrationmodel.objects.get(loginid=usid,password=pswd)
           # print('usid',usid,'pswd',pswd)
            print(check)
            request.session['userid'] = check.loginid
            print(check.loginid)
            request.session['id'] = check.id
            print(check.id)
            status = check.status
            if status == "activated":
                request.session['email'] = check.email
                #auth.login(request, usid)
                return render(request,'user/userpage.html')
            else:
                messages.success(request, 'user is not activated')
                return render(request,'user/user.html')

        except Exception as e:
            print('Exception is ', str(e))
            messages.success(request,'Invalid user id and password')
        return render(request,'user/user.html')

def userregistration(request):
        if request.method == 'POST':
            form = registrationform(request.POST)
            if form.is_valid():
                # print("Hai Meghana")
                form.save()
                #return HttpResponse("succesfully registered")
                return render(request,"user/user.html")
            else:
                print('Invalid form')
        else:
            form = registrationform()
        return render(request, "user/userregistration.html", {'form': form})

def adds(request):
    #print(uuid.uuid1())
    viewadds = uploadmodel.objects.all()
    #print(uuid.viewadds())
    return render(request,'user/userviewadds.html',{'adds':viewadds})

def adds1(request):
    idno=request.session['id']
    print(idno)
    adds=uploadmodel.objects.filter(id=idno)
    print(adds)
    return render(request,"user/userviewadds1.html",{"adds":adds})

"""def viewdetails(request):
    id = request.GET.get('id')
    check = uploadmodel.objects.get(id=id)
    request.session['id'] = check.id
    id = request.session["id"]
    viewadds = uploadmodel.objects.get(id=id)
    return render(request, 'user/viewdetails.html', {'adds': viewadds})"""

def viewdetails(request):
    if request.method == "POST":
        forms = viewdetailsform(request.POST)
        if forms.is_valid():
            forms.save()
            #messages.success(request, 'successfully ')
            return render(request,'user/useresucces.html')
        else:
            print('Invalid Form')
            price = request.POST.get('price')
            brand = request.POST.get('brand')
            property = request.POST.get('property')
            city = request.POST.get('city')
            #file = request.POST.get('file')
            rating = request.POST.get('rating')
            review = request.POST.get('review')
            #data = {'brand': brand, 'price': price, 'property': property, 'city': city, 'file': file, 'rating': rating, 'review': review}
            #print("data",data)
            form = viewdetailsmodel(price=price,brand=brand,property=property,city=city,rating=rating,review=review)
            form.save()
            print("form savved")
            return render(request,'user/userviewadds.html',{'adds':form})
    else:
        if request.method =='GET':
            print("get method taking")
            id = request.GET.get('id')
            print('Image Id  = ',id)
            price = request.GET.get('price')
            brand = request.GET.get('brand')
            property = request.GET.get('property')
            city = request.GET.get('city')
            file = request.GET.get('file')
            #name= request.session['userid']
            #  print("name",name)
            print('Price = ',price,' brand',brand)
            data = uploadmodel.objects.get(id=id)
            #data = {'brand': brand, 'price': price,  'property':property,'city':city, 'file':file}
            print("data image url =",type(data.file))
            data2 = {'brand': data.brand, 'price': data.price,  'property':data.property,'city':data.city}
            viewadds = viewdetailsform(data2)
            #print('Image Localtion Katti ',file)
            #file ='media/'+file
            return render(request, 'user/viewdetails.html', {'adds': viewadds,'image':data.file})


def search(request):
    return render(request, 'user/usersearch.html')

def viewadagency(request):
    viewadds = uploadmodel.objects.all()
    return render(request,'admin/viewadagency.html',{'adds':viewadds})


def usersearchresult(request):
    property = request.GET.get('property')
    print('product is', property, ' and its type ', type(property))
    dict = {}
    check = uploadmodel.objects.filter(property=property)
    print(check)
    object = check.filter(property=property)
    return render(request, 'user/usersearchresult.html', {"object": object})

def frgt(request):
    if request.method == 'POST':
        mail=request.POST.get('e1')
        print(mail)
        qs=registrationmodel.objects.filter(email=mail)
        print(qs)
        sa='<QuerySet []>'
        if qs.exists():
            return render(request, 'user/user1.html')

        else:
            return render(request, 'frgt.html', {"hello": "mail doesn't exist"})
    else:
        return render(request,'frgt.html')


