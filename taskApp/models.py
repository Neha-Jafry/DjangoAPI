from ensurepip import version
from tkinter import CASCADE
from django.db import models

# Create your models here.

class Books(models.Model):


    BookId = models.AutoField(primary_key=True)
    BookTitle = models.CharField(max_length=100)

class Sections(models.Model):


    SectionId = models.AutoField(primary_key=True)
    SectionTitle = models.CharField(max_length=100)
    Content = models.CharField(max_length=10000, null=True)
    Parent = models.ForeignKey("Sections", on_delete=models.CASCADE, related_name='subsecs', related_query_name='subsecs', blank=True, null=True)
    Book = models.ForeignKey("Books", on_delete=models.CASCADE, null=True)
    isParent = models.BooleanField(default=False)
