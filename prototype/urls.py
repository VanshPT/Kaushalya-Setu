from django.urls import path
from . import views

urlpatterns = [
    path('', views.roadmap, name="Roadmap Prototype"),
    path('process_prompt/', views.ProcessPromptView.as_view(), name='process_prompt'),
    path('save_prompt/', views.SaveEmitPromptView.as_view(), name="save_prompt"),
    path('get_roadmap/<int:pk>/', views.GetRoadmapView.as_view(), name='get_roadmap'),
    
    path('gen_nodes/', views.gen_nodes, name='gen_nodes'),
]