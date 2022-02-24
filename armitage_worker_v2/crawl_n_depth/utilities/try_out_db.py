# setx AVENTION_PASSWORD "<password>"
import ast
import os
import time
import sys

from azure.storage.queue import QueueClient
from bson import ObjectId
from selenium.webdriver.common.keys import Keys


from os.path import dirname as up

# from armitage.armitage_admin.catalog.dump_projects.db_connect import add_to_simplified_export_queue

three_up = up(up(__file__))
sys.path.insert(0, three_up)

from Simplified_System.Database.db_connect import refer_collection,add_to_simplified_export_queue


# mycol = refer_collection()
# print(mycol.find())
# for i in mycol.find():
#     print(i)