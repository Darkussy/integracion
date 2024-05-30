from django.shortcuts import render
from transbank.webpay.webpay_plus.transaction import Transaction, WebpayOptions, IntegrationCommerceCodes, IntegrationApiKeys
from transbank.common.integration_type import IntegrationType


# Create your views here.

def index(request):
    return render(request,"htmls/index.html")

def Pagar(request):
    precio = request.POST["valor"]
    return render(request,"htmls/Pagar.html", {'precio': precio})

def Webpay(request):
    return render(request,"htmls/Webpay.html")


#Api Webpay
def procesar_pago(request):
    token = request.GET.get('token_ws')

    transaction = Transaction(WebpayOptions(
        IntegrationCommerceCodes.WEBPAY_PLUS, 
        IntegrationApiKeys.WEBPAY, 
        IntegrationType.TEST))

    response = transaction.commit(token)

    status = response['status']
    amount = response['amount']
    buy_order = response['buy_order']

    context = {
        'status': status,
        'amount': amount,
        'buy_order': buy_order,
    }

    return render(request, 'htmls/Pagar.html', context)

def pago(request):
    buy_order = request.POST["ordenCompra"]
    session_id = request.POST["idSesion"]
    amount = request.POST["monto"]
    return_url = 'http://127.0.0.1:8000/Pagar/procesar_pago'

    transaction = Transaction(WebpayOptions(
        IntegrationCommerceCodes.WEBPAY_PLUS, 
        IntegrationApiKeys.WEBPAY, 
        IntegrationType.TEST))

    response = transaction.create(buy_order, session_id, amount, return_url)
    print (response)
    token = response['token']
    url = response['url']
    print(token,url)
    context = {
        'token': token,
        'url': url,
        'response': response  # Agrega response al contexto
    }
    
    return render(request, 'htmls/Pagar.html', context)
