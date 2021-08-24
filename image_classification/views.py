from django.conf import settings
from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from django.core.files.storage import FileSystemStorage
from torchvision import models
from torchvision import transforms
import torch.nn as nn
import torch
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import base64

device = torch.device("cpu") # device 객체

cnn_model =  models.resnet34(pretrained=True)
cnn_model.eval()

class_names = ['Kozel dark beer', 'heineken dark beer', 'pilsner urquell beer', 'tiger lemon beer', 'weihenstephan beer']
# Create your views here.

def imshow(input, title):
    # torch.Tensor를 numpy 객체로 변환
    input = input.numpy().transpose((1, 2, 0))
    # 이미지 정규화 해제하기
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    input = std * input + mean
    input = np.clip(input, 0, 1)
    # 이미지 출력
    plt.title(title)
    plt.show()


def image_upload(request):
    image_uri = None
    predicted_label = None

    transforms_test = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    if request.method == 'POST':
        # in case of POST: get the uploaded image from the form and process it
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # retrieve the uploaded image and convert it to bytes (for PyTorch)
            image = form.cleaned_data['image']
            image_bytes = image.file.read()
            # # convert and pass the image as base64 string to avoid storing it to DB or filesystem
            encoded_img = base64.b64encode(image_bytes).decode('ascii')
            image_uri = 'data:%s;base64,%s' % ('image/jpeg', encoded_img)
            baseUrl = settings.MEDIA_ROOT_URL + settings.MEDIA_URL
            num_features = cnn_model.fc.in_features
            cnn_model.fc = nn.Linear(num_features, 5)

            cnn_model.load_state_dict(torch.load(baseUrl+'cnn_model/cnn.pth'))

            # image = Image.open('./test_image.jpg')
            image = Image.open(image).convert('RGB')
            image = transforms_test(image).unsqueeze(0).to(device)

            # with torch.no_grad():
            with torch.no_grad():
                outputs = cnn_model(image)
                _, preds = torch.max(outputs, 1)
                predicted_label = class_names[preds[0]]
            # get predicted label with previously implemented PyTorch function
            # try:
            #     predicted_label = get_prediction(image_bytes)
            # except RuntimeError as re:
            #     print(re)

    else:
        # in case of GET: simply show the empty form for uploading images
        form = ImageUploadForm()

    # pass the form, image URI, and predicted label to the template to be rendered
    context = {
        'form': form,
        'image_uri': image_uri,
        'predicted_label': predicted_label,
    }
    return render(request, 'image_classification/image_upload.html', context)
