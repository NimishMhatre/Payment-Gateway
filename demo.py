keyid = 'rzp_test_2aZu4AsWZNDstl'
keySecret = '0wvijWyDutLB2CzuNx18T8iv'

import razorpay
client = razorpay.Client(auth=(keyid, keySecret))


data = {
    "amount"         : 100*100,
    "currency"       : "INR",
    "receipt"        : "Ecommerce",
    "notes"          : {
        "name"  : "Nizer",
        "Payment_for"   : "Shirts"
    }
}

order = client.order.create(data=data)
print(order)

#{'id': 'order_GV1KRp27hyq9oa', 'entity': 'order', 'amount': 10000, 'amount_paid': 0, 'amount_due': 10000, 'currency': 'INR', 'receipt': 'Ecommerce', 'offer_id': None, 'status': 'created', 'attempts': 0, 'notes': {'name': 'Nizer', 'Payment_for': 'Shirts'}, 'created_at': 1611901011}
verdict = {"razorpay_payment_id": "pay_GTSSH63KUJUAU9", "razorpay_order_id": "order_GTSIZUUhFJ2AiC", "razorpay_signature": "7a5fbc1fa51ed24ae8741a7a42d0fe0bce730c11ca15d46289dc2b3bb3b8e84c"}

client.utility.verify_payment_signature(verdict)