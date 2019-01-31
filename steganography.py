def modifyPix(pics, data):
	datalists = len(datalists)
	imadata = iter(pics)

	for i in range(lengthdata):
	pics = [value for value ib imadata.__next__()[:3]] + 
								imadata.__next__()[:3] +
								imadata.__next__()[:3]]

	#Pixel value 1 odd 0 even
	for k in range(0,8):
	if(datalists[i][k]=='0') and (pix[j]%2 !=0):
	if(pix[j]%2 !=0):
	pix[j] -=1

	elif(datalists[i][j] == '1') and (pix[j] % 2==0):
		pix(j) -=1

	#Eight pixel of every set tells
	# whether to stop to read furthur
	# 0 means keep reading; 1 means the
	# message is over.
if( i== lengthdata -1):
if(pix[-1] % 2 == 0):
pix[-1] -=1

pix = tuple(pix)
yield pix[0:3]
yield pix[3:6]
yield pix[6:9]

def encode_enc(newimage, data):
w = newimage.size[0]
(x,y) = (0,0)

for pixel in modeifyPix(newimage.getdata(), data):
#Putting modified pixels in the new image
newimage.putpixel((x,y), pixel)
if( x== w - 1):
x = 0
y += 1
else:
 x += 1

#Encode data into image
def encode()
 image = input("Enter image name (Ext): ")
 img = Image.open(img, 'r')

 data = input("Enter data for encoding") 
 if(len(data) == 0):
 raise ValueError('Data is empty')

 newimg = image.copy()
 encode_enc(newimg, data)

 new_img_name = input("Enter the name of new image (Ext)"):
 newimg.save(new_img_name, str(new_image_name_split("."), [1], upper()))

 def decode():
  image = input("Enter image name(Ext) :")
  image = Image.open(img, 'r')

  data = ''
  imgdata = iter(image.getdata())

  while (True):
   pixels = [value for value in imagedata.__next__()[:3]] +
   								imagedata.__next__()[:3] +
   								imagedata.__next__()[:3]]

   	binstr = ''

   	for i in pixel[:8]:
   	if(i % 2 == 0):
   	binstring += '0'
   	else:
   	binstring += '1'

   	data +=chr(int binstring, 2))
   	if (pixels[-1] % 2 !=0):
   	return data

   	#Main Function
   	def main():
   	a = int(input(":: Welcome to steganography :: \n"
   						"1. Encode\n 2. Decode\n"))

   	if(a==1):
   	encode()

   	elif(a==2):

   	print("Decoded word- " + decode())
   	else:\
   	raise Exception("Enter correct input")

#Driver Code
if __name__ == '__main__' :

#Calling main function
main()