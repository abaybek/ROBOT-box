from pydynamixel import dynamixel, registers
serial_port = '/dev/ttyUSB0'
servo_id = 4;
target_position = 500;
try:
    ser  = dynamixel.get_serial_for_url(serial_port)
    dynamixel.init(ser, servo_id)
    dynamixel.set_position(ser, servo_id, target_position)
    dynamixel.send_action_packet(ser)
    print('Success')
except Exception as e:
    print('error')
    print(e)