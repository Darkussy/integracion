from django.urls import path
from .views import index,Pagar,pago,procesar_pago,Webpay

urlpatterns = [
    path('', index, name="index"),
    path('Pagar/', Pagar, name='Pagar'),
    path('pago/', pago, name='pago'),
    path('Pagar/procesar_pago', procesar_pago, name='procesar_pago'),  # Nueva ruta para procesar_pago
    path('Webpay/', Webpay, name='Webpay'),
    
]