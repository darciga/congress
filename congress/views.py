from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Conference, Applicants, Workshops, Rapporteur
from .serializer import AplicantsSerializer
from rest_framework import viewsets

def index(request):
    workshops = Workshops.objects.all()
    conferences = Conference.objects.all()

    template = "index.html"
    return render_to_response(template, context_instance=RequestContext(request, locals()))

#Vista para el serializer
class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicants.objects.all()
    serializer_class = AplicantsSerializer