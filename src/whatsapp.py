# interact with whatsapp from this file
from twilio.rest import Client

from .credentials import AUTH_TOKEN, WHATSAPP_TO, WHATSAPP_FROM, ACC_SID, ADMIN_CONTACT
from .utils import log

class WhatsApp:
   '''
      handle all whatsapp functions
      can implement other whatsapp APIs from here
      in order to maintain code in other files and avoid code breaks
   '''
   TWILIO_CLIENT = Client(ACC_SID, AUTH_TOKEN)

   def __init__(self, body, to_, media=None):
      self.body  = body
      self.to_   = to_
      self.media = media
      self.twilio_send_msg()
      #self.other_app_api()       # call other api logic

   def twilio_send_msg(self):
      # twilio whatsapp api logic
      message = self.body.strip()

      if not self.to_.startswith('whatsapp:'):
         self.to_ = "whatsapp:+" + self.to_

      if self.media:
         try:
            resp = self.TWILIO_CLIENT.messages.create(body=message, from_=WHATSAPP_FROM, to=self.to_, media_url=self.media)
            # log(f"Message with media send: {resp} | media_file: {self.media}")

         except Exception as e:
            log(f"Twilio send media error: {e}", -1)

      else:
         try:
            resp = self.TWILIO_CLIENT.messages.create(body=message, from_=WHATSAPP_FROM, to=self.to_)
            # log(f"App Message sent: {resp}")

         except  Exception as error:
            log(f"Error send App msg: {error}", -1)

   def other_app_api(self):
      # logic of any other whatsapp APIs
      pass
