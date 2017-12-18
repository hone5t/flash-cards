from django.test import TestCase
from django.conf import settings

from .models import *
from api.models import User

class TestCard(TestCase):
  def setUp(self):
    self.user = User.objects.create(
      first_name = 'sam',
      email = 'sam@test.com',
      password = '123123123'
    )
    self.card = Card.objects.create(
      front = 'test card',
      back = 'details of this card',
      category = 'general',
      known = False,
      owner = self.user
    )


  def tearDown(self):
    pass

  def test_can_add_card(self):
    first_card = Card.objects.get(pk = 1)
    self.assertEqual(1, Card.objects.count())
    self.assertEqual(first_card.front, self.card.front)
    self.assertEqual(first_card.back, self.card.back)
    self.assertEqual(first_card.known, self.card.known)
    self.assertEqual(first_card.owner, self.card.owner)

  def test_can_edit_card(self):
    fail('unimplemented test')

  def test_can_see_his_card(self):
    fail('unimplemented test')



