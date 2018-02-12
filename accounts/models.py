from django.db import models
from django.contrib import auth
# Create your model.

class User(auth.models.User, auth.models.PermissionsMixin, models.Model):

    Register_no = models.IntegerField(unique=True)
    school_name = models.CharField(max_length=200, blank=False)
    RAJASTHAN = 'RA'
    HARIYANA = 'HY'
    GUJARAT = 'GUJ'
    MAHARASHTRA = 'MHR'
    UTTRA_PRADESH = 'UP'
    MADHAYA_PRADESH = 'MP'
    HIMACHAL = 'HIM'

    CHOICES_IN_STATES = (
    	(RAJASTHAN , 'Rajasthan'),
    	(HARIYANA ,'Hariyana'),
    	(GUJARAT ,'Gujarat'),
    	(MAHARASHTRA , 'Maharashtra'),
    	(UTTRA_PRADESH , 'Utra Pradesh'),
    	(MADHAYA_PRADESH , 'Madhaya Pradesh'),
    	(HIMACHAL , 'Himachal Pradesh'),
	)

    state = models.CharField(max_length=50,blank=False, choices = CHOICES_IN_STATES, default = 'Rajasthan')
    village = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now =True)

    def __str__(self):
        return "@{}".format(self.username)
