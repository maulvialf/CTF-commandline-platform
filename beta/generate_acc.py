import random
import string
import csv

def gen_rand(N):
	return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(N))

def create_account():
	account_csv   = open("account.csv", "wb")
	write_acc_csv = csv.writer(account_csv, delimiter=',', lineterminator='\n')

	label = ["Team name", "Password"]

	write_acc_csv.writerow(label)

	team_name = [
	"team1",
	"team2",
	"team3"
	]

	for name in team_name:
		password = gen_rand(32)
		arr_account = [
			name,
			password
		]

		write_acc_csv.writerow(arr_account)

	account_csv.close()

create_account()