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

        # axes = Axes(
        #     x_range=[0, 10000, 1000],
        #     y_range=[0, 10],
        #     x_axis_config = {
        #         "include_numbers" : False,
        #     },
        #     axis_config={"color": WHITE},
        # )
        #
        # # Add custom x-axis labels at powers of 10
        # for val in [10, 100, 1000]:
        #     label = MathTex(str(val)).scale(0.4)
        #     label.next_to(axes.c2p(val, 0), DOWN)
        #     axes.add(label)
        # self.add(axes)
        #
        # gr = VMobject(color=YELLOW)
        # gr.set_points_as_corners([axes.c2p(x, y) for x, y in li])
        # self.play(Create(gr), run_time=3)

        # self.wait(1)
        # self.remove(gr, axes)

        # ValueTracker to animate max x-value
        t = ValueTracker(3)  # start at 1000 = 10^3
        x_max = lambda tt: 10**tt
        ticks = lambda tt: 10**(np.floor(tt)-1)

        def get_axes():
            axes = Axes(
                        x_range=[0, x_max(t.get_value()), ticks(t.get_value())],
                        y_range=[0, 7, 1],
                        x_length=10,
                        y_length=5,
                        x_axis_config={"include_numbers": False, 'tip_shape': StealthTip},
                        y_axis_config={"include_numbers": True, 'include_tip': False}
                        )
            # axes.shift(-3*DOWN-5*LEFT)
            ft = floor(t.get_value())
            i = 10**ft
            label = MathTex(f"10^{str(ft)}").scale(0.8)
            label.next_to(axes.c2p(i, 0), DOWN)
            axes.add(label)
            label1 = MathTex(f"10^{str(ft-1)}").scale(0.8)
            label1.next_to(axes.c2p(i/10, 0), DOWN)
            axes.add(label1)
            if t.get_value() < np.log10(5) + ft:
                i = ft - 1
            else:
                i = ft
            label2 = MathTex(f"5\\cdot 10^{str(i)}").scale(0.8)
            label2.next_to(axes.c2p(5*10**i, 0), DOWN)
            axes.add(label2)
            return axes

        axes = always_redraw(get_axes)
        self.add(axes)

        def get_graph():
            axes = get_axes()
            gr = VMobject(color=YELLOW)
            lit = [np.array([x,y]) for x,y in li if x < 0.9 * x_max(t.get_value())]
            gr.set_points_as_corners([axes.c2p(x, y) for x, y in lit])
            return gr

        gr = always_redraw(get_graph)
        self.add(gr)
        self.wait(2)

        # play from 10^3 to 10^(3+4)
        self.play(t.animate.set_value(7), run_time=10, rate_func=linear)
        self.wait(2)

        now_axes = axes.copy()
        gras = VGroup()
        for aa in [-3,-2,-1,0,1,2,3,4]:
            li = load_list(f"sage_notebooks/plotpts_curve_aa{aa}.json")
            graa = VMobject(color=YELLOW)
            graa.set_points_as_corners([now_axes.c2p(x, y) for x, y in li])
            gras.add(graa)
            self.play(Create(graa), run_time=3)


#  now render it
if __name__ == "__main__":
    with tempconfig({"quality": "medium_quality", "preview": True}):
        scene = FourthScene()
        scene.render()
