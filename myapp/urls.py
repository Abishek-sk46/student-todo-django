from django.contrib import admin
from django.urls import path, include  # ✅ Import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('student_details.urls')), 
    path('todo', include('todo_app.urls')),  # ✅ Correct way to include student_details URLs
]