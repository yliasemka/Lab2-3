from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views
from .views import (
    BaseView,
    #ProductDetailView,
    ServiceDetailView,
    #CartView,
    AddToCartView,
    DeleteFromCartView,
    ChangeQTYView,
    CheckoutView,
    MakeOrderView,
    #LoginView,
    #RegistrationView,
    ProfileView,
    product_detail,
    ContactsView,
    NewsView,
    AboutView,
    SertificateView,
    VacanciesView,
    PolicyView,
    DirectoryView,
    ReviewAnswerView,
    LeaveReviewView,
    TestView,
)


urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('products/<str:slug>/', product_detail, name='product_detail'),
    path('service/<int:id>/', ServiceDetailView.as_view(), name='service_detail'),
    #path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<str:slug>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<str:slug>/', DeleteFromCartView.as_view(), name='delete_from_cart'),
    path('change-qty/<str:slug>/', ChangeQTYView.as_view(), name='change_qty'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('make-order/', MakeOrderView.as_view(), name='make_order'),
    #path('login/', LoginView.as_view(), name='login'),
    #path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    #path('registration/', RegistrationView.as_view(), name='registration'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('news/', NewsView.as_view(), name='news'),
    path('about/', AboutView.as_view(), name='about'),
    path('sertificate/', SertificateView.as_view(), name='sertificate'),
    path('vacancies/', VacanciesView.as_view(), name='vacancies'),
    path('policy/', PolicyView.as_view(), name='policy'),
    path('directory/', DirectoryView.as_view(), name='directory'),
    path('review_answer/', ReviewAnswerView.as_view(), name='review_answer'),
    path('leave_review/', LeaveReviewView.as_view(), name='leave_review'),
    path('test/', TestView.as_view(), name='test'),

]
