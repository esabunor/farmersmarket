from django.utils.translation import ugettext_lazy as _
from django.db import models
from oscar.apps.partner.abstract_models import AbstractPartner as CorePartner

class Partner(CorePartner):
    users = models.ManyToManyField('auth.User', related_name="partners", verbose_name=_("Users"))
    companyimage = models.ImageField(blank=True, upload_to="media/partners/companyimage")
from oscar.apps.partner.models import *  # noqa isort:skip