import qrcode

upi_id = input("Enter your upi id =")

#difining payment url for various data;
# upi://pay?pa=upiaddress@okhdfcbank&pn=JohnDoe&cu=INR"

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&cu=INR'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&cu=INR'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&cu=INR'

phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# to save it im img form
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

#invoking pillow

phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()


