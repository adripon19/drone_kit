# The goal of this file is to test
# the led mounted on the top of the navio
#
# setPWMFreq(channel, on , off)
# channel: The channel that should be updated with the new values (0..15)
# on: The tick (between 0..4095) when the signal
# should transition from low to high
# off:the tick (between 0..4095) when the signal
# should transition from high to low


from navio.adafruit_pwm_servo_driver import PWM
# what's doing ?!?

pwm = PWM(0x40, debug=False)
# 0x40 is the address of the LED
pwm.setPWMFreq(60)


while true:
    R = 0
    G = 0
    B = 4095
    pwm.setPWMFreq(R, G, B)
