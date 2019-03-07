from django.db import models

class Text(models.Model):       # 글
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    body=models.TextField()

    def __str__(self):      # admin 
        return self.title

    def summary(self):      # ...more
        return self.body[:100]      # 100글자 단위로 끊음

class Comment(models.Model):        # 댓글
    name=models.CharField(max_length=50)
    content=models.TextField()

