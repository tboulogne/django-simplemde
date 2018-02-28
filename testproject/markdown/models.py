from django.db import models
from inscrybmde.fields import InscrybMDEField


class Markdown(models.Model):
    title = models.CharField(max_length=32)
    content = InscrybMDEField()
