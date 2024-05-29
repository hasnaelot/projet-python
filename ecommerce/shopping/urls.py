from django.urls import path # type: ignore

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.home, name="home"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('store/', views.store, name="store"),
    path('update_item/', views.updateItem, name="update_item"),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login')    

]