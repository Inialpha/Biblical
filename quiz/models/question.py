from django.db import models

class Question(models.Model):
    """ """
    CATEGORIES = {
        'new testament': "New Testament"
    }
    question_text = models.TextField(null=False)
    category = models.CharField(max_length=255, choices=CATEGORIES)
    difficulty = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.question_text


class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    option_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.option_text

