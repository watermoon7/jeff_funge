from Inbound import *
class Camera():
    global inboundss
    def __init__(self, obj, bounding_box, ib):
        self.obj = obj
        self.bounding_box = bounding_box

    def camera_movement(self, blocks, dis):
        global inboundss
        if self.obj.rect.x > self.bounding_box.right:
            inboundss = False
            for block in blocks:
                block.x -= dis
        elif self.obj.rect.x < self.bounding_box.left:
            self.ib = False
            for block in blocks:
                block.x += dis
            
