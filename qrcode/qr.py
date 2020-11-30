import qrcode

def generate(data, img_name="Qrcode.png"):
	img = qrcode.make(data)
	img.save(img_name)
	return img

#masukan url nya disini
url = "https://bookjakarta3.com/"
generate(url)