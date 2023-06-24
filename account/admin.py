from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ["username", "email", "date_of_birth", "photo", "is_superuser"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "nickname",
                    "country",
                    "date_of_birth",
                    "photo",
                )
            },
        ),
        ("Permissions", {"fields": ("is_superuser", "is_staff", "is_active")}),
    )
    # add_fieldsets = (
    #     (
    #         None,
    #         {
    #             "classes": ("wide",),
    #             "fields": (
    #                 "username",
    #                 "email",
    #                 "country",
    #                 "nickname",
    #                 "password",
    #                 "password2",
    #             ),
    #         },
    #     ),
    # )


admin.site.register(CustomUser, CustomUserAdmin)
