from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response

from users.serializers import UserSerializer

from users.models import User
from rest_framework.generics import get_object_or_404

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
class UserView(APIView):
    # 회원 가입
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"가입완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    # 로그인 되어 있는지만 확인하는 것 같은데?
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, user_id):
        return get_object_or_404(User, id=user_id)

    # 회원 수정
    def put(self, request, user_id):
        user = self.get_object(user_id)
        # print(f"{request.user=}")
        # print(f"{user=}")
        # 왜 users.user 하면 오류가 발생할까? 에 대해 생각을 하였다.
        if request.user == user:
            serializer = UserSerializer(user, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"수정완료!"}, status=status.HTTP_200_OK)
            else:
                return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"권한이 없습니다!"}, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, user_id):
        user = self.get_object(user_id)
        if request.user == user:
            user.delete()
            return Response({"message":"삭제 완료!"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다!", status=status.HTTP_403_FORBIDDEN)

# 로그아웃 방법
# 1. 사용자의 액세스 토큰삭제
# 2. 서버에 액세스 토큰의 기간을 만료 요청
# 3. 서버에 블랙리스트 추가 요청

# 서버에 블랙리스트 요청을 하는 것으로 바꿈.
# 로컬스토리지에서 access만 삭제하면 됨.
# class LogoutView(APIView):
#     def post(self, request):
#         # refresh_token = request.data["refresh_token"]
#         # print(f"{refresh_token=}")
#         try:
#             refresh_token = request.data["refresh_token"]
#             print(f"{refresh_token=}")
#             token = RefreshToken(refresh_token)
#             token.blacklist()  # 블랙리스트에 추가
#             return Response(status=status.HTTP_205_RESET_CONTENT)
#         except (TokenError, KeyError, InvalidToken):
#             return Response(status=status.HTTP_400_BAD_REQUEST)

# Djoser
# 이메일 인증, 비밀번호 초기화, 사용자 프로필 업데이트 등의 기능
# RESTful API와 OAuth2 인증도 지원