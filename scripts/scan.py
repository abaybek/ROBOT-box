import itertools
from pypot.dynamixel.io import DxlIO

with DxlIO('/dev/ttyUSB0') as dxl_io:
    ids = dxl_io.scan([1, 2, 3, 4, 5])
    print(dxl_io.get_present_position(ids))
    for i in range(180):
        dxl_io.set_goal_position(dict(zip(ids, itertools.repeat(i))))
