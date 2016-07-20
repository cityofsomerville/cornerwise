from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^list$", views.layers_json, name="list-layers"),
]
