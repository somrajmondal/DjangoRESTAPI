#
# from django.contrib import admin
# from django.urls import path
# from student import views
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('stuinfo/<int:pk>', views.student_detail),
#     path('stuinfo/<int:pk>', views.student_list),
# ]
from django.contrib import admin
from django.urls import path
from student.views import *
from django.conf import settings
from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('books/', LCBookAPI.as_view()),
#     path('books/<int:pk>/', RUSBookAPI.as_view()),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', BookAPI.as_view()),
    path('books/<int:pk>/', BookAPI.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
