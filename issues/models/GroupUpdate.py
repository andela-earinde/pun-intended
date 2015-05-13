from django.db import models
from django.conf import settings
from kqlick.models import Group

class GroupUpdate(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='group_update')
	group = models.ForeignKey(Group, related_name='user_update')
	post = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'kqlic_group_update'