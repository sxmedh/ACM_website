from django.urls import path
from user import views

urlpatterns = [
    path('', views.home, name='home'),
    path('membership/', views.membership, name='membership'),
    path('team/', views.team, name='team'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus/', views.contactUs, name='contactus'),
    path('event/', views.event_all, name='event_all'),
    path('event/<str:eventname>/', views.event_single, name='eventsingleuser'),
    path('news/<str:newsname>/', views.newssingle, name='newssingle'),
    path('notice/<str:noticename>/', views.noticeingle, name='noticeingle'),
    path('profile/', views.profile, name="user_profile"),
    path('calendar/', views.calender, name="calendar"),
    path('calendar/<str:label_name>', views.calender_label, name="calender_label"),
    path('clubs/', views.all_clubs_user, name="all_clubs_user"),
    path('clubsingle/<str:clubname>/',
         views.club_single_user, name="club_single_user"),

    path('ec/<str:clubname>/', views.club_ec_user, name="club_ec_user"),
    path('member/<str:clubname>/', views.member_req, name="member_req"),
    path('gallery/<str:clubname>/', views.gallery, name="gallery"),
    # path('404/', views.page_not_found_view, name="404")

]
handler404 = "user.views.page_not_found_view"
