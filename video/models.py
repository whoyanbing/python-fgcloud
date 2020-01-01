from django.db import models

# Create your models here.


class Type(models.Model):
    """视频类型表"""
    # 类型id
    type_id = models.AutoField(primary_key=True)
    # 类型名称
    type_name = models.CharField(max_length=60)
    # 子类id
    type_mid = models.PositiveSmallIntegerField(null=True)
    # 父类id
    type_pid = models.PositiveSmallIntegerField(null=True)
    # 类型状态
    type_status = models.BooleanField()

    def __str__(self):
        return self.type_name

    class Meta:
        # 定义表名
        db_table = 'video_type'
        # 定义排序规则
        ordering = ['type_id']

class Video(models.Model):
    """视频信息表"""
    # 视频id
    video_id = models.AutoField(primary_key=True)
    # 视频名称
    video_name = models.CharField(max_length=255)
    # 视频类型
    video_type = models.ForeignKey("Type", on_delete=models.CASCADE)
    # 视频下标
    video_sub = models.CharField(max_length=255)
    # 视频状态
    video_status = models.BooleanField()
    # 视频首字母
    video_letter = models.CharField(max_length=1)
    # 视频标签
    video_tag = models.CharField(max_length=100)
    # 视频分类
    video_class = models.CharField(max_length=255)
    # 视频图片地址
    video_pic = models.CharField(max_length=255)
    # 视频缩略图地址
    video_pic_thumb = models.CharField(max_length=255)
    # 视频演员
    video_actor = models.CharField(max_length=255)
    # 视频导演
    video_director = models.CharField(max_length=255)
    # 视频备注
    video_remarks = models.CharField(max_length=255)
    # 视频发布时间
    video_pubdate = models.DateTimeField(auto_now_add=True)
    # 视频简介
    video_content = models.TextField()
    # 视频播放地址
    video_play_url = models.CharField(max_length=255)

    def __str__(self):
        return self.video_name

    class Meta:
        db_table = 'video_info'
        ordering = ['video_pubdate', 'video_id']