import logging

import cv2
from drivers import ArmDriver, ChassisDriver
from PIL import Image


class RaspberryPiChassisDriver(ChassisDriver):
    def __init__(self):
        self.logger = logging.getLogger(f"RaspberryPiChassisDriver")

    async def move(self, direction: float, speed: float, distance: float = -1.0):
        self.logger.debug('move %s %s %s', direction, speed, distance)
        pass

    async def rotate(self, speed: float):
        self.logger.debug('rotate %s', speed)
        pass


class RaspberryPiArmDriver(ArmDriver):
    def __init__(self, camera_id):
        self.logger = logging.getLogger(f"RaspberryPiArmDriver({camera_id})")
        self.camera = cv2.VideoCapture(camera_id)

    async def arm_up(self, speed):
        self.logger.debug('arm up %s', speed)
        pass

    async def arm_spray(self, time):
        self.logger.debug('arm spray %s', time)
        pass

    def capture_image(self) -> Image:
        self.logger.debug('capture image %s')
        return_value, image = self.camera.read()
        # You may need to convert the color.
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        im_pil = Image.fromarray(img)
        return im_pil

    def capture_image_raw(self):
        self.logger.debug('capture image raw %s')
        return_value, image = self.camera.read()
        return image
