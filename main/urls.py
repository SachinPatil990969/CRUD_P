from django.urls import path
from .views import item_list_view, add_item_view, item_details_view, item_edit_view, item_delete_view

urlpatterns = [
    path('', item_list_view, name='item_list_view'),
    path('item', add_item_view, name='add_item_view'),
    path('item/<int:pk>/', item_details_view, name='item_details_view'),
    path('item/<int:pk>/edit/', item_edit_view, name ='item_edit_view'),
    path('item/<int:pk>/delete/', item_delete_view, name='item_delete_view'),
]
