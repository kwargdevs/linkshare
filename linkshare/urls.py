from django.contrib import admin
from django.urls import path, include, re_path
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns # new
from django.contrib.auth import views as auth_views

from users.forms import ResetPasswordForm, SetNewPasswordForm

from django.views.static import serve
from django.conf import settings


urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path("admin/", admin.site.urls),
    path("", include("links.urls")),
    path('users/', include('users.urls')), # new
    path("password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name= "registration/password-reset.html",
            form_class=ResetPasswordForm
        ),
        name= "password_reset"
    ),
    path("passwordreset-done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name= "registration/password-reset-done.html"
        ),
        name= "password_reset_done"
    ),
    path("password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name= "registration/password-reset-confirm.html",
            form_class=SetNewPasswordForm
        ),
        name= "password_reset_confirm"
    ),
    path("password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name= "registration/password-reset-complete.html"
        ),
        name= "password_reset_complete"
    ),

]

