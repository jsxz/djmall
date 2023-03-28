from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig
from django.utils.module_loading import autodiscover_modules

class DadminConfig(AdminConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dadmin'
    default_site = 'dadmin.admin.DJMallAdminSite'
    def ready(self):
        autodiscover_modules('dadmin')