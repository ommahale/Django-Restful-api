from rest_framework import serializers
from .models import Person
class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        # fields=['name','age']
        fields='__all__'
        depth=1
    def validate(self, data):
        special_Chars='!()?,@$*#%^&*()-+=`~_=></\|:;'
        if any(c in special_Chars for c in data['name']):
            raise serializers.ValidationError('name cannot have special charecters')
        if(data['age']<18):
            raise serializers.ValidationError('age should be greater than 18')
        return data