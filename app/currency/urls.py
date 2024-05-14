from currency.views import (
    ContactUSCreateView,
    RateCreateView,
    RateDeleteView,
    RateDetailView,
    RateListView,
    RateUpdateView,
    SourceCreateView,
    SourceDeleteView,
    SourceDetailView,
    SourceListView,
    SourceUpdateView,
    )

from django.urls import path

app_name = 'currency'

urlpatterns = [
    path('rate/list/', RateListView.as_view(), name='rate-list'),
    path('rate/details/<int:pk>/', RateDetailView.as_view(), name='rate-details'),
    path('source/list/', SourceListView.as_view(), name='source-list'),
    path('source/details/<int:pk>/', SourceDetailView.as_view(), name='source-details'),
    path('rate/create/', RateCreateView.as_view(), name='rate-create'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),
    path('contact_us/create/', ContactUSCreateView.as_view(), name='contact-us-create'),
    path('source/create/', SourceCreateView.as_view(), name='source-create'),
    path('source/update/<int:pk>/', SourceUpdateView.as_view(), name='source-update'),
    path('source/delete/<int:pk>/', SourceDeleteView.as_view(), name='source-delete'),
]
