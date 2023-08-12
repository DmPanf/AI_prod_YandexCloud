#@title Синхронное распознавание по IAM-токену
import json
import requests
from IPython.display import Audio

def yandex_recognize(fname, IAM_TOKEN, ID_FOLDER):
    URL = 'https://stt.api.cloud.yandex.net/speech/v1/stt:recognize'

    with open(fname, "rb") as f:
      data = f.read()

    # заголовок с IAM_TOKEN'ом:
    headers = {'Authorization': f'Bearer {IAM_TOKEN}'}

    # параметры:
    params = {
        'lang': 'ru-RU',
        'folderId': ID_FOLDER,
        'sampleRateHertz': 48000,
    }

    # запрос
    response = requests.post(
        URL,
        headers=headers,
        params=params,
        data=data)

    # декодируем ответ:
    decode_resp = response.content.decode('UTF-8')

    # преобразуем в json-формат
    text = json.loads(decode_resp)

    return text

a_file1 = './audio/sample1_8k.ogg'   # Путь к файлу
Audio(a_file1)                              # Проигрывание аудиофайла
yandex_recognize(
    fname = a_file1,
    IAM_TOKEN = IAM_TOKEN,
    ID_FOLDER = ID_FOLDER
)
