from PIL import Image
dog_image = Image.open("dog.jpg")
watermark_image = Image.open("watermark.png")
pixels = dog_image.load()
watermark_image = watermark_image.resize((600, int((600/watermark_image.width) * watermark_image.height)))
dog_image.paste(watermark_image, (0,0), watermark_image)
dog_image.show()
