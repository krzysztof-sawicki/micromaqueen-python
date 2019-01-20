# micromaqueen-python
Python class for DFRobot Micro:Maqueen platform. 
## Usage
Sample program for testing front LEDs, reading distance, patrol and controlling motors:

    import microbit
    import maqueen
    mq = Maqueen()

	while True:
	    mq.set_led(0, 1)
	    microbit.sleep(1000)
	    mq.set_led(1, 1)
	    mq.set_led(0, 0)
	    microbit.sleep(1000)
	    mq.set_led(1, 0)
	    for i in range(0, 10):
		print("Distance: %d" % mq.read_distance())
		microbit.sleep(1000)

	   for i in range(0, 10):
               l = mq.read_patrol(0)
               p = mq.read_patrol(1)
               print("Patrol: %d %d" % (l, p))
               microbit.sleep(1000)

	    d = [-100, 50, 20, -200, 200, 40]
	    for i in d:
	        mq.set_motor(0, i)
	        microbit.sleep(1000)
	        mq.set_motor(1, i)
	        microbit.sleep(1000)

	    mq.motor_stop_all()


