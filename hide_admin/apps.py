from django.contrib.admin.apps import AdminConfig


class HideAdminConfig(AdminConfig):
    default_site = "hide_admin.admin_site.HideAdminSite"
