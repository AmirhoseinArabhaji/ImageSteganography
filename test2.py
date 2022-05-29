a_string = "abc"

byte_list = ''.join([bin(byte)[2:] for byte in bytearray(a_string, "utf8")])

