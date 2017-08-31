from __future__ import unicode_literals
import re
from django.db import models

class Notes(models.Model):
	title = models.CharField(max_length=255)
	note = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True) 
	updated_at = models.DateTimeField(auto_now = True)
