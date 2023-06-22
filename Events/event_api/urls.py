# from django.urls import path
# from .views import EventListView, EventDetailView

# urlpatterns = [
#     # path('events', views.get_latest_events, name='get_latest_events'),
#     # path('events/<int:event_id>', views.get_event_by_id, name='get_event_by_id'),
#     # path('events', views.create_event, name='create_event'),
#     # path('events/<int:event_id>', views.update_event, name='update_event'),
#     # path('events/<int:event_id>', views.delete_event, name='delete_event'),
#     path('events', EventListView.as_view(), name='event_list'),
#     path('events/<int:event_id>', EventDetailView.as_view(), name='event_detail'),
# ]
