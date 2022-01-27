from rest_framework import serializers

class CovidSerializers(serializers.Serializer):
    infectionPercentage = serializers.CharField(max_length=100)

