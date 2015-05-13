from django.db import models

class Group(models.Model):
	group_name        = models.CharField(max_length=30)
	is_active         = models.BooleanField(default=True)
	is_private        = models.BooleanField(default=False)
	updated_at        = models.DateTimeField(auto_now=True)
	created_at        = models.DateTimeField(auto_now_add=True)
	group_description = models.TextField()

	def __unicode__():
		return self.group_name

	class Meta:
		db_table = 'kqlic_group'