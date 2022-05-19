from django.test import TestCase
from django.contrib.auth import get_user_model


class TestAccount(TestCase):
    def test_create_user(self):
        user = get_user_model().objects.create_user(
            username = 'mohammad',
            email = 'mohammad@yahoo.com',
            password = 'Abc461379285',
        )
        self.assertEqual(user.username, 'mohammad')
        self.assertEqual(user.email, 'mohammad@yahoo.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(
            username = 'mat',
            email = 'mat@yahoo.com',
            password = 'Xbc461379285',
        )
        self.assertEqual(user.username, 'mat')
        self.assertEqual(user.email, 'mat@yahoo.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)