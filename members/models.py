from django.db import models

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)
MEMBER_TYPES = (
    ('Normal', 'Normal'),
    ('Honorable', 'Honorable'),
    ('Active', 'Active'),
)


# Create your models here.
class Members(models.Model):
    member_no = models.CharField(max_length=10)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_no = models.CharField(max_length=25)
    date_of_birth = models.DateField.Date
    created_date = models.DateTimeField(auto_now=True)
    member_type = models.CharField(max_length=20,choices=MEMBER_TYPES)
    gender = models.CharField(max_length=10, choices=GENDER)
    id_no = models.CharField(max_length=25)

    def __str__(self):
        return self.first_name
