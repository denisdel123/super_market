from django.urls import path

from marketApp.views import main, catalog, contacts, product, add_product, add_category
from marketApp.apps import MarketappConfig

app_name = MarketappConfig.name

urlpatterns = [
    path('', main, name='main'),
    path('catalog/', catalog, name='catalog'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/product/', product, name='product'),
    path('addProduct', add_product, name='addProduct'),
    path('addCategory', add_category, name='addCategory'),

]