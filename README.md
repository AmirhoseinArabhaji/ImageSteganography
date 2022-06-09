# ImageSteganography
A new approach for LSB based image steganography using secret key

Implementation of this article
[this article](https://www.researchgate.net/publication/261421805_A_new_approach_for_LSB_based_image_steganography_using_secret_key).

##Running

* `python3 -m venv venv`
* `pip install - requirements.txt`

### hiding data in image

`python main.py --hide -c <path_to_cover_image>`

### extracting data from image

`python main.py --extract -s <path_to_stego_image>`