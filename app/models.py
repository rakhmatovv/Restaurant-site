from django.db import models
from django.contrib.auth.models import User


class Products(models.Model):
    title = models.CharField(max_length=255, blank=True)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    price = models.IntegerField()
    thumb = models.ImageField(default='default.png')

    def __str__(self):
        return self.title


PARTY = [
    (1, '1 Human'),
    (2, '2 Human'),
    (3, '3 Human'),
    (4, '4 Human'),
]

SPENDING_TIME = [
    (1, '1 hour'),
    (2, '2 hour'),
]

TABLE = [
    (1, '1  Table'),
    (2, '2  Table'),
    (3, '3  Table'),
    (4, '4  Table'),
    (5, '5  Table'),
    (6, '6  Table'),
    (7, '7  Table'),
    (8, '8  Table'),
    (9, '9  Table'),
    (10, '10  Table'),
]


class BookTable(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date = models.DateField(null=True)
    party = models.PositiveSmallIntegerField(choices=PARTY, default=1)
    table = models.PositiveSmallIntegerField(choices=TABLE, default=1)
    phone = models.IntegerField()
    spending_time = models.PositiveSmallIntegerField(choices=SPENDING_TIME,
                                                     default=1)
    present_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.last_name}'


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.user.username
