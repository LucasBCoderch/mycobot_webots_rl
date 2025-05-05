# controllers/basic_control/basic_control.py
from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

# 1) Sensor y motor
sensor = robot.getDevice('joint2_to_joint1_sensor')
sensor.enable(timestep)

motor = robot.getDevice('joint2_to_joint1')
motor.setVelocity(1.0)
motor.setPosition(0.5)

# 2) Bucle principal
while robot.step(timestep) != -1:
    print(f"Joint2 position: {sensor.getValue():.3f} rad")
    break
