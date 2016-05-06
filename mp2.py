from sys import argv

script, filename = argv

class dfa:
	inputs = []
	west = []
	east = []

	def default_values(self):
		self.west = [True, True, True, True]	# C R L N

	def __init__(self, inputs):
		self.inputs = inputs

	def execute(self):
		self.default_values()

		for i in inputs:
			direction = True	# True for left, False for right
			NG = False
			for line in i:
				for letter in line:

					if letter == 'C':
						if direction:
							self.west[0] = False
							self.west[3] = False
						else:
							self.west[0] = True
							self.west[3] = True

					elif letter == 'R':
						if direction:
							self.west[1] = False
							self.west[3] = False
						else:
							self.west[1] = True
							self.west[3] = True

					elif letter == 'L': 
						if direction:
							self.west[2] = False
							self.west[3] = False
						else:
							self.west[2] = True
							self.west[3] = True

					elif letter == 'N':
						if direction:
							self.west[3] = False
						else:
							self.west[3] = True

					direction = not direction

					# NG STATES
					if self.west in [[True,True,True, False],		# carrot , rabbit , lion
									 [True, True, False, False],	# carrot , rabbit
									 [False, True, True, False], 	# rabbit , lion
									 [False, False, True, True],	# lion , man
									 [False, False, False, True],	# man	
									 [True, False, False, True],]:	# carrot , man
						NG = True

			if NG:
				#print "NG"
				outputfile.write("NG\n")
			else:
				#print "OK"
				outputfile.write("OK\n")

			self.default_values()

#inputfile = open('mp2.in')
inputfile = open(filename)
outputfile = open('mp2.out', 'w')

inputs = inputfile.readlines()

river_crossing = dfa(inputs)

print "Writing.."
river_crossing.execute()
print "Output written in 'mp2.out'"
inputfile.close()
outputfile.close()

