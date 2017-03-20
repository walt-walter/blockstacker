#!/usr/bin/python

#################################################################################
#	
#	AdventureProjects coding sample based on:
#	https://github.com/AdventureProjects/EngInterview
#
#	John Walter
#	gearslap@gmail.com
#	801-319-5747
#	https://www.mountainproject.com/u/jtwalter//105837334
#
#################################################################################

import sys

app_name = 'RoboStacker'

# list of recognized commands
allowed_commands = ['quit','size','add','mv','rm','replay','undo','help', 'exit']

# list to store commands
commands = []

# Stacker class
class Stacker:
	def __init__(self):

		#initialize slots property
		self.slots = []

	'''
		resizes the Slacker.slots list.
		params: int num - number of slots in Slacker.slots
	'''
	def size(self, num):
		num_slots = len(self.slots)
		if (num_slots < num):
			for i in range(0, num - num_slots):
				self.slots.append(0)
		elif num_slots == num:
			# do nothing
			return
		else:
			difference = num_slots - num
			self.slots = self.slots[:-difference]

	'''
		print the slots diagram
	'''
	def print_slots(self):
		# global commands
		for i in range(0, len(self.slots)):
			print str(i+1) + ': ' + ('X'*self.slots[i])
		# print commands
		print "\n"


	'''
		add value to a given slot
		params: int num - the number of slot to add b;ock
	'''
	def add(self, num):
		if (int(num) > len(self.slots)):
			print "there are only " + str(len(self.slots)) + ' slots'
		else:
			self.slots[int(num)-1] += 1

	'''
		removes block from slot
		params:	int num1 - slot to remove block from
	'''
	def rm(self, num):
		if (int(num) > len(self.slots)):
			print "there are only " + str(len(self.slots)) + ' slots'
		else:
			if self.slots[num-1] > 0:
				self.slots[int(num)-1] -= 1

	'''
		moves block from slot to slot
		params:	int num1 - slot to move block from
				int num2 - slot to move block to
	'''
	def mv(self, num1, num2):
		if (num1 > len(self.slots)) or (num2 > len(self.slots)):
			print "there are only " + str(len(self.slots)) + ' slots'
		else:
			if self.slots[num1-1] > 0:
				self.rm(num1)
				self.add(num2)

'''
	Functions
'''


def exit_stacker():
	print 'Exiting ' + app_name
	exit()

'''
	Output help commands
'''
def usage():
	print "\tsize [n]:\t\tAdjusts the number of slots."
	print "\tadd [slot]:\t\tAdds a block to the specified slot."
	print "\tmv [slot1] [slot2]:\tMoves a block from slot1 to slot2."
	print "\trm [slot]:\t\tRemoves a block from the slot."
	print "\treplay [n]:\t\tReplays the last n commands."
	print "\tundo [n]:\t\tUndo the last n commands."

'''
	Method to execute commands 
	useful for sending commands through same process
'''
def execute_command(cmd):
	global commands
	cmd_arr = cmd.split(' ')
	if (cmd_arr[0] != 'size') and (len(stacker.slots) < 1):
		print "You must define a slot size first: size [n]"
	else:
		if cmd_arr[0] == 'size':
			stacker.size(int(cmd_arr[1]))

		if cmd_arr[0] == 'add':
			stacker.add(int(cmd_arr[1]))

		if cmd_arr[0] == 'rm':
			stacker.rm(int(cmd_arr[1]))

		if cmd_arr[0] == 'mv':
			stacker.mv(int(cmd_arr[1]),int(cmd_arr[2]))

		stacker.print_slots()	
		


'''
	Main program
'''

# initiate Stacker object
stacker = Stacker()
print "Welcome to " + app_name + ". Type 'size [n]' to init (type 'help' for a list of commands)"
while True:
	line = raw_input()
	line = line.strip()
	#print "input data: %s" % line

	# split the command on space
	cmd_arr = line.split(' ')

	# administrative commands
	if cmd_arr[0] == 'stacker.count':
		print len(stacker.slots)

	if (cmd_arr[0] == 'quit') or (cmd_arr[0] == 'exit'):
		exit_stacker()

	if cmd_arr[0] == 'help':
		usage()
		continue

	if cmd_arr[0] == 'commands':
		print commands

	# check to see if command in allowed_commands
	if cmd_arr[0] not in allowed_commands:
		print line + " is not a recognized command. Type 'help' to get a list of commands"
	else:
		if len(cmd_arr) > 1:
			# check to see if second argument is an int
			try:
				num = int(cmd_arr[1])
			except ValueError:
				print "You must provide an integer as the argument for your commands"
				continue

			# only store these commands in the commands list
			# send commands through the execute_commands function
			if cmd_arr[0] in ['size', 'add', 'rm', 'mv']:
				execute_command(line)
				commands.insert(0,line)

			# if undo execute the reverse of each command
			if cmd_arr[0] == 'undo':

				if len(commands) < num:
					print 'there are only ' + str(len(commands)) + ' commands stored in memory'
				else:
					for i in range(0, num):
						tmp_arr = commands[i].split(' ')
						if tmp_arr[0] == 'mv':
							stacker.mv(int(tmp[2]), int(tmp_arr[1]))
						elif tmp_arr[0] == 'add':
							stacker.rm(int(tmp_arr[1]))
						elif tmp_arr[0] == 'rm':
							stacker.add(int(tmp_arr[1]))
						elif tmp_arr[0] == 'size':
							stacker.size(int(-tmp_arr[1]))
					stacker.print_slots()

			# replay commands
			if cmd_arr[0] == 'replay':

				if len(commands) < num:
					print 'there are only ' + str(len(commands)) + ' commands stored in memory'
				else:
					for i in range(0, num):
						execute_command(commands[i])
					stacker.print_slots()
		else:
			print "You must provide an integer as the argument for your commans"
			continue
