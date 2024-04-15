from django.db import models

# Create your models here.
class Survey(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class Question(models.Model):
    content = models.CharField(max_length=255)
    order_num = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.content} - {self.is_active}'
    
class Answer(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='quizzes')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answers = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.survey.name} - {self.question.content}'