"""
URL configuration for htmxpress_demoapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from codecs import encode
from base64 import b64encode
import python_avatars as pa
from cairosvg import svg2png

from faker import Faker

api = NinjaAPI()


@api.get("/rot13")
# TODO validation?, delayed jobs for polling
def rot13(request, text: str):
    return {"result": encode(text, 'rot13')}


@api.get("/random")
# TODO respond with randomized (same format) data
def add(request):
    return {"result": a + b}

@api.get("/avatar")
def avatar(request):
    random_avatar = pa.Avatar.random()
    random_avatar.render('avatar.svg')
    svg2png(url='avatar.svg', write_to='avatar.png', output_width=250, output_height=250)
    with open('avatar.png', 'rb') as image_file:
         encoded_image = b64encode(image_file.read()).decode('utf-8')
    return {"avatar_png_b64": encoded_image}

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]
