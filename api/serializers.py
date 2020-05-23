from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from api.models import *
from django.db import IntegrityError, transaction
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import Group


class UserApprovalSerializer(serializers.ModelSerializer):

	class Meta:
		model = UserProfile
		fields = ['IsConfirmed']

class RegisterUserSerializer(UserCreateSerializer):


	class Meta:
		model = User
		fields = ['first_name','last_name','email','username', 'password']


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = UserProfile
        fields = ['mobile', 'image', 'age', 'gender_choices','user']




# class StudentSerializer(serializers.ModelSerializer):


# 	HighSchool = serializers.SlugRelatedField(
#         read_only=True,
#         slug_field='Percentage'
#      )

# 	Intermediate = serializers.SlugRelatedField(
#         read_only=True,
#         slug_field='Percentage'
#      )

# 	Diploma = serializers.SlugRelatedField(
#         read_only=True,
#         slug_field='Percentage'
#      )

# 	Graduation = serializers.SlugRelatedField(
#         read_only=True,
#         slug_field='Percentage'
#      )

# 	PostGraduation = serializers.SlugRelatedField(
#         read_only=True,
#         slug_field='Percentage'
#      )





# 	class Meta:
# 		model = Student
# 		fields = ['user','dept','course','branch','HighSchool','Diploma','Intermediate','Graduation', 'PostGraduation']



class StudentSerializer(serializers.ModelSerializer):

	# dept = serializers.SlugRelatedField(
	# 	many = False,
	# 	read_only=False,
	# 	slug_field = 'id',
	# 	queryset=Department.objects.all()
	# 	)




	class Meta:
		model = Student
		fields = ['dept','course', 'branch', 'YearOfAdmission','RollNo', 'EnrollmentNo']



class FacultySerializer(serializers.ModelSerializer):


	class Meta:
		model = Faculty
		fields = ['dept']


class HRSerializer(serializers.ModelSerializer):

	class Meta:
		model = HR
		fields = ['company']