from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "events/",
        views.events,
        name="events"
    ),

    path(
        "events/<int:event_id>/",
        views.event_detail,
        name="event_detail"
    ),

    path(
        "book/",
        views.book,
        name="book"
    ),

    path(
        "services/",
        views.services,
        name="services"
    ),

    path(
        "about/",
        views.about,
        name="about"
    ),

    path(
        "contact/",
        views.conatct,
        name="contact"
    ),
]