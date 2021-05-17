from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from register.views import add_view,del_user,update_user


urlpatterns=[
    path('',add_view,name="addview"),
    path('delete/<int:id>/',del_user,name="deluser"),
    path('update/<int:id>/',update_user,name="updateuser")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

