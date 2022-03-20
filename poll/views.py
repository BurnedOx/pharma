from datetime import datetime
from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator
from .models import *

# Create your views here.


def home_view(request):
    upcoming_events = Event.objects.filter(
        scheduled_date__gte=datetime.now()).order_by('scheduled_date')[:6]
    new_images = Media.objects.filter(src_type='image')[:9]
    template = "pages/home.html"
    context = {
        "home_page": "active",
        "events": upcoming_events,
        "gallery": new_images,
    }
    return render(request, template, context)


class AboutView(generic.TemplateView):
    template_name = "pages/about.html"

    def get(self, request):
        members = Member.objects.all()
        context = {
            "about_page": "active",
            "members": members,
        }
        return render(request, self.template_name, context)


def events_view(request):
    events_list = Event.objects.all()
    paginator = Paginator(events_list, 9)

    page = request.GET.get('page')
    events = paginator.get_page(page)

    template = "pages/events.html"
    context = {
        "events_page": "active",
        "events": events
    }
    return render(request, template, context)


class EventDetailView(generic.DetailView):
    model = Event
    template_name = "pages/event.html"

    def get(self, request, *args, **kwargs):
        event = self.get_object()
        gallery = Media.objects.filter(event=event, src_type='image')
        context = {
            "event": event,
            "gallery": gallery,
        }
        return render(request, self.template_name, context)


class GalleryView(generic.TemplateView):
    template_name = "pages/gallery.html"

    def get(self, request):
        gallery_list = Media.objects.all()
        paginator = Paginator(gallery_list, 9)

        page = request.GET.get('page')
        gallery = paginator.get_page(page)

        context = {
            "gallery_page": "active",
            "gallery": gallery
        }
        return render(request, self.template_name, context)


class ContactView(generic.TemplateView):
    template_name = "pages/contact.html"

    def get(self, request):
        context = {"contact_page": "active"}
        return render(request, self.template_name, context)
