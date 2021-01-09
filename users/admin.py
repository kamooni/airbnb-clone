from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from rooms import models as room_models

# Register your models here.


class RoomInline(admin.StackedInline):
    model = room_models.Room


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin"""

    inlines = (RoomInline,)
    # 현재 UserAdmin이라는 django에서 제공해주는 admin은 우리가 구성한 User model의 데이터를 모르는 상태

    # 그래서 fieldsets을 구성해줘야함

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )


# 단 위에 fieldsets을 구성했더니 그전에 있던 fieldsets 들이 사라지고 위에 것들이 대체되었음
# 그래서 UserAdmin.fieldsets을 더해주면됨
