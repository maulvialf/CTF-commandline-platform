import random
import sys
import string
import csv

def gen_rand(N):
	return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(N))

def gen_flag():
	return "agrihack{" + gen_rand(64) + "}"

def read_problem():
	problem = open("../problem_list.csv").read()
	problem = problem.split(",")
	problem[-1] = problem[-1].strip()
	return problem

def read_team():
	ceesve = open("../account.csv")
	spamreader = csv.reader(ceesve, delimiter=',')
	team = []
	line = 0
	for i in (spamreader):
		line += 1
		if(line == 1):
			continue
		team.append(i[0])

	return team



problem = read_problem()
team = read_team()
print team

sys.exit()
flag_table = [["none" for i in range(len(problem) + 1)] for i in range(len(team))]



label = [
"team_name",
]


for prob in problem:
	label.append("flag_"+prob)



def isitabel():
	flag_table[0] = label
	for ind in range(1, len(team)):
		print team[ind]   #, [gen_flag() for i in range(len(problem))]

isitabel()
print flag_table
