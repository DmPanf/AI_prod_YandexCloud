# AI_prod_YandexCloud
AI Integration based on YbadexCloud &amp; DataSphere


## ✅ СИНТЕЗ РЕЧИ
🌐 https://cloud.yandex.ru/docs/speechkit/tts/?from=int-console-empty-state

### Подготовительные шаги:
- AWS Access Key ID:
- AWS Secret Access Key:
- Default region name: ru-central1
  
<p>
<code>
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip -q awscliv2.zip

aws configure
aws --endpoint-url=https://storage.yandexcloud.net s3 mb s3://dnp34-study-ai
aws --endpoint-url=https://storage.yandexcloud.net s3 ls --recursive s3://dnp34-study
aws --endpoint-url=https://storage.yandexcloud.net s3 mv s3://dnp34-study/sample4.mp3 s3://dnp34-study-ai/audio/
aws --endpoint-url=https://storage.yandexcloud.net s3 ls --recursive s3://dnp34-study-ai/audio/
aws --endpoint-url=https://storage.yandexcloud.net s3 cp --recursive s3://dnp34-study-ai/audio/ ./audio

pip install -q pydub
apt install -q ffmpeg
</code>
</p>
