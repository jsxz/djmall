from django.contrib.auth import get_user_model

from apps.dadmin.admin import admin_site

User = get_user_model()
admin_site.register(User)