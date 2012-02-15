from django.conf.urls.defaults import patterns, url
from serenesiri.views import CreatableInstanceModelView, ListOrCreateModelView

from product.resources import CategoryResource, ProductResource, PriceResource


urlpatterns = patterns('',
    url(r'^categories/?$', ListOrCreateModelView.as_view(resource=CategoryResource), name='category_list_or_create'),
    url(r'^categories/(?P<id>\d+)/?$', CreatableInstanceModelView.as_view(resource=CategoryResource), name='category_instance'),
    url(r'^products/?$', ListOrCreateModelView.as_view(resource=ProductResource), name='product_list_or_create'),
    url(r'^products/(?P<id>\d+)/?$', CreatableInstanceModelView.as_view(resource=ProductResource), name='product_instance'),
)
