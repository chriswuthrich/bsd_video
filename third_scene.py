r"""
Part of the bsd_video

Here the actual conjecture is
explained and illustrated
with graphs.

TODO

"""

from manim import *
import sage.all as sagemath
from character import StudentChar
from msage import smanim
from tools import *
import json




class ThirdScene(Scene):

    def construct(self):

        # 3.1 Count global points
        self.add(my_background())
        st = StudentChar()
        te = StudentChar(height=1.2, width=0.8, colour=GREEN, lid_colour=DARK_GRAY)
        st.scale(1)
        te.scale(1)
        stte = VGroup(st, te)
        stte.arrange()
        stte.to_corner(DL)
        shz(stte, 10)
        self.add(stte)

        # Title comes in
        tit = Text("Counting rational points", color=YELLOW)
        tit.shift(2*UP)
        self.play(GrowFromCenter(tit))
        self.wait(.5)
        e1 = MathTex(r"y^2 = x^3", r"- 4\,", " x ", "+ 1")
        e1.to_corner(UL)
        shz(e1, 5)
        self.add(e1)
        self.play(FadeOut(tit, shift=DOWN * 2, scale=1.5))
        self.wait(1)

        # table of points on this curve


#  now render it
if __name__ == "__main__":
    with tempconfig({"renderer": "cairo", "quality": "medium_quality", "preview": True}):
        scene = ThirdScene()
        scene.render()
