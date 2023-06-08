from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('news/', news, name='news'),
    path('employment/', employment, name='employment'),
    path('add_employment/', add_employment, name='add_employment'),
    path('employment/delete/<int:id>', delete, name='delete'),
    path('employment/update/<int:pk>', EmploymentUpdateView.as_view(), name='update'),
    path('employment/download', render_pdf_view, name='download'),
    path('consultation/', index, name="consultation"),
    path('news/<slug:slug>', news_detail, name='news_detail'),
    path('accounts/signup/', signup, name='account_signup'),
    path('accounts/signup_place/', signup_place, name='account_signup_place'),
    path('accounts/login/', account_login, name='account_login'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
]
