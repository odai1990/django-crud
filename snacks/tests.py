from django.http import response
from django.test import TestCase
from django.urls import reverse
from .models import Snack
from django.contrib.auth import get_user_model
# Create your tests here.

class SnacksTest(TestCase):
    def setUp(self):
        self.user=get_user_model().objects.create_user(
            username='odai',
            email='odai22odai678@gmail.com',
            password='123456'
        )
        self.snack=Snack.objects.create(
            title='Cracker nuts',
            purchaser=self.user,
            description='A snack food produced with peanuts that are coated in a wheat flour dough and then fried or deep-fried'

        )


    def testing_stutas_list_view(self):
        expacted=self.client.get(reverse('snackslist'))
        actual=200       
        self.assertEqual(expacted.status_code, actual)
        self.assertTemplateUsed(expacted, "SnackListView.html")
      
       


    def testing_stutas_add_view(self):    
        response=self.client.post(
            reverse("snackscreate"),
            {
                "title":"Cracker nuts",
                "purchaser":self.user.id,
                "description":"A snack food produced with peanuts that are coated in a wheat flour dough and then fried or deep fried"
            },follow=True
            )
        actual=200
        self.assertEqual(response.status_code,actual)
        
    

    def testing_stutas_detail_view(self):
        response = self.client.get(reverse("snackdetials", args="1"))
        actual=200         
        self.assertEqual(response.status_code, actual)        
        self.assertTemplateUsed(response, "SnackDetailView.html")
    
    def testing_stutas_update_view(self):
        response = self.client.post(
            reverse("snacksupdate", args="1"),
            {
                "title":"Cracker nuts2",
                "purchaser":self.user.id,
                "description":"A snack food produced with peanuts that are coated in a wheat flour dough and then fried or deep fried"
            },follow=True
        )
        actual=reverse("snackslist")
        actual2=200

        self.assertRedirects(response,actual )
        self.assertEqual(response.status_code,actual2 )


    def testing_stutas_delete_view(self):
        response =self.client.post(reverse('snacksdelete',args='1'))
        actual=reverse("snackslist")

        self.assertRedirects(response,actual )