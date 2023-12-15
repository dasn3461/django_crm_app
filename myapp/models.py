from django.db import models

DIVISION_CHOICE=( 
    ('Dhaka', 'Dhaka'),             
    ('Sylhet', 'Sylhet'),             
    ('Chattogram', 'Chattogram'),             
    ('Rajshahi', 'Rajshahi'),             
    ('Barishal', 'Barishal'),             
    ('Rangpur', 'Rangpur'),             
    ('Mymensingh', 'Mymensingh'),             
    ('khulna', 'khulna'),             
)

# Create your models here.
class Record(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.PositiveIntegerField()
    city=models.CharField(max_length=100)
    division=models.CharField(choices=DIVISION_CHOICE,max_length=70)
    
    
    