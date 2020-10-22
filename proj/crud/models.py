from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='logo')
    def __str__(self):
      return self.description
class tag(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    refr = models.CharField(max_length=50)
    def __str__(self):
      return self.refr
      
class likes(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    def __str__(self):
      return self.count
