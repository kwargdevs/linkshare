from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # new
from django.contrib.auth import views as auth_views

from users.forms import ResetPasswordForm, SetNewPasswordForm


urlpatterns = [
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

urlpatterns += staticfiles_urlpatterns() # new
