from django.db import models
from django.core.validators import MinLengthValidator, EmailValidator
from datetime import date
from django.contrib.auth.models import AbstractUser
from workwave.apps.users.managers import CustomUserManager
from cloudinary.models import CloudinaryField

# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(max_length=100, unique=True, validators=[EmailValidator])
    first_name = models.CharField(max_length=50,validators=[MinLengthValidator(2)])
    last_name = models.CharField(max_length=50,validators=[MinLengthValidator(2)])
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    headline = models.CharField(max_length=255, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    avatar = CloudinaryField(null=True, blank=True)
    banner = CloudinaryField(null=True, blank=True)
    is_active = models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    @property
    def avatar_url(self):
        if self.avatar == None:
            return ("null")
        else:
            return(
                f"https://res.cloudinary.com/dey5v9yb0/{self.avatar}"
            )
        
    @property
    def banner_url(self):
        if self.banner == None:
            return ("null")
        else:
            return(
                f"https://res.cloudinary.com/dey5v9yb0/{self.banner}"
            )
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.email}"

    class Meta:
        ordering = ["date_joined"]
        verbose_name = "User"
        verbose_name_plural = "Users"


class ConnectionRequests(models.Model):
    receiveruserid = models.IntegerField(db_column='receiverUserId')  # Field name made lowercase.
    status = models.TextField()  # This field type is a guess.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    userscustomuserid = models.ForeignKey(CustomUser, models.CASCADE, db_column='usersCustomuserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConnectionRequests'

class TypesOfEmployments(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'types_of_employments'


class TypesOfUbications(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'types_of_ubications'

class Experiences(models.Model):
    job_position = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    ubication = models.CharField(max_length=255, blank=True, null=True)
    sector = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    typesofemploymentid = models.ForeignKey('TypesOfEmployments', models.DO_NOTHING, db_column='typesOfEmploymentId', blank=True, null=True)  # Field name made lowercase.
    typesofubicationid = models.ForeignKey('TypesOfUbications', models.DO_NOTHING, db_column='typesOfUbicationId', blank=True, null=True)  # Field name made lowercase.
    userscustomuserid = models.ForeignKey(CustomUser, models.CASCADE, db_column='usersCustomuserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Experiences'

class Jobs(models.Model):
    job_position = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    description = models.TextField()
    ubication = models.CharField(max_length=255, blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    userscustomuserid = models.ForeignKey(CustomUser, models.CASCADE, db_column='usersCustomuserId', blank=True, null=True)  # Field name made lowercase.
    typesofemploymentid = models.ForeignKey('TypesOfEmployments', models.DO_NOTHING, db_column='typesOfEmploymentId', blank=True, null=True)  # Field name made lowercase.
    typesofubicationid = models.ForeignKey('TypesOfUbications', models.DO_NOTHING, db_column='typesOfUbicationId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Jobs'


class Posts(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    post_date = models.DateTimeField()
    photo = models.CharField(max_length=255, blank=True, null=True)
    video = models.CharField(max_length=255, blank=True, null=True)
    userscustomuserid = models.ForeignKey(CustomUser, models.CASCADE, db_column='usersCustomuserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Posts'
