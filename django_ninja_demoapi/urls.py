"""
URL configuration for django_ninja_demoapi project.

"""
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from codecs import encode
from base64 import b64encode
import python_avatars as pa
from cairosvg import svg2png

from faker import Faker
fake = Faker()

api = NinjaAPI()
print("Explore endpoints defined in `django_ninja_demoapi/urls.py` via interactive OpenAPI/Swagger UI http://127.0.0.1:8000/api/docs")

@api.get("/rot13")
# TODO validation?, delayed jobs for polling
def rot13(request, text: str):
    return {"result": encode(text, 'rot13')}

@api.get("/random")
# TODO respond with randomized (same format) data
def random(request):
    return {"result": fake.text()}

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
