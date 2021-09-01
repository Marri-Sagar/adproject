from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from adagency.forms import adagencyregistrationform, UploadaddForm
from adagency.models import adagencyregistrationmodel, uploadmodel


def adagency(request):
    return render(request,"adagency/adagency.html")

def adagencypage(request):
    return render(request,'adagency/adagencypage.html')


def adagencylogincheck(request):
    if request.method == 'POST':
        usid = request.POST.get('loginid')
        print(usid)
        pswd = request.POST.get('password')
        print(pswd)
        try:
            check = adagencyregistrationmodel.objects.get(loginid=usid, password=pswd)
           # print('usid',usid,'pswd',pswd)
            request.session['userid'] = check.loginid
            status = check.status
            if status == "activated":
                request.session['email'] = check.email
                #auth.login(request, usid)
                return render(request,'adagency/adagencypage.html')
            else:
                messages.success(request, 'user is not activated')
                return render(request,'adagency/adagency.html')

        except Exception as e:
            print('Exception is ', str(e))
            messages.success(request,'Invalid user id and password')
        return render(request,'adagency/adagency.html')

def adagencyregistration(request):
    if request.method == 'POST':
        form = adagencyregistrationform(request.POST)
        if form.is_valid():
            # print("Hai Meghana")
            form.save()
            messages.success(request, 'you are successfully registred')
            return HttpResponseRedirect('adagency')
        else:
            print('Invalid')
    else:
        form = adagencyregistrationform()
    return render(request, "adagency/adagencyregistration.html", {'form': form})

def uploadadds(request):
    if request.method == 'POST':
        form = UploadaddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adagency/uploadadd_list.html')
    else:
        form = UploadaddForm()
    return render(request, 'adagency/uploadadd.html', {'form': form})


def viewadds(request):
    viewadds = uploadmodel.objects.all()
    return render(request,'adagency/viewadds.html',{'adds':viewadds})
