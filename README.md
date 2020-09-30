# PlaceMe-Backend
PlaceMe is a Placement Portal with Admins, TPOs &amp; the whole 9 yards.
## Documentation
# Database Docs
## User Types
![Database Model](https://user-images.githubusercontent.com/22274195/94577453-3efb3d00-0294-11eb-835f-3e4ca458c51f.png)

So there is a universal user type that django uses. Here we just leveraged it & further created 3 classified user types under this universal user type.

From the default Django user model, we will use the following fields as it is : 
* username
* first_name
* last_name
* email
* password
* groups
* user_permissions
* is_staff
* is_superuser
* last_login
* date_joined 

full list of fields can be found at [django.contrib.auth.models.User](https://docs.djangoproject.com/en/3.1/ref/contrib/auth/#django.contrib.auth.models.User)

### Extending the Django User Model with "User Profile"

We need fields for all the users of our system that are still not available in default django user model. So we got ahead & created a new model called a User Profile. This profile will contain all additional fields we need for our users. Following are the fields : 
* mobile
* image (Profile Picture)
* gender
* date-of-birth

### Further divisions based on user roles

Now after having all redundant fields one level up, we can now divide user roles meaningfully. This system has 3 user types : 
* Student
* faculty
* HR/Representative

#### Student
Student user role has the following fields : 
* dept (Department)
* course
* branch
* year-of-admission
* roll-no
* enrollment-no
* is-sc (is Student Coordinator ? )
* highschool 
* intermediate 
* diploma
* graduation
* post-graduation
* project
* prev-sem-data (Previous semester CGPAs)

### Faculty
Faculty user role has following fields : 
* dept ( Department)
* is-tpo (Is Training & Placement Officer ? )
* is-pi ( Is Placement Incharge?)

### HR/Representative
HR/Representative user role has the following fields : 
* company

Remember all these 3 are under django user model & user profile model, so fields like name, email, etc are already present in all of these user roles. 
 

