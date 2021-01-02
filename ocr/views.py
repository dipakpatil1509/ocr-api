import requests
from django.http import JsonResponse
from PIL import Image
from io import BytesIO
import pytesseract
from django.views.decorators.csrf import csrf_exempt

pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'

@csrf_exempt
def imageToText(request):
    if request.method == 'POST':
        try:
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            text = pytesseract.image_to_string(img)

            result = {'text': text}

            return JsonResponse(result)
        except expression as identifier:
            return JsonResponse({'errorCode':404, 'error': 'Something went wrong. Please check url'})
        
    text = "Hello there, this api only supports post methods....\n POST ocr/ \n body:{\n url: <image url>"

    return JsonResponse({'error': text})
