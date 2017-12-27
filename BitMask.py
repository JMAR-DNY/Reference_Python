#bitmask to check if 4th bit is active
def check_bit4(input):
    mask = 0b01000
    desired = mask & input
    if desired >0:
        return "on"
    else:
        return "off"
