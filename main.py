# -*- coding: utf-8 -*-
import json
from utils import *
password = ""
users = ""

# to easy for login
# password = "41pjso2krv6sk1wj6936l06yqdpv68r5" # test
# submit = "agrihack{za3tdex5k9d4ocjq25esxm5kabyu876b0zxz6xnthvafm2zmwbf9kotkribgscol}"

	
def header():
	print "\n\n"
	print "-*"*20
	print "Welcome {}".format(users.team_name)
	print "Your score {}".format(users.score)
	print "[v] list problem"
	print "[e] exit"
	print "[s] submit flag"
	print "[p] point scoreboard"
	print "[1] view problem 1"
	print "[2] view problem 2"
	print "[<num>] view problem <num>"
	print "-*"*20
	
	print "\n\n"


def submit_flag():
	flag = raw_input("Input your flag : ")
	# flag = submit
	num = session.query(Submission).filter_by(flag_submit=flag).count()
	prob = session.query(Problem).filter_by(flag_string=flag)
	if(prob.count() == 0):
		print "Invalid flag"
		return 0
	prob = prob.one()
	
	if(prob.id_owner == users.id):
		print "This your flag. You can't submit it"
		return 0
	elif(num != 0):
		print "Flag already submitted"
		return 0
	elif(num == 0):
		user_grabbed = session.query(User).filter_by(id=prob.id_owner).one()
		
		print "Congrats. You steal '{}' Flag for '{}' Problem".format(user_grabbed.team_name, prob.problem_name)

		submitt = Submission(id_user=users.id, flag_submit=flag)
		session.add(submitt)
		
		# add submission
		users.score += 100 * prob.multiplier
		users.final_submission = session.query(Submission).count()
		
		session.add(users)
		session.commit()		


def scoreboard():
	userss  = session.query(User).order_by(User.score.desc(), User.final_submission)
	index = 1
	for user in userss:
		print index, user.team_name, user.score
		index += 1

def view_problem(cmd):
	prob  = session.query(Problem).filter_by(id=int(cmd)).one()
	print prob.description


def list_problem():
	pass

def login():
	global password, users
	password = raw_input("Input your Password: ")
	cond = True
	users = session.query(User).filter_by(password=password).one()

	if(users):
		pass
	else:
		print "Your account is not created. Ask admin"
		sys.exit()

login()
while 1:
	header()
	cmd = raw_input("Input your command >> ")
	if(cmd == "s"):
		submit_flag()
	elif(cmd == "v"):
		list_problem()
	elif(cmd == "e"):
		exit()
	elif(cmd == "p"):
		scoreboard()
	elif(unicode(cmd).isnumeric()):
		view_problem(cmd)