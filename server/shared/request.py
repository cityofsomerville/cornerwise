from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render_to_response

import logging
import json
import re

logger = logging.getLogger("logger")


class ErrorResponse(Exception):
    def __init__(self, message, data=None, status=401, err=None):
        super(Exception, self).__init__(self, message)
        self.data = {"error": message}
        if data:
            self.data.update(data)
        self.status = status
        self.exception = err


def make_response(template=None, error_template="error.djhtml"):
    """
    View decorator

    Tailor the response to the requested data type, as specified
    in the Accept header. Expects the wrapped view to return a
    dict. If the request wants JSON, renders the dict as JSON data.
    """
    def constructor_fn(view):
        def wrapped_view(req, *args, **kwargs):
            use_template = template
            status = 200
            try:
                data = view(req, *args, **kwargs)
            except ErrorResponse as err:
                data = err.data
                use_template = error_template
                status = err.status
                # render error template or return JSON with proper error
                # code

            jsonp_callback = req.GET.get("callback")

            if jsonp_callback:
                content = json.dumps(data, cls=DjangoJSONEncoder)
                body = "{callback}({json})".format(callback=jsonp_callback,
                                                   json=content)

                response = HttpResponse(body, status=status)
                response["Content-Type"] = "application/javascript"
                return response

            accepts = req.META["HTTP_ACCEPT"]

            if not use_template \
               or re.search(r"application/json", accepts):
                response = JsonResponse(data, status=status)
                # TODO: We may (or may not!) want to be more restrictive
                # in the future:
                response["Access-Control-Allow-Origin"] = "*"
                return response

            return render_to_response(use_template, data, status=status)

        return wrapped_view

    return constructor_fn
