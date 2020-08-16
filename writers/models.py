from django.db import models

# Create your models here.
class WritersJoin(models.Model):
    first_name=models.CharField(max_length=500)
    last_name=models.CharField(max_length=200)
    country=models.CharField(max_length=3)
    phone=models.CharField(max_length=200)
    additional_phone=models.CharField(max_length=200)
    email=models.EmailField()
    password=models.CharField(max_length=200)
    confirm_password=models.CharField(max_length=200)
    first_discipline=models.CharField(max_length=200)
    second_discipline=models.CharField(max_length=200)
    third_discipline=models.CharField(max_length=200)
    fourth_discipline=models.CharField(max_length=200)
    fifth_discipline=models.CharField(max_length=200)
    academic_degree=models.CharField(max_length=200)
    time_zone=models.CharField(max_length=200)
    night_calls=models.BooleanField(default=False)

    def __str__(self):
        return self.first_name


class Document(models.Model):
    description=models.CharField(max_length=255,blank=True)
    document=models.FileField(upload_to='documents/')
    uploaded_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
        