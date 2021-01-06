from django.test import TestCase,RequestFactory
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model

from .views import SignUpView
from .models import CustomUser
# Create your tests here.
class movies_crud_test(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            first_name = 'admin',
            last_name= 'admin',
            email = 'admin@gmail.com',
            username='admin',
            password = '123456admin'
        )       
                       
    def test_user_creation(self):
        self.assertEquals(self.user.__str__(),'admin')    

    def test_duplicates(self):
        try:
            self.user2 = get_user_model().objects.create_user(
                first_name = 'joudi',
                last_name= 'awameh',
                email = 'admin@gmail.com',
                username='joudi',
                password = '123456joudi'
            )           
        except:          
            print('Resgistration falied!')

    
    