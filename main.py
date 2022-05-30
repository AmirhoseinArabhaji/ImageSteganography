import argparse
import hashlib
import operator

from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument('-c', dest='cover_image_path', type=str, help='cover image path')
args = parser.parse_args()

image = Image.open(args.cover_image_path)

pixel_map = image.load()

with open('./data.txt', 'rb') as f:
    hidden_info = f.read()

length_by_bit = len(hidden_info)

hash_key = hashlib.new('sha256')
# salt = input('enter salt: ')
salt = 'salt'
hash_key.update(salt.encode())
hex_hash_key = hash_key.hexdigest()
secret_key = hex_hash_key * (length_by_bit // len(hex_hash_key) + 1)

hidden_info_binary = ''.join([f'{byte:0{8}b}' for byte in hidden_info])
secret_key_binary = ''.join([f'{byte:0{8}b}' for byte in bytearray(secret_key, "utf8")])

width, height = image.size

counter = 0
for row in range(height):
    for col in range(width):

        if counter < length_by_bit:
            red, green, blue = pixel_map[col, row]

            # determines if hidden info should store in blue or green
            xor = operator.xor(int(bin(red)[-1]), int(secret_key_binary[counter]))

            # store data in green color
            if xor == 1:
                green_bin = f'{green:0{8}b}'
                green = int(f'{green_bin[:-1]}{hidden_info_binary[counter]}', 2)
            # store data in blue color
            elif xor == 0:
                blue_bin = f'{blue:0{8}b}'
                blue = int(f'{blue_bin[:-1]}{hidden_info_binary[counter]}', 2)

            pixel_map[col, row] = (red, green, blue)

            counter += 1

image.save('./steg.jpg')
