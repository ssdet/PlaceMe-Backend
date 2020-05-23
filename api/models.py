from django.db import models
from django.contrib.auth.models import User
import datetime

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	mobile = models.PositiveIntegerField(default=0)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	age = models.PositiveSmallIntegerField(default=0)
	male = 'M'
	female = 'F'
	default = 'NS'
	gender_choices = [
	  (male, 'Male'),
	  (female, 'Female'),
	  (default, 'Not Specified'),
	]

	gender = models.CharField(max_length=2, choices=gender_choices, default = default)
	IsConfirmed = models.BooleanField(default = False)
	def __str__(self):
		return self.IsConfirmed

class Department(models.Model):
	Name = models.CharField(max_length=256, default = 'NULL')
	Description = models.TextField(max_length=256, default = 'NULL')
	ParentSchool = models.CharField(max_length=256, default = 'NULL')
	FoundedDate = models.DateField(default = 'NULL')
	image = models.ImageField(default='defaultdept.png', upload_to='dept_pics')
	def __str__(self):
		return self.Name

class Course(models.Model):
	dept = models.ForeignKey(Department, on_delete=models.CASCADE)
	Name = models.CharField(max_length=256, default = 'NULL')
	def __str__(self):
		return self.Name

class Branch(models.Model):
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	Name = models.CharField(max_length=256, default = 'NULL')
	def __str__(self):
		return self.Name

class Faculty(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	dept = models.ForeignKey(Department, on_delete=models.CASCADE)
	IsTPO = models.BooleanField(default = False)
	IsPI = models.BooleanField(default = False)
	def __str__(self):
		return self.user.username


class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)
	dept = models.ForeignKey(Department,related_name='dept', on_delete=models.CASCADE, blank=False)
	course = models.ForeignKey(Course,related_name='course', on_delete=models.CASCADE, blank=False)
	branch =  models.ForeignKey(Branch,related_name='branch', on_delete=models.CASCADE,blank=False)
	YearOfAdmission = models.PositiveIntegerField(default = 0, blank=False)
	RollNo = models.PositiveIntegerField(default = 0, blank=False)
	EnrollmentNo =  models.PositiveIntegerField(default = 0, blank=False)
	IsSC = models.BooleanField(default = False)

	def __str__(self):
		return self.user.username

class HighSchool(models.Model):
	student = models.OneToOneField(Student,related_name='HighSchool', on_delete=models.CASCADE, blank=True, null=True)
	NameOfSchool = models.CharField(max_length=256, default = 'NULL')
	Board = models.CharField(max_length=256, default = 'NULL')
	Percentage = models.DecimalField(max_digits=4, decimal_places=2)
	YearOfPassing = models.PositiveSmallIntegerField(default = 0)
	def __str__(self):
		return self.Board

class Intermediate(models.Model):
	student = models.OneToOneField(Student,related_name='Intermediate', on_delete=models.CASCADE, blank=True, null=True)
	NameOfSchool = models.CharField(max_length=256, default = 'NULL')
	Board = models.CharField(max_length=256, default = 'NULL')
	Percentage = models.DecimalField(max_digits=4, decimal_places=2)
	YearOfPassing = models.PositiveIntegerField(default = 0)
	def __str__(self):
		return self.Board

class Diploma(models.Model):
	student = models.OneToOneField(Student, related_name='Diploma', on_delete=models.CASCADE, blank=True, null=True)
	NameOfCollege = models.CharField(max_length=256, default = 'NULL')
	branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
	YearOfPassing = models.PositiveIntegerField(default = 0)
	Percentage = models.DecimalField(max_digits=4, decimal_places=2)
	def __str__(self):
		return self.NameOfCollege

class Graduation(models.Model):
	student = models.OneToOneField(Student,related_name='Graduation', on_delete=models.CASCADE, blank=True, null=True)
	NameOfCollege = models.CharField(max_length=256, default = 'NULL')
	Course = models.CharField(max_length=256, default = 'NULL')
	Branch = models.CharField(max_length=256, default = 'NULL')
	YearOfPassing = models.PositiveIntegerField(default = 0)
	Percentage = models.DecimalField(max_digits=4, decimal_places=2)
	def __str__(self):
		return self.Branch


class PostGraduation(models.Model):
	student = models.OneToOneField(Student,related_name='PostGraduation',  on_delete=models.CASCADE, blank=True, null=True)
	NameOfCollege = models.CharField(max_length=256, default = 'NULL')
	Course = models.CharField(max_length=256, default = 'NULL')
	Branch = models.CharField(max_length=256, default = 'NULL')
	YearOfPassing = models.PositiveIntegerField(default = 0)
	Percentage = models.DecimalField(max_digits=4, decimal_places=2)
	def __str__(self):
		return self.Branch

class Project(models.Model):
	student = models.ForeignKey(Student,related_name='Projects', on_delete=models.CASCADE, blank=True, null=True)
	Title = models.CharField(max_length=256, default = 'NULL')
	Description = models.TextField(max_length=256, default = 'NULL')
	def __str__(self):
		return self.Title

class PrevSemesterData(models.Model):
	student = models.ForeignKey( Student,related_name='PrevSemData', on_delete=models.CASCADE, blank=True, null=True)
	PrevSem =  models.PositiveSmallIntegerField(default = 0)
	CGPA =  models.DecimalField(max_digits=3, decimal_places=2)
	def __str__(self):
		return self.student.user.username


class Company(models.Model):
	Name = models.CharField(max_length=256, default= 'NULL')
	Website = models. URLField(default = 'https://online.hnbgu.ac.in')
	Address = models.CharField(max_length=256, default= 'NULL')

	NGO = 'NGO'
	PSU = 'PSU'
	GOVT = 'GOVT'
	PVT = 'PVT'
	Others = 'others'
	c_type_choices = [
	  (NGO, 'Non-Profit Organisation'),
	  (PSU, 'Public Sector Undertakings'),
	  (GOVT, 'Governement'),
	  (PVT, 'Private'),
	  (Others, 'Others')
	]
	CompanyType = models.CharField(max_length=6, choices=c_type_choices, default = 'NULL')
	About = models.TextField(max_length=256, default= 'NULL')
	Image = models.ImageField(default='defaultcompany.png', upload_to='company_pics')


class HR(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
	company = models.OneToOneField(Company,related_name='company', on_delete= models.CASCADE, blank = True, null = True)




class JobNotification(models.Model):
	hr = models.ForeignKey(HR, on_delete= models.CASCADE, blank = True, null = True)
	JobDesignation = models.CharField(max_length=256, default= 'NULL')
	JobDescription = models.CharField(max_length=256, default= 'NULL')
	PlaceOfPosting = models.CharField(max_length=256, default= 'NULL')
	JoiningBy = models.DateField(auto_now=False, auto_now_add=False)
	CTC = models.PositiveIntegerField(default= 0)
	Gross =  models.PositiveIntegerField(default= 0)
	IsBond =  models.BooleanField(default = False)
	IsShortListedFromResume =  models.BooleanField(default = False)
	IsWrittenTest =  models.BooleanField(default = False)
	IsgroupDiscussion =  models.BooleanField(default = False)
	IsInterview = models.BooleanField(default = False)
	IsMedicalTest =  models.BooleanField(default = False)
	NoOfRounds = models.PositiveSmallIntegerField(default = 0)
	MinOffers = models.PositiveSmallIntegerField(default = 0)

	IsConfirmed =  models.BooleanField(default = False)
	LastDateTime = models.DateTimeField(auto_now=False, auto_now_add=False)
	IsDead = models.BooleanField(default = False)

class JNeligibleCourse(models.Model):
	JobNotif = models.ForeignKey(JobNotification, on_delete=models.CASCADE, blank=True, null=True)
	Dept = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
	course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
	Branch = models.ForeignKey(Branch, on_delete=models.CASCADE, blank=True, null=True)

class AppliedJobNotification(models.Model):
	JobNotif = models.ForeignKey(JobNotification, on_delete=models.CASCADE, blank=True, null=True)
	student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)



# from django.db.models.signals import post_save, pre_save
# from django.contrib.auth.models import Group

# def save_post(sender,instance, **kwargs):
# 	if Group.objects.get(name='DEF') == 'DEF':
# 		my_group = Group.objects.get(name='DEF')
# 		my_group.user_set.add(user)
# 	else:
# 		return "error"

# post_save.connect(save_post, sender = User)