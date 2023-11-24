from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):

    def _create_user(self, username=None, email=None, 
         password=None, **extra_fields):

        if (not username) and (not email):
            raise ValueError('Должны быть установлены  (username, email)')

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            username=username,
            **extra_fields
        )

        if extra_fields.get('is_superuser'):
            user = self.model(
                username=username,
                email=email,
                **extra_fields
            )
            
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username=username, email=email, password=password, **extra_fields)

    def create_superuser(self, username, password, email, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('status', 'S')

        return self._create_user(
            username=username,
            email=email,
            password=password,
            **extra_fields
        )
