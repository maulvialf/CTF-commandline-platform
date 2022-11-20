#Configuration  
  
import sys  
  
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import relationship  
from sqlalchemy import create_engine  
  
Base = declarative_base() # Creating an instance of declarative_base() in order for our class to inherit all the features of sqlalchemy  


# Class  
class User(Base): 
	__tablename__ = 'user'  
	id = Column( Integer, primary_key = True)
	team_name = Column(String(100), nullable = False) 
	password = Column(String(100), nullable = False)  
	email = Column(String(100))
	# score = Column( Integer)
	final_submission = Column(Integer)
	
class Problem(Base):  

	__tablename__ = 'problem'  
	id = Column(Integer, primary_key = True)  
	id_owner	  = Column(Integer,     nullable=False)
	problem_name  = Column(String(100), nullable=False)  	
	flag_string   = Column(String(100), nullable=False)  
	multiplier    = Column(Float(20),   nullable=False) 
	base_score    = Column(Float(20),   nullable=False) 
	description   = Column(String(100))  

class Submission(Base):  
	__tablename__ = 'submission'  
	id  			= Column(Integer, primary_key = True)  
	id_user			= Column(Integer)  
	flag_submit		= Column(String(100))  	
	flag_owner_id	= Column(String(100))  	

engine = create_engine('sqlite:///cmd_ad.db')  
Base.metadata.create_all(engine) # This will create new tables inside the database  