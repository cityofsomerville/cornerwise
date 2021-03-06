from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Subscription

import utils

User = get_user_model()


def not_logged_in(request):
    return render(request, "user/not_logged_in.djhtml")


def with_user(view_fn):
    """View decorator that attempts to log the user in using parameters passed in
    the URL query, if provided. If authentication succeeds, redirects to the
    same URL that got the user to this view, but with the query parameters
    removed.

    """
    def wrapped_fn(request, *args, **kwargs):
        try:
            user = authenticate(pk=request.GET["uid"],
                                token=request.GET["token"])
            if user:
                messages.success(request, "Welcome back!")
                login(request, user)
            if user or not request.user.is_anonymous:
                return redirect(utils.add_params(request.get_full_path(),
                                                 remove={"uid", "token"}))
        except KeyError:
            if not request.user.is_anonymous:
                return view_fn(request, request.user, *args, **kwargs)
            else:
                messages.error(request,
                               "You must be logged in to view that page.")

        return not_logged_in(request)

    return wrapped_fn


def with_user_subscription(view_fn):
    @with_user
    def wrapped_fn(request, user, *args, **kwargs):
        try:
            sub = user.subscriptions.get(pk=request.POST["subscription_id"])

            return view_fn(request, user,
                           user.subscriptions.get(pk=request.POST["subscription_id"]),
                           *args, **kwargs)
        except Subscription.DoesNotExist:
            messages.error(request, "Invalid subscription ID")
        except KeyError:
            messages.error(request, "Missing parameter 'subscription_id'")
        return redirect(request.META.get("HTTP_REFERER", reverse("manage-user")))
    wrapped_fn.__module__ = view_fn.__module__
    wrapped_fn.__name__ = view_fn.__name__

    return wrapped_fn


def user_emails(**kwargs):
    return User.objects.filter(**kwargs)\
                        .exclude(email="")\
                        .values_list("email", flat=True)


def group_emails(group_name):
    return user_emails(groups__name=group_name)


def admin_emails():
    return user_emails(is_superuser=True)
