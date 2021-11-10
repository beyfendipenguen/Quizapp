from django.db import models
from quizes.models import Quiz


# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")

    
    def get_answers(self):
        return self.answer_set.all()
    
    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("Question_detail", kwargs={"pk": self.pk})

class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Answers")
        verbose_name_plural = _("Answerss")

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct} "

    def get_absolute_url(self):
        return reverse("Answers_detail", kwargs={"pk": self.pk})
