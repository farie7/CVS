from paynow import Paynow
import time

paynow = Paynow(
    '12312',
    '90fab47c-07e6-4415-92e9-9481177eb2d4',
    'http://google.com', 
    'http://google.com'
    )


payment = paynow.create_payment('Order', 'farierichmarume@gmail.com')

payment.add('Payment for stuff', 1)


# response = paynow.send_mobile(payment, '0777777777', 'ecocash')


if response.success:
    poll_url = response.poll_url

    print("Poll Url: ", poll_url)

    status = paynow.check_transaction_status(poll_url)

    #time.sleep(60)

    print("Payment Status: ", status.status)

