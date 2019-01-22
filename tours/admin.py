from django.contrib import admin
from .models import Destination, Gallery, Tour, TourDetail
from django_summernote.admin import SummernoteModelAdmin

class TourDetailModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(Destination)
admin.site.register(Gallery)
admin.site.register(Tour)
admin.site.register(TourDetail, TourDetailModelAdmin)
