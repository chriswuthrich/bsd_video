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

        axes = Axes(
            x_range=[0, 10000, 1000],
            y_range=[0, 10],
            x_axis_config = {
                "include_numbers" : False,
            },
            axis_config={"color": WHITE},
        )

        # Add custom x-axis labels at powers of 10
        for val in [10, 100, 1000]:
            label = MathTex(str(val)).scale(0.4)
            label.next_to(axes.c2p(val, 0), DOWN)
            axes.add(label)
        self.add(axes)

        gr = VMobject(color=YELLOW)
        gr.set_points_as_corners([axes.c2p(x, y) for x, y in li])
        self.play(Create(gr), run_time=3)
        #
        # self.wait(1)
        # self.remove(gr, axes)
        # # ValueTracker to animate max x-value
        # x_max_tracker = ValueTracker(1)
        #
        # def updater_axes(mob):
        #     mob.become(
        #         Axes(x_range=[0, 1000*x_max_tracker.get_value(), 100*x_max_tracker.get_value()],
        #         y_range=[0, 10],
        #         x_axis_config = {"include_numbers" : False},
        #         axis_config={"color": WHITE},
        #         )
        #     )
        # axes.add_updater(updater_axes)
        #
        # # # Graph that depends on the current x_max
        # gr = VMobject(color=YELLOW)
        # def updater_gr(mob):
        #     mob.become(VMobject(color=YELLOW).set_points_as_corners([axes.c2p(x, y) for x, y in li if x<900*x_max_tracker.get_value()]))
        # gr.add_updater(updater_gr)
        #
        # # graph = always_redraw(lambda: axes.plot(
        # #     func,
        # #     x_range=[0, x_max_tracker.get_value()],
        # #     use_smoothing=True,
        # #     color=BLUE,
        # # ))
        # #
        # self.add(axes, gr)
        # #
        # # # Animate the value tracker to increase x_max over time
        # self.play(x_max_tracker.animate.set_value(2), run_time=5, rate_func=linear)
        # self.wait(1)

        self.remove(gr, axes)
        self.wait(.5)
        t = ValueTracker(5)
        axes = Axes(
            x_range=[0, t.get_value(), 1],
            y_range=[0, 5, 1],
            x_length=10,
            y_length=5,
            axis_config={"include_numbers": True}
        )

        # Function to plot
        def func(x):
            return 0.5 * x ** 0.5

        # Add updater to axes
        def update_axes(mob):
            new_x_range = [0, t.get_value(), 1]
            # Save current state
            mob.become(
                Axes(
                    x_range=new_x_range,
                    y_range=[0, 5, 1],
                    x_length=10,
                    y_length=5,
                    axis_config={"include_numbers": True}
                )
            )

        gr = axes.plot(func,
                       x_range=[0, 1],
                       color=BLUE,
                       )

        def update_gr(mob):
            mob.become(
               axes.plot(func,
                       x_range=[0, t.get_value()],
                       color=BLUE,
                       )
            )

        axes.add_updater(update_axes)
        gr.add_updater(update_gr)

        self.add(axes, gr)

        # Animate the tracker to increase x_max
        self.play(t.animate.set_value(10), run_time=5, rate_func=linear)
        self.wait()

#  now render it
if __name__ == "__main__":
    with tempconfig({"quality": "medium_quality", "preview": True}):
        scene = FourthScene()
        scene.render()
