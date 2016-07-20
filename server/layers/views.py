from django.shortcuts import render
from django.http import HttpResponseDirect
from django.forms.models import model_to_dict

from .models import Layer

# TODO:
#  * Pull data from the model.
#  * Accept get parameters (filter_by_region_name, etc..)
#  * Render data as raw JSON.


# URL FORMAT:
#  cornerwise.org/layers/list?region=Somerville&region=Cambridge
#
# PARAMETERS (FILTERS):
#  region='region name'
#  
def layers_json(req):
    regions = req.GET.getlist("region")
    layers = Layer.objects.filter(region_name__in=regions)
    mdict = model_to_dict(layers)

    return HttpResponse(mdict)
    
    
