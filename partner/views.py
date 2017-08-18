from django.views.generic import TemplateView
from oscar.apps.catalogue.models import Category
from .models import Partner
"""profile page view for partners a.k.a. grower
"""
class ProfileView(TemplateView):
    model = Partner
    template_name = "profile.html"

    #get superclass context and add to it
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        partnername = kwargs['partnername']
        context['partners'] = Partner.objects.all()
        context['user_less'] = False
        context['partner_details'] = Partner.objects.filter(name__iexact=partnername)
        return context

"""this view is like a list view for displaying all growers
"""
class GrowerView(TemplateView):
    model = Partner
    template_name = "growers.html"

    def get_context_data(self, **kwargs):
        context = super(GrowerView, self).get_context_data(**kwargs)
        context['partners'] = Partner.objects.all()
        context['user_less'] = False
        return context