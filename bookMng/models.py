from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class MainMenu(models.Model):
    item = models.CharField(max_length=200, unique=True)
    link = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.item


class Book(models.Model):
    name = models.CharField(max_length=200)
    web = models.URLField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    publishdate = models.DateField(auto_now=True)
    picture = models.FileField(upload_to='bookEx/static/uploads')
    pic_path = models.CharField(max_length=300, editable=False, blank=True)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


# used for the other wishlist
class Wishlist(models.Model):
    books = models.ForeignKey(Book, blank=True, null=True, on_delete=models.CASCADE)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Wish(models.Model):
    name = models.CharField(max_length=200)
    web = models.URLField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    picture = models.FileField(upload_to='bookEx/static/uploads')
    pic_path = models.CharField(max_length=300, editable=False, blank=True)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    books = models.ForeignKey(Book, blank=True, null=True, on_delete=models.CASCADE)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=8, null=True)

    def __str__(self):
        return str(self.id)


# contact us attempt
class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.CharField(max_length=400)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


# reviews attempt
class Review(models.Model):
    name = models.CharField(max_length=200)
    review = models.CharField(max_length=400)
    bookid = models.DecimalField(null=True, decimal_places=0, max_digits=10)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Checkout(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    card = models.PositiveIntegerField(blank=True,null=True)

    def __str__(self):
        return str(self.id)
