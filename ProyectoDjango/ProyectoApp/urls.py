
from django.urls import path
from ProyectoApp.views import BlogList, BlogDetail, BlogCreate, BlogLogin, BlogLogout, BlogUpdate

urlpatterns = [
   path('blog_list/', BlogList, name="blogList"),
    path('blog_detail/', BlogDetail, name="blogDetail"),
    path('blog_create/', BlogCreate, name="blogCreate"),
    path('blog_login/', BlogLogin, name="blogLogin"),
    path('blog_logout/', BlogLogout, name="blogLogout"),
    path('blog_update/', BlogUpdate, name="blogUpdate"),
]
