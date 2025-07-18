r"""
Part of the bsd_video

In this scene we come to the original BSD formulation, definition of the rank.

create_data_for_plots_of_conjectured_limit.ipynb

"""


from manim import *
from manim.opengl import *
import sage.all as sagemath
from character import StudentChar
from msage import smanim
from first_scene import subtitle
from tools import *
import json


class FifthScene(Scene):

    def construct(self):
        pass


#  now render it
if __name__ == "__main__":
    with tempconfig({"renderer": "cairo", "quality": "medium_quality", "preview": True}):
        scene = FifthScene()
        scene.render()

