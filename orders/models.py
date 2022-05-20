from django.db import models

# Create your models here.
class product (models.Model):
  title=models.CharField(max_length=250)
  text=models.TextField()
  image = models.ImageField(blank=True, upload_to="images/")

  def __str__(self):
      return self.title


