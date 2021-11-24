from django.db import models
from django.contrib.auth.models import User
from quizes.models  import Quiz
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()



    class Meta:
        verbose_name = _("Result")
        verbose_name_plural = _("Results")

    def __str__(self):
        return f"{self.user}-{self.quiz.name}-{self.score}"

    def get_absolute_url(self):
        return reverse("Result_detail", kwargs={"pk": self.pk})
