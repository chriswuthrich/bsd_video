r"""
File that calls all scenes and makes one video

"""

from manim import *
from first_scene import FirstScene
from second_scene import SecondScene
from third_scene import ThirdScene
from fourth_scene import FourthScene
from fifth_scene import FifthScene


class BSDVideo(Scene):
    def construct(self):

        FirstScene.construct()
        # self.clear()

        SecondScene.construct()

        ThirdScene.construct()

        FourthScene.construct()

        FifthScene.construct()



# now render it
if __name__ == "__main__":
    scene = BSDVideo()
    scene.render()