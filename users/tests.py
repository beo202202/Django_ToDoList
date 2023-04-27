# from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User

# https://docs.djangoproject.com/en/4.2/topics/testing/overview/
class UserRegistrationTest(APITestCase):
    # 테스트 DB로 실행되고, 순서도 모르고, 자동 초기화 되기 때문에 서로 독립적이여야 한다.
    # Setup을 이용하면 잠시나마 초기화를 보류하고 테스트 가능하다.
    def test_registration(self):
        url = reverse("user_view")
        user_data = {
            "email": "test@testuser.com",
            "password": "testpassword",
            "name": "test",
            "gender": "M",
            "age": "40",
            "introduction": "test",
        }
        response = self.client.post(url, user_data)

        # print(user_data)
        # print(response.data)
        self.assertEqual(response.status_code, 201)
    
    # def test_update(self):
    #     url = reverse("user_view")
    #     user_data = {
    #         "email": "test@testuser.com",
    #         "password": "test2password",
    #         "name": "test2",
    #         "gender": "M",
    #         "age": "40",
    #         "introduction": "test2",
    #     }
    #     response = self.client.update(url, user_data)

    #     # print(user_data)
    #     # print(response.data)
    #     self.assertEqual(response.status_code, 201)


# 수정도 넣기

# 위와 아래는 같은 역할이기 떄문에 나중에 통합을 하자.
class LoginUserTest(APITestCase):
    def setUp(self):
        self.data = {
            "email": "test@testuser.com",
            "password": "testpassword",
            "name": "test",
            "gender": "M",
            "age": 40,
            "introduction": "",
        }
        # 과거 오류 발생지 (=패스워드는 뒤에 놔둬야 오류가 안생긴다. 왜 그럴까?)
        # => models.py에 정해준 create_user에서 정해준 순서대로 해야한다.
        self.user = User.objects.create_user(
            "test@testuser.com",            
            "test",
            "M",
            40,
            "",
            "testpassword"
        )
    
    # 과거 오류 발생지 (=왜 오류뜨는지 원인 못 찾음.)
    # >> 단순 철자 문제 serializer.py > serializers.py
    # 토큰 받기
    def test_login(self):
        response = self.client.post(reverse('token_obtain_pair'), self.data)
        # print(response.data["access"])
        self.assertEqual(response.status_code, 200)

    def test_post_user_refresh(self):
        refresh_token = self.client.post(reverse('token_obtain_pair'), self.data).data['refresh']
        response = self.client.post(reverse("token_refresh"), {"refresh":refresh_token})

        # 밑과 같은 방식으로는 안되나?
        # response = self.client.post(
        #     path=reverse("token_refresh"),
        #     HTTP_AUTHORIZATION = f"Bearer {refresh_token}"
        # )
        print(response.data["access"])
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data['email'], self.data['email'])

# 추후 로그아웃, 수정, 회원 탈퇴 테스트도 해야한다.