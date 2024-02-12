""" from django.urls import path
from . import views

urlpatterns = [
       path("",views.index,name="index"),
    path("prodDetails/<int:pid>",views.prodDetails,name="prodDetails"),
    path("viewCart/",views.viewCart,name="viewCart"),
    path("addCart/<int:pid>",views.addCart,name="addCart"),
     path("removeCart/<int:pid>",views.removeCart,name="removeCart"),
     path("range",views.range,name="range"),
     path("watchList",views.watchList,name="watchList"),
     path("mobileList/",views.mobileList,name="mobileList"),
     path("priceOrder",views.priceOrder,name="priceOrder"),
     path("descpriceOrder",views.descpriceOrder,name="descpriceOrder"),
     path("updateqty/<int:uval>/<int:pid>/",views.updateqty,name="updateqty"),
     path("viewOrder/",views.viewOrder,name="viewOrder"),
     path("register/",views.register_user,name="register"),
     path("login/",views.login_user,name="login"),
     path("logout/",views.logout_user,name="logout"),
     path("payment/",views.makePayment,name="payment"),
     path("myOrders/",views.myOrders,name="myOrders"),
     path("insertProd/",views.insertProduct,name="insertProd"),

] """