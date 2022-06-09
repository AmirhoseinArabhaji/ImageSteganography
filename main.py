import argparse
import hashlib
import operator

from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument('-c', dest='cover_image_path', type=str, help='cover image path')
parser.add_argument('-s', dest='stegano_image', type=str, help='steganographed image')
parser.add_argument('--hide', action='store_true', help='hiding data')
parser.add_argument('--extract', action='store_true', help='extracting data')
args = parser.parse_args()


def hide():
    # opening image and get pixel map if image
    image = Image.open(args.cover_image_path)
    pixel_map = image.load()

    # reading hidden information from file
    with open('./data.txt', 'rb') as f:
        hidden_info = f.read()

    length_by_byte = len(hidden_info)
    length_by_bit = length_by_byte * 8

    # creating secret key
    # for example a sha256 hash key
    hash_key = hashlib.new('sha256')
    # adding a salt to hash key for more security
    salt = input('enter salt: ')
    hash_key.update(salt.encode())
    hex_hash_key = hash_key.hexdigest()

    # make secret key same length with the hidden information
    secret_key = hex_hash_key * (length_by_byte // len(hex_hash_key) + 1)

    # saving secret key
    with open('secret_key.txt', 'w') as f:
        f.write(hex_hash_key)

    print('secret key:')
    print(hex_hash_key)

    # hidden information and secret key to binary
    hidden_info_binary = ''.join([f'{byte:0{8}b}' for byte in hidden_info])
    secret_key_binary = ''.join([f'{byte:0{8}b}' for byte in bytearray(secret_key, 'utf8')])

    # get width and height of image
    width, height = image.size

    # storing length of data in lsb of reds in first row
    length_by_bit_binary = f'{length_by_bit:0{width}b}'
    for i in range(len(length_by_bit_binary)):
        red, green, blue = pixel_map[i, 0]

        red_bin = f'{red:0{8}b}'
        red = int(f'{red_bin[:-1]}{length_by_bit_binary[i]}', 2)

        pixel_map[i, 0] = (red, green, blue)

    # counter for data length
    counter = 0

    for row in range(1, height):
        for col in range(width):

            if counter < length_by_bit:
                red, green, blue = pixel_map[col, row]

                # xoring for determining if hidden info should store in lsb of blue or green
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

    # saving steg image
    image.save('./steg.png', format='png')


def extract():
    # opening image and get pixel map if image
    image = Image.open(args.stegano_image)
    pixel_map = image.load()

    width, height = image.size
    length_of_data = ''

    # storing length of data in lsb of reds in first row
    for i in range(width):
        red, _, _ = pixel_map[i, 0]
        length_of_data += bin(red)[-1]

    length_of_data = int(length_of_data, 2)

    secret_key = input('enter your secret key: ')
    secret_key = secret_key * (length_of_data // len(secret_key) + 1)
    secret_key_binary = ''.join([f'{byte:0{8}b}' for byte in bytearray(secret_key, 'utf8')])

    hidden_info_bin = ''

    # counter for data length
    counter = 0

    for row in range(1, height):
        for col in range(width):

            if counter < length_of_data:
                red, green, blue = pixel_map[col, row]

                # xoring for determining if hidden info stored in lsb of blue or green
                xor = operator.xor(int(bin(red)[-1]), int(secret_key_binary[counter]))

                hidden_info_bin += bin(green if xor == 1 else blue)[-1]

                counter += 1

    hidden_info = ''
    for i in range(0, len(hidden_info_bin), 8):
        hidden_info += chr(int(hidden_info_bin[i: i + 8], 2))

    with open('./extracted_data.txt', 'w') as f:
        f.write(hidden_info)


if args.hide:
    hide()
elif args.extract:
    extract()
