from django.db import models
from users.models import User

# verbose_name 없이 네이밍을 해도 되는 건가??????
# >>> fk제외하고 첫 번 인자가 verbose_name을 받을 수 있다.
class TodoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField("할일 제목", max_length=100)
    is_complate = models.BooleanField("완료 여부", default=False)
    created_at = models.DateTimeField("할일 생성 시간", auto_now_add=True)
    updated_at = models.DateTimeField("할일 마지막 수정 시간", auto_now=True)
    completion_at = models.DateTimeField("할일 완료 시간", blank=True, null=True)

    def __str__(self):    
        return self.title
    
    class Meta:
        ordering = ['-created_at']
        db_table = 'todolist'
    
    TODOLIST_FIELD = 'todo_lists',
    REQUIRE_FIELD = ['title',]

    # def get_absolute_url(self):
    #     return reverse('todolist_detail', args=[str(self.id)])

# Create your models here.
