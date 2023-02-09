from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import MainMenu

from .forms import BookForm
from .forms import SearchForm
from .forms import WishForm
from .forms import ContactForm
from .forms import ReviewForm
from .forms import CheckoutForm

from django.http import HttpResponseRedirect

from .models import Book

from .models import Wish
from .models import Cart
#from .models import CartItem
from .models import Message
from .models import Review

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required

from django.db.models import Sum
from django.db.models import Value
from django.db.models.functions import Coalesce


def index(request):
    return render(request,
                  'bookMng/index.html',
                  {
                      'item_list': MainMenu.objects.all()
                  })


@login_required(login_url=reverse_lazy('login'))
def postbook(request):
    submitted = False
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            book = form.save(commit=False)
            try:
                book.username = request.user
            except Exception:
                pass
            book.save()
            return HttpResponseRedirect('/postbook?submitted=True')
    else:
        form = BookForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request,
                  'bookMng/postbook.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted
                  })


@login_required(login_url=reverse_lazy('login'))
def displaybooks(request):
    books = Book.objects.all()
    for b in books:
        b.pic_path = b.picture.url[14:]
    return render(request,
                  'bookMng/displaybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books
                  })


class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)


@login_required(login_url=reverse_lazy('login'))
def book_detail(request, book_id):
    # if form submitted from book_detail.html (POST)
    if request.method == 'POST':
        # set form from POST request
        form = ReviewForm(request.POST, request.FILES)

        # if valid, save form
        if form.is_valid():
            review = form.save(commit=False)
            try:
                review.bookid = book_id
            except Exception:
                # similar to Java continue
                pass

            review.save()

    book = Book.objects.get(id=book_id)
    book.pic_path = book.picture.url[14:]
    # get review form
    form = ReviewForm()

    # get all reviews for book
    reviews = Review.objects.filter(bookid=book_id)
    return render(request,
                  'bookMng/book_detail.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'book': book,
                      'form': form,
                      'reviews': reviews,
                  })

#displays my books page
@login_required(login_url=reverse_lazy('login'))
def mybooks(request):
    books = Book.objects.filter(username=request.user)
    for b in books:
        b.pic_path = b.picture.url[14:]
    return render(request,
                  'bookMng/mybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books
                  })

#deletes book from display books
@login_required(login_url=reverse_lazy('login'))
def book_delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return render(request,
                  'bookMng/book_delete.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  })

# searches for a book in display books
def searchbook(request):
    submitted = False
    books = Book.objects.all()
    if request.method == 'POST':
        form = SearchForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            search = request.POST.get('name')

            return HttpResponseRedirect('/searchbook?submitted=True&name=' + search)
    else:
        form = SearchForm()
        if 'submitted' in request.GET:
            submitted = True
            search = request.GET.get('name')
            books = Book.objects.filter(name__contains=search)
            for b in books:
                b.pic_path = b.picture.url[14:]


    return render(request,
                  'bookMng/searchbook.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'books' : books,
                      'submitted': submitted,
                  })

#add books to the wishlist from display
#@login_required(login_url=reverse_lazy('login'))
#def add_to_wishlist(request, book_id):
    #books = Book.objects.all()
    #book = Book.objects.get(id=book_id)
    #wishlist = Wishlist.objects.all()
    #wishlist = Wishlist.objects.get_or_create(books=book,id=book_id, username=request.user)

    #return render(request,
                  #'extra/add_to_wishlist.html',
                  #{
                      #'item_list': MainMenu.objects.all(),
                  #})

@login_required(login_url=reverse_lazy('login'))
def wishlist(request):
    wishlist = Wish.objects.all()

    return render(request,
                  'bookMng/displaywishlist.html',
                  {
                      'item_list': MainMenu.objects.all(),
                       'wishlist': wishlist
                  })

@login_required(login_url=reverse_lazy('login'))
def wishlist_delete(request, wishlist_id):
    wish = Wish.objects.get(id=wishlist_id)
    wish.delete()
    return render(request,
                  'bookMng/wishlist_delete.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  })

#for form put in
@login_required(login_url=reverse_lazy('login'))
def submit_to_wishlist(request):
    submitted = False
    if request.method == 'POST':
        form = WishForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            wish = form.save(commit=False)
            try:
                wish.username = request.user
            except Exception:
                pass
            wish.save()
            return HttpResponseRedirect('/submit_to_wishlist?submitted=True')
    else:
        form = WishForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request,
                  'bookMng/submit_to_wishlist.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted
                  })


@login_required(login_url=reverse_lazy('login'))
def add_to_cart(request, book_id):
    books = Book.objects.all()
    book = Book.objects.get(id=book_id)
    cartlist = Cart.objects.all()
    cartlist = Cart.objects.get_or_create(books=book,id=book_id, username=request.user)

    return render(request,
                  'extra/add_to_cart.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  })

@login_required(login_url=reverse_lazy('login'))
def cart(request):
    cartlist = Cart.objects.filter(username=request.user)

    total = cartlist.aggregate(the_sum=Coalesce(Sum('price'), Value(0)))['the_sum']
    count = 0
    for item in cartlist:
        total += item.books.price




    return render(request,
                  'extra/cart.html',
                  {
                      'item_list': MainMenu.objects.all(),
                       'cartlist': cartlist,
                      'total' : total,
                      'count' : count,


                  })

@login_required(login_url=reverse_lazy('login'))
def cart_delete(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return render(request,
                  'extra/cart_delete.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  })






# contact us attempt
@login_required(login_url=reverse_lazy('login'))
def contactus(request):
    submitted = False

    # if (3. form submitted from contactus.html (POST))
    if request.method == 'POST':
        # set form from POST request
        form = ContactForm(request.POST, request.FILES)

        # if valid, save form and return with GET parameter
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contactus?submitted=True')

    # else (GET) (1. display an empty form to be filled out for the first time),
    else:
        form = ContactForm()

        # if (4. submitted is passed as GET parameter, set submitted to true)
        if 'submitted' in request.GET:
            submitted = True

    # (2., 5. render contactus.html page)
    return render(request,
                  'bookMng/contactus.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted,
                  })

# about us attempt
def aboutus(request):
    return render(request,
                  'bookMng/aboutus.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  })


@login_required(login_url=reverse_lazy('login'))
def displaymessages(request):
    # gets all messages from db
    messages = Message.objects.all()

    # get username
    username = request.user
    admin = (username.username == 'admin')

    return render(request,
                  'bookMng/displaymessages.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'messages': messages,
                      'admin': admin,
                      'username': username,
                  })

@login_required(login_url=reverse_lazy('login'))
def checkout(request):
    submitted = False
    if request.method == 'POST':
        form = CheckoutForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            checkout = form.save(commit=False)
            try:
                book.username = request.user
            except Exception:
                pass
            checkout.save()
            return HttpResponseRedirect('/checkout?submitted=True')
    else:
        form = CheckoutForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request,
                  'extra/checkout.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted
                  })


