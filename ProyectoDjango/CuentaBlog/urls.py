from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from CuentaBlog import views

urlpatterns = [
    path("crear/", views.SignUpView.as_view(), name ="signup"),
    path("profile/<pk>/", views.BlogProfile.as_view(), name ="blog_profile"),
    path("editar/<pk>/", views.BlogUpdate.as_view(), name ="blog_edit"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)