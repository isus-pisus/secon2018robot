import RPi.GPIO as GPIO
from datetime import datetime

INPUT_WIRE = 18
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(INPUT_WIRE, GPIO.IN)


def get_ir_code():
	value = 1
	# Loop until we read a 0
	while value:
		value = GPIO.input(INPUT_WIRE)

	startTime = datetime.now()

	# Used to buffer the command pulses
	command = []

	# The end of the "command" happens when we read more than
	# a certain number of 1s (1 is off for my IR receiver)
	numOnes = 0

	# Used to keep track of transitions from 1 to 0
	previousVal = 0

	while True:

		if value != previousVal:
			# The value has changed, so calculate the length of this run
			now = datetime.now()
			pulseLength = now - startTime
			startTime = now

			if previousVal == 1:
				command.append((previousVal, pulseLength.microseconds))

		if value:
			numOnes = numOnes + 1
		else:
			numOnes = 0

		if numOnes > 10000:
			break

		previousVal = value
		value = GPIO.input(INPUT_WIRE)

	last_eight = command[len(command)-8:]
	for x in range(0, len(last_eight)):
		if last_eight[x][1] > 1000:
			last_eight[x] = 1
		else:
			last_eight[x] = 0

	return last_eight
