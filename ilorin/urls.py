from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),

    path('', views.storeView, name='vendor'),
    path('prod/<str:pk>/', views.viewProduct, name='product'),
    path('add/', views.addPhoto, name='add'),
    path('shop/<str:name>/', views.shopView, name='shop')
]

# the back in the photo view should go to vendor.id ..shop if not logged in ..rout it that way 
# Todo: add url for editing product for vendors .. and deleting products ..
# implement same in blog app also 