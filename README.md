# Plasma : Extract text from image using Tesseract OCR

Aplikasi ini bertujuan untuk mengekstrak teks pada gambar error yang didapatkan pengguna yang nantinya dianalisis menggunakan platform dari Kata.ai.

Demo aplikasi yang telah dipublikasikan menggunakan [Heroku](https://www.heroku.com/) bisa dilihat disini [https://warm-citadel-64062.herokuapp.com/](https://warm-citadel-64062.herokuapp.com/)

## Spesifikasi Aplikasi

Aplikasi ini menggunakan beberapa library python diantaranya
- Framework Django
- Library PyTesseract OCR
- Library Pillow

## Configuring PyTesseract on Heroku

1. Tambahkan heroku-apt-buildpack menggunakan command:

Untuk melihat sumber : [repository](https://github.com/heroku/heroku-buildpack-apt)
```sh
$ heroku buildpacks:add --index 1 heroku-community/apt
```
2. Tambahkan Aptfile ke direktori project
```sh
$ touch Aptfile
```
3. Tambahkan daftar konfigurasi ke Aptfile

tesseract-ocr-eng untuk identifikasi bahasa inggris pada tesseract.

tesseract-ocr-ind untuk identifikasi bahasa indonesia pada tesseract.
```sh
tesseract-ocr
tesseract-ocr-eng
tesseract-ocr-ind
```
4. Cek path untuk mengakses data package tesseract-ocr-eng dan tesseract-ocr-ind

Kita akan menggunakan path tersebut di langkah selanjutnya
```sh
$ heroku run bash
$ find -iname tessdata # this will give us the path we need
```
Kamu dapat keluar dari heroku shell dengan command `exit`
5. Sekarang, atur variabel heroku config bernama TESSDATA_PREFIX dengan path sebelumnya

Biasanya path yang didapatkan seperti ini
```sh
$ heroku config:set TESSDATA_PREFIX=./.apt/usr/share/tesseract-ocr/4.00/tessdata
```
6. Push perubahan ke heroku
```sh
$ git push heroku master
```

Sumber : [Using Tesseract on Heroku with Django](https://stackoverflow.com/questions/19521976/using-tesseract-on-heroku-with-django)


## Configuring PyTesseract on PC (Windows)

1. Install tesseract using windows installer available at: [installer](https://github.com/UB-Mannheim/tesseract/wiki)

2. Note the tesseract path from the installation.Default installation path at the time the time of this edit was: C:\Program Files\Tesseract-OCR. It may change so please check the installation path.

3. pip install pytesseract

4. set the tesseract path in the script before calling image_to_string:
```sh
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```


Source : [Pytesseract : "Tesseract Not Found"](https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i)


## Implementasi Coding pada Heroku

file berada di direktori `chats/views.py`
```sh
from io import BytesIO
from PIL import Image
import requests
import pytesseract

def attachment(request):
    chats = Chat.objects.filter(user = "user", is_sent = 0)

    if chats.count() :
        for chat in chats :
    
            if chat.attachment :
                #disesuaikan dengan path gambar yang akan diekstrak
                response   = requests.get("https://warm-citadel-64062.herokuapp.com" + chat.attachment.url)
                img        = Image.open(BytesIO(response.content))
                transcript = pytesseract.image_to_string(img)
                
                chat.message = transcript
                chat.is_sent = 1
                chat.save()

                return JsonResponse({'transcript' : transcript, 'img_url' : chat.attachment.url})

        return HttpResponse('')
        
    return HttpResponse('')
```

## Implementasi Coding pada Local (PC Windows)

file berada di direktori `chats/views.py`
```sh
from io import BytesIO
from PIL import Image
import requests
import pytesseract

def attachment(request):
    chats = Chat.objects.filter(user = "user", is_sent = 0)

    if chats.count() :
        for chat in chats :

            if chat.attachment :
                #Dibutuhkan untuk mengakses package data tesseract pada server lokal
                pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
                
                response   = requests.get("http://localhost:5000" + chat.attachment.url)
                img        = Image.open(BytesIO(response.content))
                transcript = pytesseract.image_to_string(img)
                
                chat.message = transcript
                chat.is_sent = 1
                chat.save()

                return JsonResponse({'transcript' : transcript, 'img_url' : chat.attachment.url})

        return HttpResponse('')
        
    return HttpResponse('')
```