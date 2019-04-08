import hashlib

# Generation the sha256 hashes
h1, h2, h3 = [hashlib.sha256() for i in range(3)]

# The image files
images = ["data/example.png", "data/example_messenger.png", "data/example_gmail.png"]

# Open the images
image, image_messenger, image_gmail = [open(image, 'rb').read() for image in images]

# Updated the hashes
h1.update(image)
h2.update(image_messenger)
h3.update(image_gmail)

# Printing the hashes
print(f'Source image :\t\t\t{h1.hexdigest()}')
print(f'Messenger downloaded image :\t{h2.hexdigest()}')
print(f'Gmail downloaded image :\t{h3.hexdigest()}')

