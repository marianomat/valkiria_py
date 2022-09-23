from rest_framework import serializers


class AspnetusersSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=100)
    password = serializers.CharField()        
    companyID = serializers.IntegerField()
    applicationID = serializers.IntegerField()

