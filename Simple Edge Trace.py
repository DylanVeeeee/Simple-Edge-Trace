import cv2
from matplotlib import pyplot as plt

filepath = input('Input Path to File: ')
dpi = input('Input DPI: ')
th1 = input('Threshhold 1: ')
th2 = input('Threshhold 2: ')
filepath = filepath.strip('\"')
dpi = int(dpi)
th1 = int(th1)
th2 = int(th2)

image = cv2.imread(filepath)
canny = cv2.Canny(image, th1, th2)

plt.imshow(canny, 'gray')
plt.xticks([])
plt.yticks([])

plt.savefig('canny.png', dpi=dpi, bbox_inches='tight')
plt.show()
