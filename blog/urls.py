from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<str:slug>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<str:slug>/edit/', views.post_edit, name='post_edit'),
    path('signup/',views.signup_page, name = 'signup_page'),
    path('login/',views.login_page, name='login_page'),
    path('logout/',views.logout_page, name='logout_page'),
    path('profile/',views.profile_page, name='profile_page'),
    path('edit_profile/',views.edit_profile_page, name='edit_profile_page'),
    path('category/<str:slug>/',views.category_list, name='category'),
    path('tags/<str:slug>/',views.tag_list, name='tags'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
