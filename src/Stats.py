# perfom statistics of bot operations
# @author:  Donald C
# @created: 09 Jan 2020

from os import path, listdir
from .utils import PRO_STATS_DIR, DEV_STATS_DIR

# format of stats
# 29-12-2019_15-32-24: 263778060126, help

def checkDirExist():
   if path.isdir(PRO_STATS_DIR):
   #if path.isdir(DEV_STATS_DIR):
      return True

def perfom_stats(stats_l):
   # received a list of stats data in format above
   stats_nums = []
   stats_comm = []
   stats_requests = 0
   stats_date     = ""

   for line in stats_l:
      if len(line) > 5:
         _date, contact_command = line.split(':')
         stats_date = _date.split('_')[0]
         _contact, _command = contact_command.split(',')
         stats_nums.append(_contact.strip())
         stats_comm.append(_command.strip())
         stats_requests += 1

   # remove duplicates
   contacts = len(set(stats_nums))
   commands = len(set(stats_comm))
   stats_profile = f"All Contacts: {len(stats_nums)}. All Commands: {len(stats_comm)}"

   return stats_profile

def botStats():
   res = ""
   count = 0
   if checkDirExist():
      for prodctn_stats_file in listdir(DEV_STATS_DIR):
         if prodctn_stats_file.endswith(".log"):
            with open(path.join(DEV_STATS_DIR, prodctn_stats_file), encoding='utf-8', errors='ignore') as stats_f:
               stats_list = stats_f.readlines()
               stats_res = perfom_stats(stats_list)
               res += stats_res

         else:
            res = ""

         count += 1

   else:
      res = ""

   if len(res) == 0:
      res = "No stats"

   result = f"Bot stats\n{res.strip()}"
   return result