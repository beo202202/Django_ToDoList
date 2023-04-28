from rest_framework import serializers
from users.models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# from django.contrib.auth.password_validation import validate_password
# from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    
    # password = serializers.CharField(
    #     write_only=True,
    #     required=True,
    #     validators=[validate_password]
    # )
    # email = serializers.EmailField(
    #     required=True,
    #     validators=[UniqueValidator(queryset=User.objects.all())]
    # )

    class Meta:
        model = User
        fields = "__all__"
    
    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        # 패스워드를 hashing하기
        user.set_password(password)
        # 데이터베이스에 전달
        user.save()
        return user
    
    def update(self, instance, validated_data):
        email = serializers.EmailField(read_only=True)
        user = super().update(instance, validated_data)
        password = validated_data.get('password')
        if password:
            # 패스워드를 hashing하기
            user.set_password(password)
            # 데이터베이스에 전달
            user.save()
        return user


# 커스텀 토큰
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['name'] = user.name
        token['gender'] = user.gender
        token['age'] = user.age

        return token
    