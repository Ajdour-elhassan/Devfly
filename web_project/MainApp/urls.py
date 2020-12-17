from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name='home'),
    path('category/<slug:category_slug>' , views.home , name='post_by_category'),
    path('category/<slug:category_slug>/<slug:post_slug>' , views.details_page , name='post_details'),
    path('account/create_an_account/' , views.sign_up , name='sign_up'),
    path('account/login' , views.sign_in , name='sign_in'),
    path('sign_out' , views.logoutView , name='sign_out'),
    path('about/' , views.about , name='about'),
    path('search/' , views.search , name='search'),
    path('contact/' , views.contact , name="contact"),
]

