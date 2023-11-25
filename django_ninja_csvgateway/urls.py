"""
URL configuration for django_ninja_csvgateway project.

"""
from django.contrib import admin
from django.urls import path
from django.http import FileResponse, HttpResponse
from ninja import NinjaAPI, File
from ninja.security import HttpBearer
from ninja.files import UploadedFile
import os


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        if token == "supersecret":
            return token


api = NinjaAPI(auth=AuthBearer())  # global bearer authentication
UPLOADPATH = 'uploads/'


@api.post('/upload')
def upload(request, file: File[UploadedFile]):
    data = file.read()
    # write data into file with same name as it was sent
    with open(UPLOADPATH + file.name, 'wb') as f:
        f.write(data)

    return {'name': file.name, 'len': len(data)}


@api.get('/download')
def download(request, file: str):

    if not os.path.exists(UPLOADPATH + file):
        return HttpResponse(status=404) 

    return FileResponse(open(UPLOADPATH + file, 'rb'))


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]
