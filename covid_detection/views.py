import imp
from django.http import HttpResponse, JsonResponse
from .detection_algorithm  import readData, encodeData, removeUnwantedData, calculateInfectionProbability
from .covid_serializers import CovidSerializers

def detectCovidInfectionProb(req): 
    print(req.body)
    covid = readData()
    covid = encodeData(covid)
    covid = removeUnwantedData(covid)
    probability = calculateInfectionProbability(covid=covid, data= [1,1,1,1,1,0,1,1,0,0,1])
    return JsonResponse({
        "message" : "Infection Probability calculated Successfully",
        "payload" : {
            "percentage" : probability,
        }
    }, safe=False)