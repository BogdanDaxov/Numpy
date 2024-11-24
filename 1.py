from PIL import Image
import numpy as np

# считаем картинку в numpy array
for i in range(1,4):
    img = Image.open("lunar_images/lunar0"+str(i)+"_raw.jpg")
    data = np.array(img)
    a=data.min()
    b=data.max()
    data=round(255/(b-a))*(data-a)
    res_img = Image.fromarray(data)
    res_img.save("new_lunar_images/new_lunar0"+str(i)+"_raw.jpg")