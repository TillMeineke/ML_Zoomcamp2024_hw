FROM agrigorev/model-2024-hairstyle:v3

RUN pip install keras-image-helper
RUN pip install --no-deps https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl

COPY homework_09_till_meineke.py .
ENV MODEL_NAME=model_2024_hairstyle_v2.tflite

CMD [ "homework_09_till_meineke.lambda_handler" ]
