import argparse
import random
import string
import operator

from PIL import Image


def get_random_string(length) -> str:
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for _ in range(length))
    print("Random string of length", length, "is:", result_str)
    return result_str


parser = argparse.ArgumentParser()
parser.add_argument('-c', dest='cover_image_path', type=str, help='cover image path')
args = parser.parse_args()

image = Image.open(args.cover_image_path)

pixel_map = image.load()

# hidden_info = input('write hidden info: ')
hidden_info = 'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha' \
              'adskhfbsdjahfskadjhfjksdbfkjsdhbfkjdshflkjsahdflkshdlfhsaldkfhlksdjhflsajhdfljshadlfkjdshlfjsha'
length_by_bit = len(hidden_info) * 8

secret_key = get_random_string(len(hidden_info))

hidden_info_binary = ''.join([f'{byte:0{8}b}' for byte in bytearray(hidden_info, "utf8")])
secret_key_binary = ''.join([f'{byte:0{8}b}' for byte in bytearray(secret_key, "utf8")])

width, height = image.size

counter = 0
for row in range(height):
    for col in range(width):

        if counter < length_by_bit:
            red, green, blue = pixel_map[col, row]

            xor = operator.xor(int(bin(red)[-1]), int(secret_key_binary[counter]))

            if xor == 1:
                green_bin = f'{green:0{8}b}'
                green = int(f'{green_bin[:-1]}{hidden_info_binary[counter]}')
            elif xor == 0:
                blue_bin = f'{blue:0{8}b}'
                blue = int(f'{blue_bin[:-1]}{hidden_info_binary[counter]}')

            pixel_map[col, row] = (red, green, blue)

            counter += 1

image.save('./steg.jpg')
