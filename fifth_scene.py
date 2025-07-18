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

        # 5 Rank and original conjecture
        # 5.1 Rank
        self.next_section("5.1 What is the rank")
        st = StudentChar()
        te = StudentChar(height=1.2, width=0.8, colour=GREEN, lid_colour=DARK_GRAY)
        st.scale(1)
        te.scale(1)
        stte = VGroup(st, te)
        stte.arrange()
        stte.to_corner(DL)
        shz(stte, 10)
        self.add(my_background(), stte)

        # state Theorem
        thm_tit = Text("Theorem:", color=YELLOW)




#  now render it
if __name__ == "__main__":
    with tempconfig({"renderer": "cairo", "quality": "medium_quality", "preview": True}):
        scene = FifthScene()
        scene.render()

