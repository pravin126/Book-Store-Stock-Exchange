from django.urls import path,include
from .import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('product',views.ProductView)

urlpatterns = [
    path('', views.index,name="index"),
    path('aboutus', views.aboutus,name="aboutus"),
    path('contactus', views.contactus,name="contactus"),
    path('delete/<contact_id>', views.delete,name="delete"),
    path('edit/<contact_id>', views.edit,name="edit"),
    path('market', views.market,name="market"),
    path('rest', include(router.urls)),

]