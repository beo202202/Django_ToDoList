from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response

from todo_lists.serializers import TodoListSerializer, TodoListCreateSerializer
from users.serializers import UserSerializer

from todo_lists.models import TodoList
from rest_framework.generics import get_object_or_404

class TodoListView(APIView):
    # 로그인 되어 있는지
    permission_classes = [permissions.IsAuthenticated]    

    def get(self, request):
        todolist = TodoList.objects.all()
        serializer = TodoListSerializer(todolist, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        print(f"{request.data=}")
        serializer = TodoListCreateSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"message":"작성완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)

class TodoListDetailView(APIView):
    # 로그인 되어 있는지
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(TodoList, pk=pk)

    def get(self, request, todolist_id):
        todolist = self.get_object(todolist_id)
        serializer = TodoListSerializer(todolist)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, todolist_id):
        todolist = self.get_object(todolist_id)
        if request.user == todolist.user:
            serializer = TodoListCreateSerializer(todolist, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"수정완료!"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)
    
    def delete(self, request, todolist_id):
        todolist = self.get_object(todolist_id)
        if request.user == todolist.user:
            todolist.delete()
            return Response({"message":"삭제완료!"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message":"권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)
