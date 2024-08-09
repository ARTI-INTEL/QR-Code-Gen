import qrcode

data = str(input("Enter link you want QR Coded: "))
name = str(input("Enter what you would like the file to be called: "))

img = qrcode.make('Some data here')
type(img)  # qrcode.image.pil.PilImage
img.save(f"{name}.png")