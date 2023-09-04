"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from revitdb import views
from revitdb import views, forms
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TopView.as_view(), name="top"),
    path('modelform/', views.modelform_upload, name='modelform'),   #ファイルアップロード画面

    path('revitdb/project_info/', views.Project_infoListView.as_view(), name="list"), #プロジェクト情報一覧

    path('revitdb/wall_finish/', views.Wall_finishListView.as_view(), name="wall_finish_list"),          #壁仕上一覧
    path('revitdb/ceiling_finish/', views.Ceiling_finishListView.as_view(), name="ceiling_finish_list"), #天井仕上一覧
    path('revitdb/floor_finish/', views.Floor_finishListView.as_view(), name="floor_finish_list"),       #床仕上一覧


    path("revitdb/product_list/", views.product_list, name="product_list"),          #部屋一覧
    # path('revitdb/room_list/', views.RoomListView.as_view(), name="room_list"),      #部屋一覧
    path('revitdb/update/<int:pk>', views.RoomUpdateView, name='room_update'),  #部屋の編集画面


    path('login/', views.LoginView.as_view(), name="login"),    #ログイン画面
    path('logout/', views.LogoutView.as_view(), name="logout"), #ログアウト画面



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

