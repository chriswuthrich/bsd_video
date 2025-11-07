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

        # 5 Rank and original conjecture
        # 5.1 Rank
        self.next_section("5.1 What is the rank")
        self.clear()
        stte = two_characters_standing_next_to_each_other()
        self.add(cloud_background(), stte)

        # state Theorem
        thm_tit = Text("Theorem:", color=YELLOW)





#  now render it
if __name__ == "__main__":
    scene = FifthScene()
    scene.render()

