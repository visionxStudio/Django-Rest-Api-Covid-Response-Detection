from django.contrib.auth.models import User
import json
from django.http import HttpResponse, JsonResponse
from .models import Profile
from django.contrib.auth import login, authenticate, logout


def saveUser(req):
    reqBody = json.loads(req.body)
    username = reqBody['username']
    password = reqBody['password']
    email = reqBody['email']
    phone = reqBody['phone']
    dob = reqBody['dob']
    add = reqBody['address']

    if (User.objects.filter(username=username).exists()):
        return JsonResponse({
            "status": "user_already_exists"
        }, safe=False)

    if (User.objects.filter(email=email).exists()):
        return JsonResponse({
            "status": "email_already_exists"
        }, safe=False)

    try:
        usr = User.objects.create_user(username=username, email=email, password=password)
        pro = Profile(username=usr, Phone_Number=phone, Address=add, DOB=dob)
        pro.save()
        Profile.refresh_from_db(pro)

        return JsonResponse({
            "status": "profile_saved",
        }, safe=False)

    except Exception as e:
        return JsonResponse({
            "status": "something_went_wrong",
            "Error": str(e)
        }, safe=False)


def Login(req):
    reqBody = json.loads(req.body)
    username = reqBody['username']
    password = reqBody['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        login(req, user)
        return JsonResponse({
            "status": "logged_in"
        }, safe=False)

    else:
        return JsonResponse({
            "status": "something_went_wrong"
        }, safe=False)


def getUserInfo(req):
    print(req.body)
    reqBody = json.loads(req.body)
    print(reqBody)
    return JsonResponse({
        "status": "getUserInfo"
    }, safe=False)
