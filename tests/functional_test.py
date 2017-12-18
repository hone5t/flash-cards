from django.test import LiveServerTestCase

class FunctionalTest(LiveServerTestCase):
  def test_creating_card(self):
    """
    sam visit the flash card app 
    sam werent logged in so he get redirected
    to login page 
    """

    """
    once logged in sam see a card
    with the front of the card shown
    """

    """
    sam can click on the card to flip it and see
    the back of the card once he read the back of the card
    he click it again to see the front
    """

    """
    after reading the card sam click to see the next one
    """

    """
    the card was familir so sam marked it as known
    once sam marked this card as known new card appear in the screen
    the prvious card now stored in the known category
    and sam can see it again if he visit the known page
    """

    """
    sam decided to delete a card
    he click on delete button then a confirmation message appear
    he confirm and the card gone
    then new cards appear
    """

    """
    sam didnt like the info in the new card so he decide to edit it
    he click on the edit button 
    a new window appear 
    that have a text for fron,back,category
    he edit it and hit save
    and see that the card info edited and saved to db
    """
    self.fail('incomplete test')