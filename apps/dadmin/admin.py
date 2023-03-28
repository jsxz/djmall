from django.contrib.admin import AdminSite

# Register your models here.
from .forms import DadminAuthenticationForm


class DJMallAdminSite(AdminSite):
    site_header = 'DJmall'
    site_title = '商城系统'
    # login_form = DadminAuthenticationForm
    login_template = 'dadmin/login.html'

admin_site = DJMallAdminSite(name='dadmin')
