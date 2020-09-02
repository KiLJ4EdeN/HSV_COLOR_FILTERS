import cv2

class ColorDescriptor(object):
    def __init__(self):
        self.hsv_color = [0, 0, 0]

    def __del__(self):
        print('descriptor was collected.')

    def apply_color_filter(self, image, color_range=60, low=100, high=255):
        # the conversion
        image = cv2.medianBlur(image, 5)
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower_hsv = np.array([(self.hsv_color[0]-color_range), low, low])
        higher_hsv = np.array([(self.hsv_color[0]+color_range), high, high])
        hsv_mask = cv2.inRange(hsv_image, lower_hsv, higher_hsv)
        output = cv2.bitwise_and(image, image, mask=hsv_mask)
        return output, hsv_mask

    def change_color(self, bgr=(255, 0, 0)):
        color = np.uint8([[[bgr[0], bgr[1], bgr[2]]]])
        hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
        self.hsv_color = hsv_color[0][0]
        
        
if __name__ == '__main__':
    # load an image.
    image = cv2.imread('image.jpg', cv2.IMREAD_COLOR)
    
    # create color descriptor.
    desc = ColorDescriptor()

    # try some colors.
    desc.change_color(bgr=(255, 0, 0))
    res1, mask1 = desc.apply_color_filter(image=image, color_range=30, low=100, high=255) 
    
    desc.change_color(bgr=(0, 0, 255))
    res2, mask2 = desc.apply_color_filter(image=image, color_range=30, low=100, high=255) 
    
    cv2.imshow('blue', res1)
    cv2.imshow('blue_mask', mask1)
    
    cv2.imshow('red', res2)
    cv2.imshow('red_mask', mask2)
