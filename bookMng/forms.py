from django import forms
from django.forms import ModelForm
from .models import Book

from .models import Wishlist
from .models import Cart
from .models import Wish
from .models import Message
from .models import Review
from .models import Checkout


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
            'web',
            'price',
            'picture',
        ]


class SearchForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
        ]


class WishForm(ModelForm):
    class Meta:
        model = Wish
        fields = [
            'name',
            'price',
            'web',
        ]


class CartForm(ModelForm):
    class Meta:
        model = Cart
        fields = [
            'books',
        ]


# contact us attempt
class ContactForm(ModelForm):
    class Meta:
        model = Message
        fields = [
            'name',
            'email',
            'message',
        ]


# reviews attempt
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = [
            'name',
            'review',
        ]


class CheckoutForm(ModelForm):
    class Meta:
        model = Checkout
        fields = [
            'firstname',
            'lastname',
            'email',
            'address',
            'city',
            'state',

        ]
