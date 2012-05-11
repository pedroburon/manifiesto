from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from signers.models import Signer


class SignerModelTest(TestCase):
    def test_create(self):
        # Arrange
        user = User.objects.create_user(username='doe',
                                        password='secret',
                                        email='joe@doe.net')
        country = 1
        message = 'Lorem ipsum'
        subscribed = True

        # Act
        signer = Signer.objects.create(user=user, country=country,
                                       message=message,
                                       subscribed=subscribed)
        
        # Assert
        self.assertIsInstance(signer, Signer)
        self.assertIsNotNone(signer.pk)
        self.assertEqual(user, signer.user)
        self.assertEqual(country, signer.country)
        self.assertEqual(message, signer.message)
        self.assertEqual(subscribed, signer.subscribed)


class SignerListViewTest(TestCase):
    fixtures = ['test_users']
    def setUp(self):
        self.url = reverse('signer_list')

    def test_get_list_empty(self):
        response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)
        self.assertTrue('signer_list' in response.context)
        self.assertEqual(0, response.context['signer_list'].count())
        self.assertTrue('is_paginated' in response.context)
        self.assertFalse(response.context['is_paginated'])

    def test_get_list_not_empty_but_not_paginated(self):
        user = User.objects.get(pk=1)
        country = 1
        message = 'Lorem ipsum'
        subscribed = True
        signer = Signer.objects.create(user=user, country=country,
                                       message=message,
                                       subscribed=subscribed)
        
        response = self.client.get(self.url)
        
        self.assertEqual(200, response.status_code)
        self.assertTrue('signer_list' in response.context)
        self.assertEqual(1, response.context['signer_list'].count())
        self.assertTrue('is_paginated' in response.context)
        self.assertFalse(response.context['is_paginated'])
        self.assertEqual(response.context['signer_list'][0], signer)

        self.assertContains(response, user.get_full_name())
        
        
        
