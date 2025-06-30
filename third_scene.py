r"""
Part of the bsd_video

Here the actual conjecture is
explained and illustrated
with graphs.

TODO

"""

from manim import *
from manim.opengl import *
import sage.all as sagemath
from character import StudentChar
from msage import smanim
from tools import subtitle, my_background
import json




class ThirdScene(Scene):

    def construct(self):
       pass


#  now render it
if __name__ == "__main__":
    with tempconfig({"renderer": "cairo", "quality": "medium_quality", "preview": True}):
        scene = ThirdScene()
        scene.render()
