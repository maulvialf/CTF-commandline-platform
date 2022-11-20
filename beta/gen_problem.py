import os
import csv

def generate_problem():
	problem = os.listdir("problem")
	file = open("problem_list.csv", "w")
	problem_list   = open("problem_list.csv", "wb")
	write_csv = csv.writer(problem_list, delimiter=',', lineterminator='\n')
	write_csv.writerow(problem)
	problem_list.close()

generate_problem()