import Adafruit_PCA9685

class ServoMotor:

    def __init__(self, Channel, ZeroOffset):
        self.mChannel = Channel
        self.m_ZeroOffset = ZeroOffset

        #initialize PCA9685
        self.mPwm = Adafruit_PCA9685.PCA9685(address=0x40) 
        self.mPwm.set_pwm_freq(60) # 60Hz

    def setAngle(self, angle):
        pulse = int((650-150)*angle/180+150+self.m_ZeroOffset)
        self.mPwm.set_pwm(self.mChannel, 0, pulse)

    def cleanup(self):
        self.setAngle(10)
        
def servo_start_1(se_num1,se_num2,se_num3,se_num4):
                  #,se_num4,se_num5,se_num6):
    servoMotors = []

    servoMotors.append(ServoMotor(Channel=0, ZeroOffset=0))
    servoMotors.append(ServoMotor(Channel=3, ZeroOffset=0))
    servoMotors.append(ServoMotor(Channel=4, ZeroOffset=0))
    servoMotors.append(ServoMotor(Channel=7, ZeroOffset=0))
    servoMotors.append(ServoMotor(Channel=8, ZeroOffset=0))
    servoMotors.append(ServoMotor(Channel=11, ZeroOffset=0))

   
    #servoMotors[0].setAngle((se_num1)+80)
    servoMotors[0].setAngle((se_num1)+0)
    servoMotors[1].setAngle((-1)*(se_num1)+74)
    servoMotors[2].setAngle((se_num2)+80)
    servoMotors[3].setAngle((-1)*(se_num2)+74)
    servoMotors[4].setAngle((se_num3))
    servoMotors[5].setAngle((se_num4)+40)

