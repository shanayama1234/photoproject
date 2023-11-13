from django.contrib import admin

#CustomUserをインポートする
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):

    #レコード一覧にidとusernameを表示
    list_display=('id','username')

    #表示するカラムにリンクを設定
    list_display_links=('id','username')

#Django管理サイトにCustomUser,CustomUserAdminを登録する
admin.site.register(CustomUser,CustomUserAdmin)