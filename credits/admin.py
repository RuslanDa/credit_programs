from django.contrib import admin
from .models import Organization, Offer, Partner, Checklist, Order


class OfferInline(admin.TabularInline):
    model = Offer
    extra = 3


class CheckListInline(admin.TabularInline):
    model = Checklist
    extra = 3


class OrderInline(admin.TabularInline):
    model = Order
    extra = 3


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'address', 'ogrn', 'reg_num', 'reg_date')
    readonly_fields = ('id', 'cbrf_id')
    list_display_links = ('title',)
    search_fields = ('title', 'ogrn', 'address')
    list_filter = ('title',)
    inlines = [
        OfferInline,
    ]


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'address', 'inn')
    readonly_fields = ('id',)
    list_display_links = ('title',)
    search_fields = ('title', 'inn')
    list_filter = ('title',)
    inlines = [
        CheckListInline,
    ]


class OfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'organization', 'created', 'updated', 'date_begin_rotation', 'date_end_rotation', 'min_scoring', 'max_scoring')
    readonly_fields = ('id',)
    list_display_links = ('title',)
    search_fields = ('title',)
    list_editable = ('date_begin_rotation',  'date_end_rotation')
    list_filter = ('type',)
    inlines = [
        OrderInline,
    ]
    

class ChecklistAdmin(admin.ModelAdmin):
    list_display = ('id', 'partner', 'last_name', 'first_name', 'middle_name', 'birthday', 'passport', 'scoring')
    readonly_fields = ('id',)
    list_display_links = ('first_name', 'partner')
    search_fields = ('last_name', 'title')
    list_filter = ('last_name', 'partner')
    inlines = [
        OrderInline,
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'checklist', 'offer', 'status')
    readonly_fields = ('id',)
    list_display_links = ('checklist',)
    search_fields = ('checklist', 'offer')
    list_filter = ('status',)

admin.site.site_header = 'Административная панель'
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Checklist, ChecklistAdmin)
admin.site.register(Order, OrderAdmin)
