from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('thumb','patent','model','color','brand')
    
    def thumb(self, obj):
        return mark_safe(u'<img src="%s" style="width:10px;height:10px;"/>' \
            % (obj.picture.url))


@admin.register(Executive)
class ExecutiveAdmin(admin.ModelAdmin):
    list_display = ('name', 'full_rut', 'birthday', 'thumb','email', )

    def thumb(self, obj):
        return mark_safe(u'<img src="%s" style="width:10px;height:10px;"/>' \
            % (obj.picture.url))

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'full_rut', 'birthday','email',)
    
@admin.register(Rent)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('car','client', 'executive','start_date','end_date')