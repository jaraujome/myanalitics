from django.db import models

# Copia aquí los modelos generados en analytics_models.py
# Modelo Sentimientos de chatt
class ChatMessage(models.Model):
    message = models.TextField()
    user_id = models.IntegerField()
    course_id = models.IntegerField()
       
# Modelo Sentimientos de Foros Discución
class ForumDiscussion(models.Model):
    name = models.CharField(max_length=255)
    forum_id = models.IntegerField()
    user_id = models.IntegerField()
    course_id = models.IntegerField()
           
# Modelo Sentimientos de Foros Post
class ForumPost(models.Model):
    message = models.TextField(max_length=255)
    user_id = models.IntegerField()
    discussion_id = models.IntegerField()
    course_id = models.IntegerField()
