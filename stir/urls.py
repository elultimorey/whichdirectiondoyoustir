from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
                       (r'^$', 'stir.main.views.main'),
                       (r'^stats/(.*)$', 'stir.main.views.stats'),
)