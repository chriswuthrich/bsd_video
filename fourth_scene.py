r"""
Part of the bsd_video

Here we illustrate the conjectures with moving graphs

"""

from manim import *
from sage.all import *
from character import StudentChar
from msage import smanim
from first_scene import subtitle
from third_scene import my_background
import json

def load_list(fi):
    r"""
    read json file fi into as a list
    """
    with open(fi, "r") as f:
        li = json.load(f)
    return li

class FourthScene(Scene):

    def construct(self):
        gradient_rect = my_background()
        self.add(gradient_rect)

        li = load_list("plotpts_curve_rk2.json")
        print(len(li))

        axes = Axes(
            x_range=[0, 10000, 10000/10],
            y_range=[0, 10],
            x_axis_config = {"numbers_to_include": [10**i for i in [2,3,4,5,6,7,8]]},
            axis_config={"color": WHITE},
        ).add_coordinates()

        self.add(axes)

        gr = VMobject(color=YELLOW)
        gr.set_points_as_corners([axes.c2p(x, y) for x, y in li[:1000]])
        self.play(Create(gr))




#  now render it
if __name__ == "__main__":
    with tempconfig({"quality": "medium_quality", "preview": True}):
        scene = FourthScene()
        scene.render()
