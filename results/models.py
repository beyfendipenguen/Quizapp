from django.db import models
from django.contrib.auth.models import User
from quizes.models  import Quiz
# Create your models here.

class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()



    class Meta:
        verbose_name = _("Result")
        verbose_name_plural = _("Results")

    def __str__(self):
        return self.pk

    def get_absolute_url(self):
        return reverse("Result_detail", kwargs={"pk": self.pk})
