import cv2


# 4 rows off buttons and operators
class Button:
    def __init__(self, position, width, height, text):
        self.position = position
        self.width = width
        self.height = height
        self.text = text

    # draw this on calling
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

    # draw this on click
    def buttonClicked(self, image, x, y):
        if self.position[0] < x < self.position[0] + self.width and \
                self.position[1] < y < self.position[1] + self.height:
            cv2.rectangle(image, self.position, (self.position[0] + self.width, self.position[1] + self.height),
                          (255, 255, 255), cv2.FILLED)
            # border
            cv2.rectangle(image, self.position, (self.position[0] + self.width, self.position[1] + self.height),
                          (50, 50, 50), 3)
            # text
            cv2.putText(image, self.text, (self.position[0] + 10, self.position[1] + 70), cv2.FONT_HERSHEY_PLAIN, 5,
                        (0, 0, 0), 5)
            return True
        else:
            return False


# top input area
class Input:
    def __init__(self, position, width, height, text):
        self.position = position
        self.width = width
        self.height = height
        self.text = text

    # draw this on calling
    def draw(self, image):
        cv2.rectangle(image, self.position, (self.position[0] + self.width, self.position[1] + self.height),
                      (255, 255, 255), cv2.FILLED)
        # border
        cv2.rectangle(image, self.position, (self.position[0] + self.width, self.position[1] + self.height),
                      (50, 50, 50), 3)
        # text
        cv2.putText(image, self.text, (self.position[0] + 10, self.position[1] + 70), cv2.FONT_HERSHEY_PLAIN, 2,
                    (50, 50, 50), 2)


class Equals:
    def __init__(self, position, width, height):
        self.position = position
        self.width = width
        self.height = height
        self.text = "="

    # draw this on calling
    def draw(self, image):
        cv2.rectangle(image, self.position, (self.position[0] + self.width, self.position[1] + self.height),
                      (215, 215, 215), cv2.FILLED)
        cv2.rectangle(image, self.position, (self.position[0] + self.width, self.position[1] + self.height),
                      (50, 50, 50), 3)
        cv2.putText(image, self.text, (self.position[0] + 185, self.position[1] + 45), cv2.FONT_HERSHEY_PLAIN, 2,
                    (50, 50, 50), 2)

    # draw this on click
    def equalsClicked(self, image, x, y):
        if self.position[0] < x < self.position[0] + self.width and \
                self.position[1] < y < self.position[1] + self.height:
            cv2.rectangle(image, self.position, (self.position[0] + self.width, self.position[1] + self.height),
                          (255, 255, 255), cv2.FILLED)
            # border
            cv2.rectangle(image, self.position, (self.position[0] + self.width, self.position[1] + self.height),
                          (50, 50, 50), 3)
            # text
            cv2.putText(image, self.text, (self.position[0] + 170, self.position[1] + 55), cv2.FONT_HERSHEY_PLAIN, 5,
                        (0, 0, 0), 5)
            return True
        else:
            return False


class Delete:
    def __init__(self, position, width, height):
        self.position = position
        self.width = width
        self.height = height

    def draw(self, image):
        cv2.rectangle(image, self.position, (self.position[0] + self.width, self.position[1] + self.height), (0, 0, 0),
                      cv2.FILLED)

    def deleteButtonClicked(self, image, x, y):
        if self.position[0] < x < self.position[0] + self.width and \
                self.position[1] < y < self.position[1] + self.height:
            return True
        else:
            return False
