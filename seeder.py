from utils import *
def create_account():
	team_name = [
	"team1",
	"team2",
	"team3"
	]

	for name in team_name:
		password = gen_rand(32)
		acc = User(team_name = name, password=password, score=0, final_submission=0)
		print name, password
		session.add(acc)
		session.commit()

def create_problem():
	problems = os.listdir("problem")
	users = session.query(User).all()

	for user in users:
		for problem in problems:
			flag = gen_flag()
			description = open("problem/%s/desc" % (problem)).read()

			print user.id,problem, flag, description
			prob = Problem(
				id_owner = user.id, 
				problem_name = problem, 
				flag_string=flag,
				multiplier=1,
				description=description
				)
			session.add(prob)
			session.commit()

remove("cmd_ad.db")
# Base.metadata.create_all(engine) # This will create new tables inside the database  
create_account()
create_problem()