from django.contrib import admin
from .models import UserProfile, Department, Course, Branch, Faculty, Student, HighSchool, Intermediate, Diploma, Graduation, PostGraduation, Project, PrevSemesterData, HR, Company, JobNotification, JNeligibleCourse, AppliedJobNotification

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Branch)
admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(HighSchool)
admin.site.register(Intermediate)
admin.site.register(Diploma)
admin.site.register(Graduation)
admin.site.register(PostGraduation)
admin.site.register(Project)
admin.site.register(PrevSemesterData)
admin.site.register(HR)
admin.site.register(Company)
admin.site.register(JNeligibleCourse)
admin.site.register(JobNotification)
admin.site.register(AppliedJobNotification)
