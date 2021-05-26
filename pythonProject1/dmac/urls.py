from django.urls import path
from . import views
# from rest_framework import routers
# from .api import LeadViewSet
# from tableview import views

# router = routers.DefaultRouter()
# router.register('api/leads',LeadViewSet,'leads')

app_name = 'dmac'
urlpatterns = [
    path('login/', views.adminhome, name='adminhome'),
    path('', views.loginpage, name='glogin'),
    # path('logout/', views.logout, name='glogin'),
    # path('article/', views.article_list, name='glogin'),
    # path('tab_details/', views.tab_details, name='tab_details'),
    path('mergetable/', views.merge_table, name='mergetable'),
    path('post/', views.post, name='post'),
    path('rest/', views.rest, name='rest'),
    path('dmacpage/', views.dmacpage, name='dmacpage'),
    path('table/', views.Table, name ="table"),
    path('finaljson/', views.finaljson, name ="finaljson"),
    path('posttable/', views.posttable, name ="posttable"),
    path('postdata/', views.postdata, name ="postdata"),
    path('postdata1/', views.postdata1, name ="postdata1"),
    path('addtable/', views.addtable, name ="addtable"),
    path('postdata3/', views.postdata3, name ="postdata3"),
    path('concatdata/', views.concatdata, name ="concatdata"),
    path('concattable/', views.concattable, name ="concattable"),
    path('thankyou/', views.thankyou, name ="thankyou"),
    path('dragdrop/', views.dragdrop, name ="dragdrop"),
    path('tables/', views.tables, name='tables'),
    path('connections/', views.connections, name='connections'),
    # path('jsonreducer/', views.jsonreducer, name ="jsonreducer"),
    # path('save_json_to_table/', views.save_json_to_table, name ="save_json_to_table"),

]
#comment
# urlpatterns = router.urls