
from django.urls import path
from ProyectoApp.views import BlogList, BlogDetail, BlogCreate, BlogLogin, BlogLogout, BlogUpdate
from ProyectoApp import views


urlpatterns = [
    path("index/", views.index, name="index"),
    path("blog_list/", views.BlogList.as_view(), name="blogList"),
    path("blog_detail/", views.BlogDetail.as_view(), name="blogDetail"),
    path("blog_create/", views.BlogCreate.as_view(), name="blogCreate"),
    path("blog_login/", views.BlogLogin.as_view(), name="blogLogin"),
    path("blog_logout/", views.BlogLogout.as_view(), name="blogLogout"),
    path("blog_update/", views.BlogUpdate.as_view(), name="blogUpdate"),
]
