from random import randint
import mysql.connector
import pandas as pd

from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from adagency.models import adagencyregistrationmodel
from user.models import registrationmodel

from numpy import loadtxt
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def index(request):
    return render(request,"index.html")

def adminhome(request):
    return render(request,'admin/adminhome.html')

def adminlogin(request):
    return render(request, "admin/adminlogin.html")

def adminloginaction(request):
        if request.method == "POST":
            if request.method == "POST":
                login = request.POST.get('loginid')
                print(login)
                pswd = request.POST.get('password')
                if login == 'admin' and pswd == 'admin':
                    return render(request, 'admin/adminhome.html')
                else:
                    messages.success(request, 'Invalid user id and password')
        # messages.success(request, 'Invalid user id and password')
        return render(request, 'admin/adminlogin.html')

def logout(request):
    return render(request,'index.html')

def userdetails(request):
    userdata = registrationmodel.objects.all()
    return render(request,'admin/viewuserdetails.html', {'object': userdata})

def activateuser(request):
    if request.method=='GET':
        usid = request.GET.get('usid')
        authkey = random_with_N_digits(8)
        status = 'activated'
        print("USID = ",usid,authkey,status)
        registrationmodel.objects.filter(id=usid).update(authkey=authkey , status=status)
        userdata = registrationmodel.objects.all()
        return render(request,'admin/viewuserdetails.html',{'object':userdata})

def adagencydetails(request):
    adagencydata = adagencyregistrationmodel.objects.all()
    return render(request,'admin/viewadagencydetails.html', {'object': adagencydata})

def activateadagency(request):
    if request.method=='GET':
        usid = request.GET.get('usid')
        authkey = random_with_N_digits(8)
        status = 'activated'
        print("USID = ",usid,authkey,status)
        adagencyregistrationmodel.objects.filter(id=usid).update(authkey=authkey , status=status)
        adagencydata = adagencyregistrationmodel.objects.all()
        return render(request,'admin/viewadagencydetails.html',{'object':adagencydata})


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def accuracy(request):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "advertising"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT price,rating FROM user_viewdetailsmodel")
    myresult = mycursor.fetchall()
    dataset = pd.DataFrame(myresult)
    #print("dataset",dataset)
    mycursor.execute("SELECT rating FROM user_viewdetailsmodel")
    myresult1 = mycursor.fetchall()
    dataset1 = pd.DataFrame(myresult1)
    #print ("dataset1",dataset1)

    #dataset = loadtxt('pima-indians-diabetes.csv', delimiter=",")
    print(dataset.shape)
    # split data into X and y
    #X = dataset[:, 0:8]
    #Y = dataset[:, 8]
    X = dataset
    print("X",len(X))
    Y = dataset1
    print("Y", len(Y))
    #print("x",X)
    # split data into train and test sets
    seed = 2
    test_size = 5
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)
    """print("X_train",X_train)
    print(" X_test", X_test)
    print("y_train",y_train)
    print("y_test",y_test)"""
    # fit model no training data
    model = XGBClassifier()
    print('Katti X= ',X_train)
    print('Katti y= ', y_train)

    model.fit(X_train, y_train)
    # make predictions for test data
    y_pred = model.predict(X_test)
    predictions = [round(value) for value in y_pred]
    print("predictions",predictions)
    # evaluate predictions
    accuracy = accuracy_score(y_test, predictions)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    dict = {
            "accuracy" : accuracy* 100.0,
    }
    return render(request,"admin/accuracy.html",dict)
    #return HttpResponse("wait for algoritham process")