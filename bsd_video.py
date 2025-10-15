r"""

File that calls all scenes and makes one video

"""

from manim import *
from first_scene import FirstScene
from second_scene import SecondScene
from third_scene import ThirdScene
from fourth_scene import FourthScene
from fifth_scene import FifthScene


class BSDVideo(ThreeDScene):
    def construct(self):

        FirstScene.construct(self)

        SecondScene.construct(self)

        # ThirdScene.construct(self)

        # FourthScene.construct(self)

        # FifthScene.construct(self)



# now render it
if __name__ == "__main__":
    scene = BSDVideo()
    scene.render()
