

from manim import *
import sage.all as sagemath
# from character import two_characters_standing_next_to_each_other
from msage import smanim
from tools import *


import json


def load_list(fi):
    r"""
    read json file fi into as a list
    """
    with open(fi, "r") as f:
        li = json.load(f)
    return li

class Conj(Scene):
    def construct(self):

        self.camera.background_color = WHITE

        # plot several in logarithmic coordinates
        axes_for_log_plot = Axes(x_range=[3, 9, 1],
                                 y_range=[0, 7, 1],
                                 x_length=10,
                                 y_length=5,
                                 x_axis_config={"include_numbers": False, 'tip_shape': CurvyPointyTip, 'color':BLACK},
                                 y_axis_config={"include_numbers": True, 'tip_shape': CurvyPointyTip, 'color':BLACK},
                                 color=BLACK,
                                 axis_config={
                                    "color": BLACK,        # axis lines
                                    # "number_color": BLACK, # numbers on axes
                                    # "label_color": BLACK,  # axis labels
                                    # "tick_color": BLACK,   # tick marks
                                    }
                                 )
        axes_for_log_plot.set_color(BLACK)

        for i in range(3, 9):
            label = MathTex(f"10^{str(i)}", color=BLACK).scale(0.7)
            label.next_to(axes_for_log_plot.c2p(i, 0), DOWN)
            axes_for_log_plot.add(label)

        #shift_the_full_graph = vec(1, 1)
        #axes_for_log_plot.shift(shift_the_full_graph)
        self.add(axes_for_log_plot)

        # first draw the usual curve
        li = load_list(f"../data/plotpts_curve_aa-4_up_to_9.json")
        log_graph = VMobject(color=rgb_to_color([0, 0, 155]))
        log_graph.set_points_as_corners([axes_for_log_plot.c2p(np.log10(x), y) for x, y in li if x > 1000])
        log_graph.set_style(stroke_width=2)
        eq_changing_curve = MathTex(r"y^2 = x^3 - 4\,x + 1 ", color=BLACK)
        eq_changing_curve.to_edge(UP)
        self.add(log_graph, eq_changing_curve)
        previous_log_graph = log_graph
        self.wait(2)
        self.remove(eq_changing_curve)

        # for each A draw the new draw and fade the old
        for aa in [-3, -2, -1, 0, 1, 2, 3, 4]:
            li = load_list(f"../data/plotpts_curve_aa{aa}_up_to_9.json")
            log_graph = VMobject(color=rgb_to_color([0, 0, 155]))
            log_graph.set_points_as_corners([axes_for_log_plot.c2p(np.log10(x), y) for x, y in li if x > 1000])
            log_graph.set_style(stroke_width=2)
            if aa < -1:
                eq_changing_curve = MathTex(f"y^2 = x^3 - {-aa} \\,x + 1 ", color=BLACK)
            elif aa == -1:
                eq_changing_curve = MathTex(r"y^2 = x^3 \ - x + 1 ", color=BLACK)
            elif aa == 0:
                eq_changing_curve = MathTex(r"y^2 = x^3 \phantom{-4\,x}+ 1 ", color=BLACK)
            elif aa == 1:
                eq_changing_curve = MathTex(r"y^2 = x^3 \ + x + 1 ", color=BLACK)
            else:
                eq_changing_curve = MathTex(f"y^2 = x^3 + {aa} \\,x + 1 ", color=BLACK)
            eq_changing_curve.to_edge(UP)
            self.add(eq_changing_curve)
            self.play(Create(log_graph),
                      FadeOut(previous_log_graph, rate_func=rate_functions.ease_out_circ),
                      Indicate(eq_changing_curve,color=BLACK),
                      run_time=3)
            self.remove(eq_changing_curve)
            previous_log_graph = log_graph

        self.wait(10)


#  now render it
if __name__ == "__main__":
    scene = Conj()
    scene.render()
