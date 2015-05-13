from django.db import models
from django.conf import settings
from kqlick.models import Group

class GroupUsers(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='groups')
	group = models.ForeignKey(Group, related_name='users')
	is_anonymous = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	updated_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.is_anonymous

	class Meta:
		db_table = 'kqlic_group_users'