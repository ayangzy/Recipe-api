from cgi import test
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_emai_successful(self):
        """Test that create user if email is successful"""
        email = "johndoe@gmail.com"
        password = "test123"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test that can normalize user email to lower"""

        email = 'hellWORD@gmail.com'

        user = get_user_model().objects.create_user(email, '23345')
        self.assertTrue(user.email, email.lower())
        #self.assertEqual(user.email, email.lower())
