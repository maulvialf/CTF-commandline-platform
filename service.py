from utils import *


problems = os.listdir("problem")

def deploy():
	for prob in problems:
		os.chdir("%s/problem/%s" % (curdir, prob))
		# print os.getcwd()
		

deploy()
# print problems