from django.contrib import admin
from .models import Organization, Offer, Partner, Checklist, Order


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'address', 'ogrn', 'reg_num', 'reg_date')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'ogrn')
    list_editable = ('address',)
    list_filter = ('title',)


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'address', 'inn')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'inn')
    list_editable = ('address',)
    list_filter = ('title',)


class OfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'organization', 'created', 'updated', 'date_begin_rotation', 'date_end_rotation', 'min_scoring', 'max_scoring')
    #list_display_links = ('id', 'org_title')
    search_fields = ('title',)
    list_editable = ('date_begin_rotation',  'date_end_rotation')
    list_filter = ('type',)


class ChecklistAdmin(admin.ModelAdmin):
    list_display = ('id', 'partner', 'first_name', 'middle_name','last_name', 'birthday', 'passport', 'scoring')
    list_display_links = ('id', 'first_name')
    search_fields = ('id', 'first_name', 'title')
    list_filter = ('first_name', 'partner')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'checklist', 'offer', 'status')
    list_display_links = ('id', 'checklist')
    search_fields = ('id', 'checklist', 'offer')
    list_filter = ('status',)

admin.site.site_header = 'Административная панель'
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Checklist, ChecklistAdmin)
admin.site.register(Order, OrderAdmin)