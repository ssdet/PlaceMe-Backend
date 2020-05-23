from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework.response import Response
from api.models import UserProfile

def AllowedUserGroup(allowed_roles=[]):
				def decorator(view_func):
								def wrapper_func(request, *args, **kwargs):

												group = None
												if request.user.groups.exists():

																group = request.user.groups.all()[0].name

												if group in allowed_roles:
																return view_func(request, *args, **kwargs)

												else:
																return Response(data = "Unauthorised API request")
								return wrapper_func
				return decorator

def ApprovedUser(view_func):
				def wrapper_func(request, *args, **kwargs):

												IsConfirmed = UserProfile.objects.filter(user = request.user).values('IsConfirmed')
												IsConfirmed = IsConfirmed[0]["IsConfirmed"]

												if IsConfirmed == True:
																return view_func(request, *args, **kwargs)

												else:
																return Response(data = "Your approval is pending")
				return wrapper_func

				return ApprovedUser


def AlreadyRegistered(view_func):
				def wrapper_func(request, *args, **kwargs):

												
												if request.user.groups.exists():

													return Response(data = "You are already a Registered User. Don't try to outsmart me")
												else:
													return view_func(request, *args, **kwargs)
				return wrapper_func

				return AlreadyRegistered