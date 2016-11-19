from django.conf.urls import url, patterns
from apps.notifications import views
from oauth2_provider import views as op_views

urlpatterns = patterns('',
    url(r'^$', views.notifications_by_feed, name='notifications-by-feed'),
    url(r'^feed/?$', views.set_notifications_for_feed, name='set-notifications-for-feed'),
    url(r'^apns_token/?$', views.set_apns_token, name='set-apns-token'),
    url(r'^android_token/?$', views.set_android_token, name='set-android-token'),
)