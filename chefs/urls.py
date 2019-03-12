from django.conf.urls import url
from chefs.views import ChefsListView


urlpatterns = [
    url(r'^$', ChefsListView.as_view(), name="chefs_list"),
]
