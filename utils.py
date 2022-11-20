import os
import random
import string
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import *

# uncomment seed to debug
random.seed(0)
def gen_rand(N):
	return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(N))

def gen_flag():
	return "agrihack{" + gen_rand(64) + "}"



engine = create_engine('sqlite:///cmd_ad.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
curdir = os.getcwd()