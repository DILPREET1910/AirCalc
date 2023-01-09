import cv2


class Button:
    def __init__(self, position, width, height, text):
        self.position = position
        self.width = width
        self.height = height
        self.text = text

    def draw(self, image):
        # button
        cv2.rectangle(image, self.position, (self.position[0] + self.width, self.position[1] + self.height),
                      (215, 215, 215), cv2.FILLED)
        # border
        cv2.rectangle(image, self.position, (self.position[0] + self.width, self.position[1] + self.height),
                      (50, 50, 50), 3)
        # text
        cv2.putText(image, self.text, (self.position[0] + 20, self.position[1] + 40), cv2.FONT_HERSHEY_PLAIN, 2,
                    (50, 50, 50), 2)
