from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class DetailInfo(models.Model):
    subject = models.CharField(max_length=200)
    render_subject = models.CharField(max_length=200,null=True)
    info = models.TextField()
    create_date = models.DateTimeField(null=True)
    def __str__(self):
        return self.subject

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name='author_comment')
    post=models.ForeignKey(DetailInfo, related_name='comments', on_delete=models.CASCADE)
    author_name=models.CharField(max_length=20)
    comment_text=models.TextField()
    created_at=models.DateTimeField(default=timezone.now) #장고에서 기본으로 제공됨
    # 들어갈 내용들 : 댓글 작성자, 댓글 내용, 댓글 작성 시간
    voter = models.ManyToManyField(User, related_name='voter_comment')
    def approve(self):
        self.save() 

    def __str__(self): 
        return self.comment_text

class Recomment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(DetailInfo, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Comment, null=True, blank=True, on_delete=models.CASCADE)