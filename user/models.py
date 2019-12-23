from django.db import models

from django.contrib.auth.models import (
   	BaseUserManager, AbstractBaseUser
)
class UserManager(BaseUserManager):
	def create_user(self, username, password, active=True, staff=False, admin=False):
		if not username:
			raise ValueError('enter username')
		if not password:
			raise ValueError('enter password')

		user_obj = self.model(
			username=username,
			password=password
		)
		user_obj.active = active
		user_obj.staff = staff
		user_obj.admin = admin
		user_obj.set_password(password)
		user_obj.save(using=self._db)

		return user_obj

	def create_staffuser(self, username, password):
		user = self.create_user(
				username=username, 
				password=password,
				staff=True
			)
		return user
	def create_superuser(self, username, password):
		user = self.create_user(
				username=username,
				password=password,
				staff=True,
				admin=True
			)
		return user
# Create your models here.
class User(AbstractBaseUser):
	username = models.CharField(max_length=255,unique=True)
	active = models.BooleanField(default=True)
	staff = models.BooleanField(default=False) # a admin user; non super-user
	admin = models.BooleanField(default=False) # a superuser
	is_tutor = models.BooleanField(default=False)

	objects = UserManager()
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = [] 

	def get_username(self):
		return self.username

	def has_perm(self, perm, obj=None):
		return True
	def has_module_perms(self, app_label):
		return True
		
	@property
	def is_active(self):
		return self.active
	@property
	def is_staff(self):
		return self.staff
	@property
	def is_admin(self):
		return self.admin
	def __str__(self):
		return self.username