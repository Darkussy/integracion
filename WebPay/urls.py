from django.urls import path
from .views import index,Pagar,pago,procesar_pago,Webpay,agregar_producto,eliminar_producto,limpiar_carrito,restar_producto,tienda

urlpatterns = [
    path('', index, name="index"),
    path('Pagar/', Pagar, name='Pagar'),
    path('pago/', pago, name='pago'),
    path('Pagar/procesar_pago', procesar_pago, name='procesar_pago'),  # Nueva ruta para procesar_pago
    path('Webpay/', Webpay, name='Webpay'),
    path('tienda/',tienda, name="Tienda"),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),

]