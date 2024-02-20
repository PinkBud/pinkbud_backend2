from rest_framework import serializers
from .models import UserPost
from .models import User
from .models import Lawyer
from .models import Therapist
from .models import Ngo
from .models import Opportunity

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','password','email']

class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPost
        fields = ['id','title','description','img']

class LawyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lawyer
        fields = ['name','email','description','img','certificate','password']

class TherapistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Therapist
        fields = ['name','email','description','img','certificate','password']

class NgoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ngo
        fields = ['name', 'email', 'description', 'img', 'certificate', 'password']

class OpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = ['title','contact_no','description','prize','certification','date','ngo']