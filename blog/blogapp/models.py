from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20,unique=True)
    desc = models.TextField(blank=True)
    #date
    #models.DateField()
    #models.DateTimeField(auto_now=True)
    #models.TimeField()
    #models.BooleanField()
    #models.IntegerField()
    #models.PositiveIntegerField()
    #models.BinaryField()
    #models.ImageField()
    #models.FileField()
    #models.URLField()
    #models.EmailField()

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(unique=True, max_length=50)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    #Link category
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    picture = models.ImageField(upload_to='posts', null=True, blank=True)

    def __str__(self):
        return self.name
