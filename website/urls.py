from django.urls import path
from website.views import *
from .views import ComingSoonView

app_name = 'website'


urlpatterns = [
    # path('', ComingSoonView.as_view(), name='coming_soon'),
    path('',index_view, name = "index"),
    path('about',about_view, name = "about" ),
    path('contact',contact_view, name = "contact"),
    path('newsletter',newsletter_view, name = "newsletter"),
    

]