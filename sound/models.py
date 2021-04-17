from django.db import models
from django.db import models
#from datetime import datetime
from datetime import date
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
def check_time(value):
    today=date.today()
    if value < today:
        raise ValidationError(_('Past Date Not Possible'),params={'value': value},)

def check_participants(value):
    value=value.split(",")
    
    if len(value)>10:
        raise ValidationError(
            _('More than 10 elements'),
            params={'value': value},
        )
    for i in value:
        if len(i)>100:
            raise ValidationError(
            _('Length greater than 100'),
            params={'value': value},
        )
class Song(models.Model):
    ID =models.IntegerField(primary_key=True,null=False)
    Name= models.CharField(max_length=100,null=False)
    Duration=models.PositiveIntegerField(null=False)
    Uploaded=models.DateField(validators=[check_time])
    def __str__(self):
        return str(self.ID)

class Podcast(models.Model):
    ID =models.IntegerField(primary_key=True,null=False)
    Name= models.CharField(max_length=100,null=False)
    Duration=models.PositiveIntegerField(null=False)
    Uploaded=models.DateField(validators=[check_time]) 
    Participants=models.CharField(max_length=1010,validators=[check_participants])
    def __str__(self):
        return str(self.ID)
class Audiobook(models.Model):
    ID =models.IntegerField(primary_key=True,null=False)
    Title = models.CharField(max_length=100,null=False ) 
    Author= models.CharField(max_length=100,null=False)
    Narrator =  models.CharField(max_length=100,null=False) 
    Duration=models.PositiveIntegerField(null=False)
    Uploaded=models.DateField(validators=[check_time]) 
    def __str__(self):
        return str(self.ID)