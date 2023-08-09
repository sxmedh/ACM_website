
from django.contrib import admin
from django.urls import path,include
from eventapp import views
# from django.conf import settings
# from django.conf.urls.static import static
# manageevent.html
urlpatterns = [
    path('create/', views.createevent, name='createevent'),
    path('hosted/', views.hosted_events, name='hostedevent'),
    path('eventsingle/<str:eventname>', views.eventsingle, name='eventsingle'),
    path('participants/', views.participants, name='participants'),
    path('participants/<str:eventname>/', views.participants_details, name='participants_details'),
    #path('clubs/', views.clubs, name='allclubs')

]
# urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
