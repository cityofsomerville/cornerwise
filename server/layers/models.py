from django.db import models
from django.conf import settings

class Layer(models.Model):
    source = models.CharField(max_length=128,
                              help_text="The source of the layer data.")
    layer_id = models.CharField(max_length=64)
    icon = models.CharField(max_length=64)
    icon_credit = models.CharField(max_lenth=128)
    region_name = models.CharField(max_Length=128,
                                   default=settings.GEO_REGION,
                                   null=True,
                                   help_text="")
    title = models.CharField(max_length=128,
                             help_text="The name of the layer.")
    short_name = models.CharField(max_length=64,
                                  help_text="The shortened name of the layer.")
    info = models.CharField(max_length=512,
                            help_text="A general summary of what the layer represents.")
    template = models.TextField(default="",
                                help_text="The template used to display the layer. NOTE: possibly to be removed and made in to a distinct Django template.")
    color = models.CharField(max_length=24,
                             help_text="The color of the layer.")
    shown = models.BooleanField(default=False,
                                help_text="Switch for whether or not the layer is shown.")
    marker_type = models.CharField(max_length="24",
                                   help_text="The type of marker to display on the layer.")
    marker_color = models.CharField(max_length=24,
                                    help_text="The color of the marker being displayed.")
    marker_fillcolor = models.CharField(max_length=24)
    marker_radius = models.IntegerField(default=0)
    marker_fillopacity = models.IntegerField(default=0)
