from django.shortcuts import render
from django.http import HttpResponseDirect
from .models import Layer

# TODO:
#  * Pull data from the model.
#  * Accept get parameters (filter_by_region_name, etc..)
#  * Render data as raw JSON.

def layers_json(req):
    layers = Layer.
