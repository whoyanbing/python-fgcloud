from django.db import models

# Create your models here.

class User(models.Model):

    user_id = models.AutoField(primary_key=True, verbose_name='用户ID')
    user_name = models.CharField(max_length=128, unique=True, verbose_name='用户名')
    user_password = models.CharField(max_length=256, verbose_name='用户密码')
    user_create_time = models.DateTimeField(auto_now_add=True, verbose_name='用户注册时间')

    def __str__(self):
        return self.user_name

    class Meta:
        ordering = ['-user_create_time']
        verbose_name = '用户列表'
        verbose_name_plural = '用户列表'