from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=20)
	
	def __unicode__(self):
		return u'%s %s' %(self.username, self.password)