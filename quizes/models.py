from django.db import models
from django.utils.translation import gettext_lazy as _
import random

# Create your models here.

DIFICULTLY_CHOICES = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard')    
)

# all fields for a simple quiz
class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="duration of the quiz in minutes")
    required_score_to_pass = models.IntegerField(help_text="required score in %")
    difficultly = models.CharField(max_length=6,choices=DIFICULTLY_CHOICES)

    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizes")

    
    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions] 

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_absolute_url(self):
        return reverse("Quiz_detail", kwargs={"pk": self.pk})
