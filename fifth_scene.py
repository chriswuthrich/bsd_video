r"""
Part of the bsd_video

In this scene we come to the original BSD formulation, definition of the rank.

create_data_for_plots_of_conjectured_limit.ipynb

"""


from manim import *
import sage.all as sagemath
from character import two_characters_standing_next_to_each_other
from msage import smanim
from tools import *
import json


class FifthScene(Scene):

    def construct(self):

        # 5 Origin
        # 5.1 Origin
        self.next_section("5.1 Origin")
        self.clear()
        stte = two_characters_standing_next_to_each_other()
        self.add(cloud_background(), stte)

        img = ImageMobject("bandsd.jpg")
        img.scale(.1)
        img.move_to(ORIGIN)
        self.add(img)
        self.wait(2)



#  now render it
if __name__ == "__main__":
    scene = FifthScene()
    scene.render()

