from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, fullname, phone, country, city, district, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        user = self.model(
            email=self.normalize_email(email),
            fullname=fullname,
            phone=phone,
            country=country,
            city=city,
            district=district
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('fullname', '')
        extra_fields.setdefault('phone', '')
        extra_fields.setdefault('country', '')
        extra_fields.setdefault('city', '')
        extra_fields.setdefault('district', '')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, **extra_fields)

class CustomUser(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['fullname','email', 'phone', 'country', 'city', 'district']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


