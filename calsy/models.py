from django.db import models

# Create your models here.
class user_details(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

class details(models.Model):
    # user = models.ForeignKey(user_details, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    PhoneNo = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    # dob = models.CharField(max_length=50)
    linkedin = models.CharField(max_length=100)
    AboutMe = models.CharField(max_length=250)
    EmailId = models.CharField(max_length=100)
    Skills1 = models.CharField(max_length=100)
    Skills2 = models.CharField(max_length=100)
    Skills3 = models.CharField(max_length=100)
    Skills4 = models.CharField(max_length=100)
    Skills5 = models.CharField(max_length=100)
    LanguagesKnown1 = models.CharField(max_length=100)
    LanguagesKnown2 = models.CharField(max_length=100)
    LanguagesKnown3 = models.CharField(max_length=100)
    sslc = models.CharField(max_length=100)
    sslcyear = models.CharField(max_length=100)
    sslcmark = models.CharField(max_length=100)
    hsc = models.CharField(max_length=100)
    hscyear = models.CharField(max_length=100)
    hscmark = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    CollegeName = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    cgpa = models.CharField(max_length=100)
    ProjectTitle1 = models.CharField(max_length=100)
    ProjectTitle2 = models.CharField(max_length=100)
    Interest1=models.CharField(max_length=100,null=True)
    Interest2=models.CharField(max_length=100,null=True)
    Interest3=models.CharField(max_length=100,null=True)
    Interest4=models.CharField(max_length=100,null=True)
    Description1 = models.CharField(max_length=250)
    Description2 = models.CharField(max_length=250)
    AchievementType1 = models.CharField(max_length=100)
    AchievementType2 = models.CharField(max_length=100)
    AchievementType3 = models.CharField(max_length=100)
    created_by = models.ForeignKey(
        user_details, null=True, blank=True, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)

class todo(models.Model):
    task = models.CharField(max_length=30)
    description=models.CharField( max_length=200,blank=True) 
    date = models.CharField(max_length=10)
    
    created_by = models.ForeignKey(
        user_details, null=True, blank=True, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
