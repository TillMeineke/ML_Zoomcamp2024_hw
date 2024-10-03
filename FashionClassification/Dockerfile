FROM public.ecr.aws/lambda/python:3.10

RUN pip install --upgrade pip
RUN pip install keras-image-helper
RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/blob/main/tflite/tflite_runtime-2.14.0-cp311-cp311-linux_x86_64.whl

COPY ./models/clothing_model.tflite .
COPY lambda_function.py .

CMD [ "lambda_function.lambda_handler" ]

# ERROR: tflite_runtime-2.14.0-cp311-cp311-linux_x86_64.whl is not a supported wheel on this platform.
# Besause of Apple Silicon?