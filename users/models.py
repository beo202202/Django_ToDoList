from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, name, gender, age, introduction, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email = self.normalize_email(email),
            name = name,
            gender = gender,
            age = age,
            introduction = introduction,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, gender, age, introduction, password=None):
        # email과 패스워드만 입력해도 되지 않나?
        user = self.create_user(
            email,
            password = password,
            name = name,
            gender = gender,
            age = age,
            introduction = introduction,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        "이메일",
        max_length=255,
        unique=True,
    )
    name = models.CharField("이름", max_length=50)
    GENDER_CHOICES=(
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    )
    gender = models.CharField("성별", choices=GENDER_CHOICES, max_length=1)
    age = models.PositiveIntegerField("나이")
    introduction = models.TextField("자기 소개", max_length=200, blank=True)
    is_active = models.BooleanField("활성화 여부", default=True)
    is_admin = models.BooleanField("관리자 여부", default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "gender", "age", "introduction"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin