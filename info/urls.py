from django.conf.urls.defaults import patterns

urlpatterns = patterns('groundtruth.info.views',
    (r'(?P<model_name>[\w-]+)/popup$','info_popup_view'),
)