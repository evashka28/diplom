from django.urls import path, include

from appointment.views import appointment_request, get_available_slots_ajax, get_next_available_date_ajax, \
    appointment_request_submit, appointment_client_information, default_thank_you

app_name = 'appointment'
from django.urls import path, include


ajax_urlpatterns = [
    path('available_slots/', get_available_slots_ajax, name='available_slots_ajax'),
    path('request_next_available_slot/<int:service_id>/', get_next_available_date_ajax,
         name='request_next_available_slot'),
]

urlpatterns = [
    # homepage

    path('request/<int:service_id>/', appointment_request, name='appointment_request'),
    path('request-submit/', appointment_request_submit, name='appointment_request_submit'),
    path('client-info/<int:appointment_request_id>/<str:id_request>/', appointment_client_information,
         name='appointment_client_information'),
    path('thank-you/<int:appointment_id>/', default_thank_you, name='default_thank_you'),
    path('ajax/', include(ajax_urlpatterns)),
]
