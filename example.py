from LX16A import LX16A

MOTOR_PAN_ID = 1
MOTOR_TILT_ID = 2

# instantiate a controller
lx16 = LX16A()


'''
position: 0-240 degrees
rate: 0-30000 ms (this is the duration over which the change in position is acheived... i.e. 1ms = get there in 1ms)

home: 120 degrees is the neutral position for both motors
pan: the deviation from home for the pan motor (range is +/- 120)
tilt: the deviation from home for the tilt motor (range is [-60,120])
'''
home = 120
pan = 40
tilt = 40
lx16.moveServo(id=MOTOR_PAN_ID,position=(home+pan),rate=1000)
lx16.moveServo(id=MOTOR_TILT_ID,position=(home+tilt),rate=1000) # 60-240 degrees only

'''
Rescale the position information to get it into degrees
'''
pos = lx16.readPosition(id=MOTOR_TILT_ID)*240/1000
voltage = lx16.readVoltage(id=MOTOR_PAN_ID)
temp = lx16.readTemperature(id=MOTOR_PAN_ID)
print('Position: ', pos)
print('Temperature (C): ',temp)
print('Voltage (mv): ', voltage)