# utils.py
# handles your-bot utilities

from os import path, listdir
from datetime import datetime as dtime, timedelta as tdelta
import logging
from time import sleep

allowLogging      = True

now            = dtime.now()
_time          = now.strftime("%d-%m-%Y")

ROOT_DIR       = path.dirname(__file__)
ROOT_DIR       = path.dirname(ROOT_DIR)
FILES_DIR      = path.join(ROOT_DIR, "files")
RESOURCE_DIR   = path.join(ROOT_DIR, "resource")
DATABASE_DIR   = path.join(ROOT_DIR, "databases")
STATS_DIR      = path.join(ROOT_DIR, "stats")
DEV_STATS_DIR  = path.join(path.abspath(STATS_DIR), 'development')
PRO_STATS_DIR  = path.join(path.abspath(STATS_DIR), 'production')
MODR_LOG_DIR   = path.join(ROOT_DIR, "Logs")          # keep log file for moderator

FOOTER         = "\n\n*YOUR COMPANY MOTO*📡_"  # your org moto e.g "Your #1 stop shop for earthmoving machinery🚩"

# TODO Use CSV or databases files
admin_file         = "admin_help.txt"
help_file          = "help.txt"
dev_file           = "dev_help.txt"
command_file       = "commands.txt"
notify_db          = "notify.txt"
suggested_db       = "suggestedProducts.txt"
feedback_db        = f"feedback_{_time}_.txt"
moderator_file     = f'bot_log_{_time}_.log'

admin_help         = path.join(FILES_DIR, admin_file)
help_general       = path.join(FILES_DIR, help_file)
devlpr_help        = path.join(FILES_DIR, dev_file)
commands           = path.join(FILES_DIR, command_file)
suggested          = path.join(DATABASE_DIR, suggested_db)
feedback           = path.join(DATABASE_DIR, feedback_db)
subscribed_clients = path.join(DATABASE_DIR, notify_db)
moderator_log      = path.join(MODR_LOG_DIR, moderator_file)
prod_f             = path.join(PRO_STATS_DIR, 'prod.log')

if allowLogging:
   if checkFile(moderator_log):
      logging.basicConfig(level=logging.DEBUG, filename=moderator_log, format = '%(asctime)s - %(levelname)s - %(message)s')

   else:
      logging.basicConfig(level=logging.DEBUG, filename=moderator_log, format = '%(asctime)s - %(levelname)s - %(message)s')

def logStats(number, command, prod_env=False):
   # log bot stats
   number = number.strip('whatsapp:+')
   if prod_env:
      # TODO:: log stats during production
      pass

   else:
      # TODO:: log stats during development
      pass

def log(message='', level=0):
   if allowLogging:
      if level == 0:
         logging.debug(message)

      if level == -1:
         logging.error(message)

      if level == 1:
         logging.warning(message)

def developerProfile():
   # show some love 🍻
   profile = "About the bot developer 👨‍💻\n_Developer_: Donn🐾\nFollow 👇\n_On GitHub_: https://github.com/DonnC\n_Whatsapp_: https://wa.me/263778060126"
   return profile

def checkFile(fpath_):
   if path.isfile(fpath_):
      return True

def notifyClients():
   # automatically notify your clients on whatsapp on any notices the admin | moderator provides
   deleteDupNotify()
   contacts = []
   if checkFile(subscribed_clients):
      with open(subscribed_clients, encoding="utf8", errors='ignore') as clients_db:
         db = clients_db.readlines()
         if len(db) > 0:
            db = set(db)  # avoid duplicates
            for number in db:
               if len(number) > 11:
                  num = "whatsapp:+" + number.strip()
                  contacts.append(num)
   return contacts

def saveBackNotify(lines_list):
   # save back clients to notify after a -notify
   lines = ""
   for line in lines_list:
      line = line.strip()
      lines += line + '\n'

   with open(subscribed_clients, 'w', encoding="utf8", errors='ignore') as notfy:
      notfy.writelines(str(lines))
   lines = ""

def subscribe(contact):
   # subscribe a client to your notify list
   deleteDupNotify()
   contact = contact.strip("whatsapp:+")
   if checkFile(subscribed_clients):
      with open(subscribed_clients, 'a+', errors='ignore') as clients_db:
      #with open('../databases/notify.txt', 'a+') as clients_db:
         clients_db.write(f'{contact}\n')

def Command():
   # get your commands in the bot's environment
   commands_ = []
   if checkFile(commands):
      with open(commands, encoding="utf8", errors='ignore') as f:
         command = f.readlines()
         for command_ in command:
            if len(command_) > 3 and not command_.startswith('//'):
               commands_.append(command_.strip())
   return commands_

def saveClientSuggestion(client, client_suggestion):
   # get client suggestions and logs them to file
   if checkFile(suggested):
      _time  = now.strftime("%d-%m-%Y_%H-%M-%S")
      # TODO:: Save | log user suggestion
      pass

def helpAdmin():
   # get admin's help text
   if checkFile(admin_help):
      with open(admin_help, encoding="utf8", errors='ignore') as h:
         help_file = h.read()

      return help_file

def helpText():
   # get general help text for users
   if checkFile(help_general):
      with open(help_general, encoding="utf8", errors='ignore') as hf:
         help_ = hf.read()

      return help_

def helpDev():
   # get help text for developer | moderator
   if checkFile(devlpr_help):
      print("[INFO] Dev helper found")
      with open(devlpr_help, encoding="utf8", errors='ignore') as hf:
         help_dev_ = hf.read()

      return help_dev_

def saveFeedback(body, contact):
   # TODO: Save | log user feedback
   pass

def restruct(bdy):
   txt = ""
   if type(bdy) == list:
      for t in bdy:
         txt += t + " "

      return txt.strip()

   else:
      return bdy

def getFeedback():
   # get all user feedback for the admin | moderator
   fdbacks = ""
   if checkFile(feedback):
      with open(feedback, encoding="utf8", errors='ignore') as fdbck_db:
         data = fdbck_db.readlines()
         if len(data) > 0:
            for fdbck in data:
               all_them = fdbck.split(',')
               fdback  = f"*{all_them[0]}* : {restruct(all_them[1:])}\n"
               fdbacks += fdback

   fdbacks.strip()
   return fdbacks

# handles resources, fileIO on server files
def getAgents():
   agents_ = "<YOUR AGENT DETAILS IF ANY>"
   return agents_

def getAdress():
   adrress = "<YOUR ADDRESSES IF ANY>"
   return adrress

def deleteDupNotify():
   if checkFile(subscribed_clients):
      with open(subscribed_clients, encoding="utf8", errors='ignore') as clients_db:
      #with open('../databases/notify.txt') as clients_db:
         db = clients_db.readlines()
         if len(db) > 0:
            # remove duplicates
            db = set(db)
            nw = list(db)
            saveBackNotify(nw)

def getModLog():
   # TODO: send log file to moderator
   # TODO: get number of the moder log files
   numLogs = 0
   return numLogs

# --------------------- test -------------------------
#logStats("whatsapp:+263778060126", "-logs", True)