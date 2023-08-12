# pip -q install speechkit

from speechkit import Session, SpeechSynthesis
from speechkit import ShortAudioRecognition

def yandex_recognize_speechkit(fname, OAuth_token, ID_FOLDER, format='lpcm'):
  # Экземпляр класса `Session` можно получать из разных данных
  session = Session.from_yandex_passport_oauth_token(OAuth_token, ID_FOLDER)
  # Читаем файл
  with open(fname, 'rb') as f:
    data = f.read()

    # Создаем экземпляр класса с помощью `session` полученного ранее
    recognizeShortAudio = ShortAudioRecognition(session)

    # Передаем файл и его формат в метод `.recognize()`,
    # который возвращает строку с текстом
    text = recognizeShortAudio.recognize(
        data, format=format, sampleRateHertz='8000')
    print(text)

yandex_recognize_speechkit(
    fname = './audio/sample4_8k.ogg',
    OAuth_token = OAuth_token,
    ID_FOLDER = ID_FOLDER,
    format = 'oggopus'
)
