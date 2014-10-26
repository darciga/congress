from django.contrib import admin
from .models import Applicants, Rapporteur, Conference, Workshops

admin.site.register(Applicants)
admin.site.register(Rapporteur)
admin.site.register(Conference)
admin.site.register(Workshops)

