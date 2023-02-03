import qrcode

data=input("Enter any data and it will generate QR corresponding to that data! ")
athentha=qrcode.QRCode()
athentha.add_data(data)
athentha.print_ascii()
print("QR Generated successfully")