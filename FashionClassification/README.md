# Fashion Classification

This week, we´ll learn about neural nets and build a model for classifying images of clothes.

## Multiclass Classification

Dataset:
- Full: [https://github.com/alexeygrigorev/clothing-dataset](https://github.com/alexeygrigorev/clothing-dataset)
- Small: [https://github.com/alexeygrigorev/clothing-dataset-small](https://github.com/alexeygrigorev/clothing-dataset-small)

Links:
- [https://cs231n.github.com](https://cs231n.github.com)

## TensorFlow and Keras

## Serverless Deep learning

### 9.1 Introduction to Serverless

- Modul 9 covers serverless deep learning

### 9.2 AWS Lambda

- Intro to AWS Lambda
- Serverless vs serverfull
- only pay when your code runs, don need to worry about servers or scaling

### 9.3 TensorFlow Lite

- Why not TensorFlow
  - to big
  - lambda had a limit of 50MB, now larger up to 10GB for Docker images
    - $$$ for storage
    - slow init
    - slow to import, bigger ram footprint
- Converting the model
- Using the TF-Lite model for making predictions
  - inference (`model.predict(X)`)

### 9.4 Preparing the Lambda code

- Moving the code from notebook to script
- Testing it locally

### 9.5 Preparing a Docker image

- Lambda base images
- Preparing the dockerfile
- Using the right TF-Lite wheel
  - not working on Apple Silicon

### 9.6 Creating the lambda function

- Publishing the image to AWS ECR
```bash
pip install awscli
aws ecr create-repository --repository-name clothing-tflite-images
aws ecr get-login --no-include-email | sed "s/[0-9a-zA-Z=]\{20,\}/PASSWORD/g"
(aws ecr get-login --no-include-email)
```
- Creating the function
- Configuring it
- Testing the function from the AWS console
- Pricing

### 9.7 API Gateway: exposing the lambda function

- Creating and configuring the gateway

### 9.8 Summary

- AWS Lambda is way of deploying models without having to worry about servers
- TensorFlow Lite is a lightweight alternative to TensorFlow that only focuses on inference
- To deploy your code, package it in a Docker container
- Expose the lambda function via API Gateway

### 9.9 Explore more

- Google Cloud Functions, Azure Functions, Heroku?
- works for other models as well
- check homework

## Extra: BentoML

- [https://github.com/bentoml/bentoctl](https://github.com/bentoml/bentoctl)
- Terraform Hashicorp