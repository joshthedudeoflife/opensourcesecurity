from django.db import models

# Create your models here.
class Portscanner(models.Model):
	ip_address = models.IPAddressField()
	port_number = models.DecimalField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	email = models.EmailField()
	full_name = models.CharField(max_lenght=120, blank=True, null=True)

	def __unicode__(self):
		return self.email
		#figure out what to run next