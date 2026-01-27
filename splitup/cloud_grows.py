r"""
split scene
1.2, 1.3
cloud that grows containing zeta and elliptic curve
"""

from manim import *
from tools import thought_bubble, vec, shz, little_curve_icon


class CloudGrowsScene1(Scene):

    def construct(self):

        # 1
        # 1.1 From real to maths world

        # st thinks of zeta(s)
        cloud_centre = vec(-1, 2.6)
        thoughts = thought_bubble(cloud_centre, 0.85)
        # shift small bubbles a little
        thoughts[1][0].shift(vec(0, 0.2))
        thoughts[1][1].shift(vec(0.2, 0.2))
        thoughts[1][2].shift(vec(0.6, 0.4))
        shz(thoughts[0], 1)

        # text in the bubble
        zeta = MathTex(r"\zeta(s)", font_size=72)
        zeta.set_color(YELLOW)
        zeta.move_to(cloud_centre)
        shz(zeta, 5)
        self.add(thoughts, zeta)
        self.wait(1)

        # te thinks of an elliptic curve
        # small bubbles move to teacher
        thoughts[1][0].shift(vec(2, .5))
        thoughts[1][1].shift(vec(2.2, .7))
        thoughts[1][2].shift(vec(2.1, 0.6))

        # the little elliptic curve appears
        icon = little_curve_icon()
        icon.move_to(cloud_centre + vec(1.3, 0))
        shz(icon, 5)
        self.play(FadeIn(icon))
        self.wait(.3)

        # and the curve kicks out the zeta
        t = ValueTracker(0)

        # the elliptic curve icon moves and changes colour
        def icon_movement(tt):
            """
            bouncing function cooked up with cubic splines
            """
            # this was created in
            # bump_rate_function_for_first_scene.ipynb
            if tt < 0.4:
                return 12.5*tt**3 - 3.75*tt**2
            elif tt < 0.5:
                return -100*tt**3 + 120*tt**2 - 45*tt + 5.4
            elif tt < 0.7:
                return 50*tt**3 - 90*tt**2 + 52.5*tt - 9.6
            elif tt < 1:
                return (-1600*tt**3 + 4080*tt**2 - 3360*tt + 907)/27
            else:
                return 1

        icon.add_updater(lambda m: m.move_to(cloud_centre
                                             + vec(1.3, 0, z=5/100)
                                             - vec(icon_movement(t.get_value()), 0)))
        # white goes to yellow:
        icon.add_updater(lambda m: m.set_color(rgb_to_color([255, 255, 255 * (1 - t.get_value())])))

        # the zeta gets kicked out and vanishes
        def zeta_movement(tt):
            if tt < 0.5:
                return 0
            else:
                return 6 * (tt - 0.5)

        def zeta_opacity(tt):
            if tt < 0.5:
                return 1
            else:
                return 2 * (1 - tt)

        zeta.add_updater(lambda m: m.move_to(cloud_centre
                                             - vec(zeta_movement(t.get_value()), 0)))
        zeta.add_updater(lambda m: m.set_opacity(zeta_opacity(t.get_value())))

        self.play(t.animate.set_value(1), run_time=2, rate_func=linear)
        self.play(icon.animate.move_to(cloud_centre), run_time=0.3)
        self.wait(.7)
        self.remove(zeta)

        # bubble grows, title appears, and characters move to the lower left corner
        t = ValueTracker(0)

        # bubble grows
        thoughts.clear_updaters()
        original_cloud = thoughts[0].copy()
        self.remove(thoughts[1])

        def scale_cloud_updater(m):
            if t.get_value() < .72:
                scale_factor = 1 + 9*t.get_value()
            else:
                scale_factor = 7.48  # value at .72
            mo = original_cloud.copy().scale(scale_factor)
            m.become(mo)

        # move to the centre
        def cloud_movement(tt):
            s = (1-tt) * cloud_centre
            s += vec(0, 0, 1/100)
            return s

        thoughts.add_updater(lambda m: m.move_to(cloud_movement(t.get_value())))
        thoughts.add_updater(scale_cloud_updater)


# now render it
if __name__ == "__main__":
    scene = CloudGrowsScene1()
    scene.render()