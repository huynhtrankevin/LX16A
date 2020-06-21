from LX16A import LX16A

MOTOR_PAN_ID = 1
MOTOR_TILT_ID = 2

# instantiate a controller
lx16 = LX16A()

# set the motor ID
'''
You need to set the ID's one at a time (only 1 plugged in at a time)
Once the ID's have been set, comment out these lines (the motor seems to have problems with continuous reassignment)
'''
#lx16.setID(LX16A.BROADCAST_ID, MOTOR_PAN_ID)
#lx16.setID(LX16A.BROADCAST_ID, MOTOR_TILT_ID)

'''
position: 0-240 degrees
rate: 0-30000 ms (this is the duration over which the change in position is acheived... i.e. 1ms = get there in 1ms)
'''
lx16.moveServo(id=MOTOR_PAN_ID,position=180,rate=1000)

pos = lx16.readPosition(id=MOTOR_PAN_ID)*240/1000
voltage = lx16.readVoltage(id=MOTOR_PAN_ID)
temp = lx16.readTemperature(id=MOTOR_PAN_ID)
print('Position: ', pos)
print('Temperature (C): ',temp)
print('Voltage (mv): ', voltage)