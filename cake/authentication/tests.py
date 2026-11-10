from django.core import mail
from django.test import TestCase, override_settings
from rest_framework.test import APIClient


class RegisterViewTests(TestCase):
    @override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
    def test_registration_sends_welcome_email(self):
        response = APIClient().post(
            '/register/',
            {
                'username': 'newuser@mailinator.com',
                'first_name': 'New User',
                'role': 'User',
                'password': 'SafePassword123!',
            },
            format='json',
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, ['newuser@mailinator.com'])
        self.assertIn('Hello New User', mail.outbox[0].alternatives[0][0])
