import qrcode
import image
qr = qrcode.QRCode(
    version = 15,  #15 means the version of qr code high the number bigger the code and complicated picture 
    box_size = 10,  # size of the box where qr code will be displayed
    border = 5   # it is the white part of image -- border with all 4 sides with white color
)

data = "https://www.youtube.com/"
# as i have given the path of my channel like the same way you can give anything
# if you don't want to redirect and create for normal text that write text in quotes

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black",black_color = "white")
img.save("test.png")