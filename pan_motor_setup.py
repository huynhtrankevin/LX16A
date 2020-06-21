from LX16A import LX16A

MOTOR_PAN_ID = 1
MOTOR_TILT_ID = 2

# instantiate a controller
lx16 = LX16A()

# set ID
lx16.setID(LX16A.BROADCAST_ID, MOTOR_PAN_ID)
#lx16.setAngleLimit(id=MOTOR_TILT_ID,angleMin=60,angleMax=240)



