from django.urls import path
from . import views
urlpatterns=[

    path('index/',views.index),
    path('',views.index),
    path('vissionmission/',views.vissionmission),
    path('donate/',views.donate),
    path('contact/',views.contact),
    path('about/',views.about),
    path('story/',views.story),
    path('volunteers/',views.ourvolunteers),
    path('events/',views.events),
    path('help/',views.help),
    path('viewevent/',views.viewevent),
    path('volunteerlist/',views.volunteerslist),
    path('detail/',views.details),
    path('poshan/',views.poshans),
    path('breakfast/',views.breakfast),
    path('feeding/',views.feedings),
    path('mother/',views.mothers),
    path('login/',views.login),




]