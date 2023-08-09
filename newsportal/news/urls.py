from django.urls import path
from .views import NewsList, NewsDetail, NewsCreate, NewsUpdate, NewsDelete

urlpatterns = [
   path('', NewsList.as_view()),
   path('<int:pk>', NewsDetail.as_view(), name='news'),
   path('create/', NewsCreate.as_view()),
   path('<int:pk>/update/', NewsUpdate.as_view()),
   path('<int:pk>/delete/', NewsDelete.as_view()),
]
