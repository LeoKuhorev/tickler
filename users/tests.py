# from django.test import TestCase, Client
# from django.contrib.auth import get_user_model
# from .models import UserManager 
# from django.urls import reverse 
# class BasicTest(TestCase):
#     def test_assert(self):
#         self.assertEqual(True,True)
# #

# class TestUrl(TestCase):
#     def setUp(self):
#         #create a user in temp db
#         #provide username and pass
#         #post same email and password to login
#         #should return 200 code  
        

#     def test_login_url(self):
#         response = self.client.get(reverse('token_obtain_pair'))
#         self.assertEqual(response.status_code, 200)

#     def test_token_url(self):
#         response = self.client.get(reverse('token_refresh'))
#         self.assertEqual(response.status_code, 200)


#     def test_profile_url(self):
#         response = self.client.get(reverse('profile'))
#         self.assertEqual(response.status_code, 200)