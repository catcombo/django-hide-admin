# django-hide-admin

Hides Django admin from users without staff level access. Anonymous users or users without staff level access will see `404 Not found` error if they try to open the Django admin login page or any other admin pages.

Since the Django admin login page is not available, your project should have a login page for users and staff. Once staff are logged in, they can open `/admin/` (by default) to access admin interface.

# Prerequisites

- Python 3.7+
- Django 2.2+

# Installation

```
pip install django-hide-admin
```

# Usage

Replace `django.contrib.admin` with `hide_admin.apps.HideAdminConfig` in `INSTALLED_APPS`.
