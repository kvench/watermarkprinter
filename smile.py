import PIL
# импортируем модуль для запросов в интернет
import requests
# открываем файл с картинкой в бинарном режиме (rb) и читаем из него все
Image = open('people.jpg', 'rb').read()
# это адрес сервиса для распознавания эмоций
url = "https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize"
# словарь с двумя элементами - типом данных и ключом доступа
header = {
    "Content-Type": "application/octet-stream",
    "Ocp-Apim-Subscription-Key": "4f2ad86f11724c5287d94a2efb2731c6"
}
# отправляем запрос в microsoft прикладывая к нему словарь с заголовками и саму картинку
# ответ попадает в result
result = requests.post(url, headers=header, data = Image)
# парсим json и на выходе получаем словарь с лицами
faces = result.json()
fun_smile_image = Image.open('fun_smile.png')
for face in faces:
    fun_smile_image = fun_smile_image.resize((face['faceRectangle']['width'], int((face['faceRectangle']['height']/fun_smile_image.width) * fun_smile_image.height)))
    people_image.paste(fun_smile_image, (0,0), fun_smile_image)
people_image.show()
