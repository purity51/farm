import requests
import base64
from datetime import datetime
from django.conf import settings

def get_token():
    url = 'https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    response = requests.get(url, auth=(
        settings.MPESA_CONSUMER_KEY,
          settings.MPESA_CONSUMER_SECRET
    ))
    return response.json()['access_token']

def stk_push(phone, amount):
    token = get_token()
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    password = base64.b64encode(
        f"{settings.MPESA_SHORTCODE}{settings.MPESA_PASSKEY}{timestamp}".encode()
    ).decode()

    payload = {
        "BusinessShortCode": settings.MPESA_SHORTCODE,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone,  # customer phone e.g. 2547XXXXXXXX
        "PartyB": settings.MPESA_SHORTCODE,
        "PhoneNumber": phone,
        "CallBackURL": settings.MPESA_CALLBACK_URL,
        "AccountReference": "LenzisAgro",
        "TransactionDesc": "Payment for farm products"
    }

    response = requests.post(
        'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest',
        json=payload,
        headers={'Authorization': f'Bearer {token}'}
    )
    return response.json()