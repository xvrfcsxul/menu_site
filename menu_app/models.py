from django.db import models
# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, default=None)

    def __str__(self) -> str:
        return self.name

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('MenuItem', blank=True, default=None, null=True, on_delete=models.CASCADE)
    href = models.CharField(max_length=100, blank=True, default=None, null=True)
    named_url = models.CharField(max_length=50, blank=True, null=True, default=None)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE, default=None, null=True)

    class Meta:
        ordering = ['menu', 'id']

    def __str__(self) -> str:
        return self.title
