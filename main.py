
import pandas as pd 
import numpy as np 
import random 
import matplotlib.pyplot as plt


def probability( m1 , m2 ):

	return 0.5 + 0.5*(  (m1 - m2)/(m1+ m2 ) )
class Agent( ):

	def __init__( self , money ):

		self.coin = money 

	def trade( self ,  agent , bet = 10  ):

		r = random.random()
		c1 = self.get_coin()
		c2 = agent.get_coin()
		if  (c1 + c2 ) <= 0 :
			return 
		# I win 
		#print( probability( c1 , c2 ))
		if r <= probability(c1  , c2) :
			
			self.plus_coin( bet )
			agent.minus_coin( bet )
		else:
			self.minus_coin( bet )
			agent.plus_coin( bet )

	def get_coin( self ):

		return self.coin

	def minus_coin( self , loss ):

		self.coin = self.coin - loss

	def plus_coin( self , earn  ):

		self.coin = self.coin + earn 



population = [  Agent(100) for x in range(1000) ]


for k in range(10000):

	traders = random.sample( population , 2 )
	population.remove( traders[0] ) 
	population.remove( traders[1] )

	traders[0].trade( traders[1] )

	population.append( traders[0] )
	population.append( traders[1] )
	if k % 1000 == 0:
		print(k)

	#print(  t )


earns = np.array(  [ x.get_coin() for x in population ] ) 

print("Agentes con perdidas ")
print(  np.where(earns < 100 )[0].size )
print("Agentes muertos - deuda")
print(  np.where(earns < 0 )[0].size )
print( "Agentes con ganancias ") 
print(  np.where(earns > 100 )[0].size )

plt.hist( earns )
plt.show()





