from rest_framework import serializers
from .models import *

class Employeeserializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'


    def validate(self,data):
        if data['esal'] < 10000:
            raise serializers.ValidationError({'error':'Employee salary must be grater than 10000'})


        if data['ename']:
            for n in data['ename']:
                if n.isdigit():
                    raise serializers.ValidationError({'error':'name cannot be in numeric'})