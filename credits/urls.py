from rest_framework import routers
from .api import OrganizationViewSet, OfferViewSet, PartnerViewSet, ChecklistViewSet
from django.urls import path, include
from credits import views
from django.conf.urls import url



router = routers.DefaultRouter()
router.register('api/orgs', OrganizationViewSet, 'orgs')
#router.register('api/offers', OfferViewSet, 'offers')
router.register('api/partners', PartnerViewSet, 'partners')
#router.register('api/chklists', ChecklistViewSet, 'chklists')

#path('api/partners/<int:partner_id>/chklists/', views.check_list, name='checklists')

#urlpatterns = router.urls
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/partners/(?P<partner_id>[0-9]+)/chklists/$', views.check_list, name='check-list'),
    url(r'^api/partners/(?P<partner_id>[0-9]+)/chklists/(?P<chklst_id>[0-9]+)/$', views.chklist_detail, name='check-list-detail'),
]
#urlpatterns = [
#    path('api/offers/', views.offer_list),
#    path('api/offers/<int:pk>/', views.offer_detail),
#    path('api-auth/', include('rest_framework.urls')),
#]
