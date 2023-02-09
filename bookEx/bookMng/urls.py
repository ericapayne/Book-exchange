from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book_detail/<int:book_id>', views.book_detail, name='book_detail'),
    path('book_delete/<int:book_id>', views.book_delete, name='book_delete'),
    path('postbook', views.postbook, name='postbook'),
    path('mybooks', views.mybooks, name='mybooks'),
    path('displaybooks', views.displaybooks, name='displaybooks'),
    path('searchbook', views.searchbook, name='searchbook'),
    path('submit_to_wishlist', views.submit_to_wishlist, name='submit_to_wishlist'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('wishlist_delete/<int:wishlist_id>', views.wishlist_delete, name='wishlist_delete'),
    path('add_to_cart/<int:book_id>', views.add_to_cart, name='add_to_cart'),
    path('cart', views.cart, name='cart'),
    path('cart_delete/<int:cart_id>', views.cart_delete, name='cart_delete'),
    path('get_total', views.get_total, name='get_total'),
    # contact us attempt
    path('contactus', views.contactus, name='contactus'),
    path('displaymessages', views.displaymessages, name='displaymessages'),

    # about us attempt
    path('aboutus', views.aboutus, name='aboutus'),

]
