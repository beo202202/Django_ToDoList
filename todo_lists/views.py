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
        # 이사람 꺼인지 확인하고 권한 확인해야함.
        todolist = self.get_object(todolist_id)
        serializer = TodoListCreateSerializer(todolist, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"수정완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
        

