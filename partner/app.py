from django.conf.urls import url
from oscar.core.application import Application
from .views import ProfileView, GrowerView
#Providing custom url for growers profile view and other custom views

class PartnerApplication(Application):
    def get_urls(self):
        urlpatterns = [
            url(r'^growers/(?P<partnername>.*)/$', ProfileView.as_view(), name='growersprofileview'),
            url(r'^growers/$', GrowerView.as_view(), name='growersview')
        ]

        return urlpatterns

application = PartnerApplication()