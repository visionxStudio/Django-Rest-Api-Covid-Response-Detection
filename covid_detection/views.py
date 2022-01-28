import imp
from django.http import  JsonResponse
from .detection_algorithm  import readData, encodeData, removeUnwantedData, calculateInfectionProbability
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def detectCovidInfectionProb(req): 
    if req.method == 'POST':
        reqBody = json.loads(req.body)
        data = reqBody['data']
        if len(data) == 11 :
            covid = readData()
            covid = encodeData(covid)
            covid = removeUnwantedData(covid)
            probability = calculateInfectionProbability(covid=covid, data= data)
            return JsonResponse({
                "message" : "Infection Probability calculated Successfully",
                "payload" : {
                    "percentage" : probability,
                }
            }, safe=False, status = 200)
        return JsonResponse({
            "message" : "Invalid data",
        }, safe=False, status = 422)
    return JsonResponse({
            "message" : "Method Not Allowed",
        }, safe=False, status = 405)
   