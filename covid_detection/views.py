import imp
from django.http import HttpResponse, JsonResponse
from .detection_algorithm import readData, encodeData, removeUnwantedData, calculateInfectionProbability
from .covid_serializers import CovidSerializers
from django.contrib.auth.models import User
import json
from .models import Profile
from django.contrib.auth import login, authenticate, logout


def detectCovidInfectionProb(req):
    print(req.body)
    covid = readData()
    covid = encodeData(covid)
    covid = removeUnwantedData(covid)
    probability = calculateInfectionProbability(covid=covid, data=[1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1])
    return JsonResponse({
        "message": "Infection Probability calculated Successfully",
        "payload": {
            "percentage": probability,
        }
    }, safe=False)


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
    reqBody = json.loads(req.body)
    return JsonResponse({
        "status": "something_went_wrong"
    }, safe=False)
