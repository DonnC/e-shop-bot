# handler.py
# handle messages from whatsapp and respond accordingly
import sys
from random import choice
from time import sleep
from datetime import datetime as dtime

# user defined modules
from .credentials import ADMIN_CONTACT, MODERATOR
#from .searchProduct import Search
from .utils import *
from .whatsapp import WhatsApp

class BotHandler:
   '''
      handle all messages from whatsapp for the Bot Engine
   '''
   def __init__(self, body, contact):
      self.body    = body
      self.contact = contact

   def runBotHandler(self):
      # run the Bot Engine handler
      self.parseForCommand()

   def isSatisfied(self):
      # check if command is available in user`s message
      checkPresent = False

      for command in Command():
         if self.body.find(command) == 0:
            checkPresent = True

      return checkPresent

   def restructureText(self, text_list):
      # restructure given text list
      full_text = ""
      for txt in text_list:
         txt = txt.strip()
         full_text += txt + " "

      full_text = full_text.strip()
      return full_text

   def parseForCommand(self):
      # look for commands and make the bot respond to `em
      # you can implement your own parser depending on how you tell your user to send
      # your bot the message, can be e.g airtime,10,263xxxxxxxxx or music NF - One Hundred or weather Bulawayo

      if self.contact == MODERATOR:
         '''
          implement services provided by the moderator
          can add more commands and implement them accordingly in seperate modules
          e.g utils.py to keep the handler clean and short
         '''
         if self.isSatisfied():
            command_ = self.body.split(' ')[0].strip()
            app_resp = self.body.lstrip(command_).strip()
            mod_command  = command_

         mod_command = mod_command.lower()

         if mod_command.startswith('-'):
            logStats(self.contact, mod_command, True)

            if mod_command == '-help':
               WhatsApp(helpDev(), MODERATOR)

            if mod_command == '-subscribed':
               WhatsApp(f"So far there are {len(notifyClients())} subscribed clients", MODERATOR)

            if mod_command == "-feedback":
               msg  = "Feedbacks\n"
               WhatsApp(msg+getFeedback(), MODERATOR)

            if mod_command == "-stats":
               # return statistics of bot
               from .Stats import botStats
               WhatsApp(botStats(), MODERATOR)

            if mod_command == "-notify":
               # notify clients from developer | moderator desktop
               contacts_list = notifyClients()
               notify_msg    = f"Notice*\n{app_resp}"
               if len(contacts_list) > 0:
                  for contact in contacts_list:
                     WhatsApp(notify_msg, contact)

      if self.contact == ADMIN_CONTACT:
         '''
          implement services provided by the admin (person in charge of whatsapp bot and company client services)
          can add more commands and implement them accordingly in seperate modules
          e.g utils.py to keep the handler clean and short
         '''
         if self.isSatisfied():
            command_ = self.body.split(' ')[0].strip()
            app_resp = self.body.lstrip(command_).strip()
            admin_command  = command_

         admin_command = admin_command.lower()

         if admin_command.startswith("#"):
            logStats(self.contact, admin_command, True)

            if admin_command == "#help":
               WhatsApp(helpAdmin(), self.contact)

            if admin_command == "#notify":
               contacts_list = notifyClients()
               notify_msg    = f"<COMPANY-NAME>📢\n{app_resp}"
               if len(contacts_list) > 0:
                  for contact in contacts_list:
                     WhatsApp(notify_msg, contact)

            if admin_command == "#feedback":
               msg  = "Feedbacks\n"
               WhatsApp(msg+getFeedback(), self.contact)

      if self.contact:
         '''
          general client section.
          can add more commands and implement them accordingly in seperate modules
          e.g utils.py to keep the handler clean and short
         '''

         if self.isSatisfied():
            command_ = self.body.split(' ')[0].strip()
            app_resp = self.body.lstrip(command_).strip()
            command  = command_

         command = command.lower() # just in case

         if command in Command():
            logStats(self.contact, command, True)

            if command == "start":
               WhatsApp(helpText(), self.contact)

            if command == "feedback":
               msg = app_resp
               saveFeedback(msg, self.contact)
               WhatsApp("Thank you for writing to us.", self.contact)

            if command == "developer":
               WhatsApp(developerProfile(), self.contact)

            if command == "suggest":
               # TODO: client suggested something, do something
               WhatsApp("Thank you for your suggestion.", self.contact)