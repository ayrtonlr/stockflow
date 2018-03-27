
from django.contrib import admin

from .models import Wallet, Company, MyModelAdmin, NewsCompany,DescriptionCompany, ImageCompany

admin.site.register(Wallet, MyModelAdmin)
admin.site.register(Company)
admin.site.register(NewsCompany)
admin.site.register(DescriptionCompany)
admin.site.register(ImageCompany)
