from controller import Robot
robot = Robot()
ts = int(robot.getBasicTimeStep())

sensor = robot.getDevice('joint2_to_joint1_sensor')
sensor.enable(ts)

motor = robot.getDevice('joint2_to_joint1')
motor.setVelocity(1.0)
motor.setPosition(0.5)      # 0.5 rad target

while robot.step(ts) != -1:
    print(f"joint2 → joint1: {sensor.getValue():.3f} rad")
