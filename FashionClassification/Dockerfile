FROM public.ecr.aws/lambda/python:3.11

RUN pip install --upgrade pip
RUN pip install keras-image-helper "numpy<2.0"
# RUN pip install --extra-index-url \
#     https://google-coral.github.io/py-repo/ tflite_runtime
RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/refs/heads/main/tflite/tflite_runtime-2.14.0-cp311-cp311-linux_x86_64.whl

COPY ./models/clothing_model.tflite .
COPY lambda_function.py .

CMD [ "lambda_function.lambda_handler" ]

# ERROR: tflite_runtime-2.14.0-cp311-cp311-linux_x86_64.whl is not a supported wheel on this platform.
# Besause of Apple Silicon?