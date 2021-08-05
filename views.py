from django.shortcuts import render
from django.views.generic.base import TemplateView


class LoginView(TemplateView):
    """
    Ask the user to either log in or create an account.
    """
    template_name = "bookmarks/login.html"
    context = {}
