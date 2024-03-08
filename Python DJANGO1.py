#!/usr/bin/env python
# coding: utf-8

# In[ ]:


todo_project/
│
├── todos/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── todo_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── requirements.txt


# In[ ]:


pip install django djangorestframework


# In[ ]:


django-admin startproject todo_project
cd todo_project
django-admin startapp todos


# In[ ]:


from django.db import models

class ToDoItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# In[ ]:


from rest_framework import serializers
from .models import ToDoItem

class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = '__all__'


# In[ ]:


from rest_framework import generics
from .models import ToDoItem
from .serializers import ToDoItemSerializer

class ToDoItemListCreate(generics.ListCreateAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer

class ToDoItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer


# In[ ]:


from django.db import models

class ToDoItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# In[ ]:


from rest_framework import serializers
from .models import ToDoItem

class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = '__all__'


# In[ ]:


from rest_framework import generics
from .models import ToDoItem
from .serializers import ToDoItemSerializer

class ToDoItemListCreate(generics.ListCreateAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer

class ToDoItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer

class ToDoItemMarkComplete(generics.UpdateAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer

    def perform_update(self, serializer):
        serializer.instance.completed = True
        serializer.save()

class ToDoItemSchedule(generics.UpdateAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer

class ToDoItemReschedule(generics.UpdateAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer


# In[ ]:


from django.urls import path
from .views import ToDoItemListCreate, ToDoItemRetrieveUpdateDestroy, ToDoItemMarkComplete, ToDoItemSchedule, ToDoItemReschedule

urlpatterns = [
    path('todos/', ToDoItemListCreate.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', ToDoItemRetrieveUpdateDestroy.as_view(), name='todo-detail'),
    path('todos/<int:pk>/complete/', ToDoItemMarkComplete.as_view(), name='todo-mark-complete'),
    path('todos/<int:pk>/schedule/', ToDoItemSchedule.as_view(), name='todo-schedule'),
    path('todos/<int:pk>/reschedule/', ToDoItemReschedule.as_view(), name='todo-reschedule'),
]


# In[ ]:


from rest_framework import generics
from django.db.models import Q
from datetime import datetime
from .models import ToDoItem
from .serializers import ToDoItemSerializer

class ToDoItemListCreate(generics.ListCreateAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer

class ToDoItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer

class ToDoItemMarkComplete(generics.UpdateAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer

    def perform_update(self, serializer):
        serializer.instance.completed = True
        serializer.save()

class ToDoItemSchedule(generics.UpdateAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer

class ToDoItemReschedule(generics.UpdateAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer

class ToDoItemSearchByTitle(generics.ListAPIView):
    serializer_class = ToDoItemSerializer

    def get_queryset(self):
        title = self.kwargs['title']
        return ToDoItem.objects.filter(title__icontains=title)

class ToDoItemSearchByDate(generics.ListAPIView):
    serializer_class = ToDoItemSerializer

    def get_queryset(self):
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        if start_date and end_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d').replace(hour=23, minute=59, second=59)
            return ToDoItem.objects.filter(due_date__range=[start_date, end_date])
        return ToDoItem.objects.none()


# In[ ]:


from django.urls import path
from .views import ToDoItemListCreate, ToDoItemRetrieveUpdateDestroy, ToDoItemMarkComplete, ToDoItemSchedule, ToDoItemReschedule, ToDoItemSearchByTitle, ToDoItemSearchByDate

urlpatterns = [
    path('todos/', ToDoItemListCreate.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', ToDoItemRetrieveUpdateDestroy.as_view(), name='todo-detail'),
    path('todos/<int:pk>/complete/', ToDoItemMarkComplete.as_view(), name='todo-mark-complete'),
    path('todos/<int:pk>/schedule/', ToDoItemSchedule.as_view(), name='todo-schedule'),
    path('todos/<int:pk>/reschedule/', ToDoItemReschedule.as_view(), name='todo-reschedule'),
    path('searchByTitle/<str:title>/', ToDoItemSearchByTitle.as_view(), name='todo-search-by-title'),
    path('searchByDate/', ToDoItemSearchByDate.as_view(), name='todo-search-by-date'),
]


# In[ ]:





# In[ ]:


# models.py
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    scheduled_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

# serializers.py
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

# views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @action(detail=False, methods=['get'])
    def searchByTitle(self, request):
        title_query = request.query_params.get('title', '')
        todos = Todo.objects.filter(title__icontains=title_query)
        serializer = self.get_serializer(todos, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def searchByDate(self, request):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        if start_date and end_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d') + timedelta(days=1)
            todos = Todo.objects.filter(scheduled_at__range=(start_date, end_date))
            serializer = self.get_serializer(todos, many=True)
            return Response(serializer.data)
        else:
            return Response("Please provide start_date and end_date parameters.")

# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet

router = DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todo')

urlpatterns = [
    path('', include(router.urls)),
]

# settings.py (Add DRF to installed apps)
INSTALLED_APPS = [
    ...
    'rest_framework',
    ...
]


# In[ ]:





# In[ ]:




