from django.db import models

# Create your models here.


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question

class UserQuery(models.Model):
    user_text = models.TextField()
    bot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_text[:50]
