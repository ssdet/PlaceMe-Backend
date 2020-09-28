from django.shortcuts import render
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets, request
from rest_framework.response import Response
from api.models import *
from api.serializers import *
from api.decorators import *
from django.db.models import Q


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restricted(request,*args, **kwargs):
	return Response(data="Hello to Restricted Area", status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
class UserProfileView(APIView):
	def get(self, request, format = None):
		userprofiles = UserProfile.objects.filter(user = self.request.user) #current user profile
		serializer = UserProfileSerializer(userprofiles, many=True) #json
		return Response(data= serializer.data)

	def post(self, request, format= None):
		user = self.request.user
		params = self.request.data
		serialized = UserProfileSerializer(data= params)
		if serialized.is_valid():
			mobile = serialized.data['mobile']
			image = serialized.data['image']
			age = serialized.data['age']
			gender = serialized.data['gender']

			userProfile = UserProfile.objects.create(
				user = user,
				mobile = mobile,
				image = image,
				age = age,
				gender = gender
				)
			return Response(data = serialized.data)
		else:
			return Response(data="Invalid Data", status = status.HTTP_400_BAD_REQUEST)

@method_decorator(AllowedUserGroup(allowed_roles = ['FAC']), name='list')
@method_decorator(ApprovedUser, name='list')
class StudentViewSet(viewsets.ModelViewSet):
    """
   
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# class AddUserGroupFAC(APIView):
# 	def post(self,request, format= None):
# 		user = self.request.user
# 		params = self.request.query_params
# 		my_group = Group.objects.get(name=params['FAC'])
# 		my_group.user_set.add(user)

@permission_classes([IsAuthenticated])
@method_decorator(AlreadyRegistered, name = 'post')	
class RegisterStudentView(APIView):
	def post(self, request, format = None):
		user = self.request.user
		params = self.request.data
		serialized = StudentSerializer(data = params)
		if serialized.is_valid():
			user = self.request.user
			dept = Department.objects.get(id = serialized.data['dept'])
			course = Course.objects.get(id=serialized.data['course'])
			branch = Branch.objects.get(id=serialized.data['branch'])
   
			student = Student.objects.create(
		    user = user,
		    dept = dept,
		    course = course,
		    branch = branch,
		    YearOfAdmission = serialized.data['YearOfAdmission'],
		    RollNo = serialized.data['RollNo'],
		    EnrollmentNo = serialized.data['EnrollmentNo'],
			)

			my_group = Group.objects.get(name='STUD') 
			my_group.user_set.add(user)

			return Response(data = serialized.data)
		else:
			return Response(data="Invalid Data", status = status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@method_decorator(AlreadyRegistered, name = 'post')		
class RegisterFacultyView(APIView):
	def post(self, request, format = None):
		user = self.request.user
		params = self.request.data
		serialized = FacultySerializer(data = params)
		if serialized.is_valid():
			user = self.request.user
			dept = Department.objects.get(id = serialized.data['dept'])
   
			faculty = Faculty.objects.create(
		    user = user,
		    dept = dept,
			)

			my_group = Group.objects.get(name='FAC') 
			my_group.user_set.add(user)

			return Response(data = serialized.data)
		else:
			return Response(data="Invalid Data", status = status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@method_decorator(AlreadyRegistered, name='post')		
class RegisterHRView(APIView):
	def post(self, request, format = None):
		user = self.request.user
		params = self.request.data
		serialized = HRSerializer(data = params)
		if serialized.is_valid():
			user = self.request.user
			company = Company.objects.get(id = serialized.data['company'])
   
			hr = HR.objects.create(
		    user = user,
		    company = company
			)

			my_group = Group.objects.get(name='HR')
			my_group.user_set.add(user)

			return Response(data = serialized.data)
		else:
			return Response(data="Invalid Data", status = status.HTTP_400_BAD_REQUEST)


class ApproveStudentView(APIView):
	def get(self,request, format = None):
		params = self.request.query_params
		serialized = UserApprovalSerializer(data=params)

		if serialized.is_valid():
			dept = Department.objects.get(id= params['dept'])
			students = Student.objects.filter(Q(dept = dept))





