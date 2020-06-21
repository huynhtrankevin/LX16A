from LX16A import LX16A

MOTOR_PAN_ID = 1
MOTOR_TILT_ID = 2

# instantiate a controller
lx16 = LX16A()

# set ID
'''
You need to set the ID's one at a time (only 1 plugged in at a time)
Once the ID's have been set, comment out these lines (the motor seems to have problems with continuous reassignment)
'''
lx16.setID(LX16A.BROADCAST_ID, MOTOR_TILT_ID)

# set angle limits
lx16.setAngleLimit(id=MOTOR_TILT_ID,angleMin=60,angleMax=240)


