from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseUsers(models.Model):
    name = models.CharField(_("Name"), max_length=60)
    lastName = models.CharField(_("LastName"), max_length=80)
    email = models.EmailField(_("Email"))
    address = models.CharField(_("Address"), max_length=140)
    city = models.CharField(_("City"), max_length=90)
    telephone = models.CharField(_("Telephone"), max_length=30)

    class Meta:
        abstract = True


class Rapporteur(BaseUsers):
    company = models.CharField(_("Company"), max_length=160, help_text="Company or institution")

    class Meta:
        verbose_name = "Rapporteur"
        verbose_name_plural = "Rapporteurs"

    def __unicode__(self):
        return self.name


class BasePresentations(models.Model):
    name = models.CharField(_("Name"), max_length=140)
    description = models.TextField(_("Description"))
    objective = models.TextField(_("Objective"))
    dateBegin = models.DateField(_("Date begin"), auto_now=False)
    dateEnd = models.DateField(_("Date end"), auto_now=False)
    hourBegin = models.CharField(_("Hour Begin"), max_length=10)
    hourEnd = models.CharField(_("Hour end"), max_length=10)
    place = models.CharField(_("Place"), max_length=40)

    class Meta:
        abstract = True


class Conference(BasePresentations):
    rapporteur = models.ForeignKey(Rapporteur, related_name="Lecturer")

    class Meta:
        verbose_name = "Conference"
        verbose_name_plural = "Conferences"

    def __unicode__(self):
        return self.name


class Workshops(BasePresentations):
    rapporteur = models.ForeignKey(Rapporteur, related_name="Rapporteur")
    placesAvailable = models.IntegerField(_("Places available"), default=20)
    requirements = models.CharField(_("Requirements"), max_length=180, default="Laptop")

    class Meta:
        verbose_name = "Workshop"
        verbose_name_plural = "Workshops"

    def __unicode__(self):
        return self.name


class Applicants(BaseUsers):
    placeOrigin = models.CharField(_("Place of origin"), max_length=180, help_text="Company or institute")
    workshop = models.ManyToManyField(Workshops, verbose_name="Workshop")
    conference = models.ManyToManyField(Conference, verbose_name="Conference")

    class Meta:
        verbose_name = "Applicant"
        verbose_name_plural = "Applicants"

    def __unicode__(self):
        return self.name