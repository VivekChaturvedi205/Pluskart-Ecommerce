from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, first_name, last_name,email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user=self.model(first_name=first_name, last_name=last_name,email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name,email, password=None):
        user=self.create_user(first_name=first_name, last_name=last_name,email=self.normalize_email(email), password=password)
        user.is_staff=True
        user.is_superadmin=True
        user.is_admin=True
        user.is_active=True
        user.save(using=self._db)
        return user

        

