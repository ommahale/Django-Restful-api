from base.views import index,people_data,PersonAPI,PeopleViewSet
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'viewset',PeopleViewSet,basename='viewset')

urlpatterns=[
    path('',include(router.urls)),
    path('index/',index),
    path('people/',people_data),
    path('person/',PersonAPI.as_view())

]