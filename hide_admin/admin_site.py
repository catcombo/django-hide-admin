from functools import update_wrapper

from django.contrib import admin
from django.http import Http404
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect


class HideAdminSite(admin.AdminSite):
    def admin_view(self, view, cacheable=False):
        def inner(request, *args, **kwargs):
            if not self.has_permission(request):
                raise Http404
            return view(request, *args, **kwargs)

        if not cacheable:
            inner = never_cache(inner)

        if not getattr(view, "csrf_exempt", False):
            inner = csrf_protect(inner)

        return update_wrapper(inner, view)

    @never_cache
    def login(self, request, extra_context=None):
        raise Http404
