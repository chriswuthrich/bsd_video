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

        # 5 Origin
        # 5.1 Origin
        self.next_section("5.1 Origin")
        self.clear()
        bg = natural_initial_background()
        stte = two_characters_standing_next_to_each_other()
        shz(stte,5)
        bu =  thought_bubble(ORIGIN, size=7.48)  # usual background
        shz(bu, 1)
        self.add(bg, bu, stte)

        img = ImageMobject("pics/bandsd.jpg")
        img.scale(.3)
        img.shift(UP)
        img.shift(RIGHT)
        shz(img, 5)

        caption1 = Text("Bryan Birch")
        caption2 = Text("and")
        caption2.next_to(caption1, DR)
        caption3 = Text("Sir Peter Swinnerton-Dyer")
        caption3.next_to(caption2, DOWN)
        caption = VGroup(caption1, caption2, caption3)
        shz(caption, 5)
        caption.next_to(img, DOWN)
        self.add(caption)
        self.add(img)

        self.wait(2)
        self.remove(img, caption)

        cloud_centre = vec(-1, 2.6)
        original_cloud = thought_bubble(cloud_centre, 0.85)[0]
        shz(original_cloud, 1)

        t = ValueTracker()
        initial_scale = 7.48
        final_scale = 1

        def scale_cloud_updater(m):
            scale_factor = initial_scale + t.get_value()*(final_scale - initial_scale)
            mo = original_cloud.copy().scale(scale_factor)
            m.become(mo)

        def cloud_movement(tt):
            s = (1-tt) * cloud_centre
            s += vec(0, 0, 1/100)
            return s

        bu.add_updater(lambda m: m.move_to(cloud_movement(t.get_value())))
        bu.add_updater(scale_cloud_updater)

        conj_lfunction = MathTex(r"\operatorname{ord}_{s=1} L(E,s) = \operatorname{rank} (\mathbb{Q})")
        conj_lfunction.shift(2*UP+LEFT)
        shz(conj_lfunction, 10)
        lfunction = VGroup(conj_lfunction[6:11]) # MathTex(r"L(E,s)")
        zeta = MathTex(r"\zeta(s)", font_size=72)
        zeta.move_to(cloud_centre)
        zeta.shift(.4*UP)
        shz(zeta, 10)
        icon = little_curve_icon()
        icon.next_to(zeta, DOWN)
        shz(icon, 10)

        def bump(tt, a, b):
            epsilon = .05
            if tt<a-epsilon:
                return 0
            elif tt<a:
                return rate_functions.smooth((tt-a+epsilon)/epsilon)
            elif tt<b:
                return 1
            elif tt<b+epsilon:
                return rate_functions.smooth((epsilon+b-tt)/epsilon)
            else:
                return 0

        lfunction_visible = lambda tt : bump(tt, .1, .5)
        conj_visible = lambda tt : bump(tt, .3, .5)
        zeta_visible = lambda tt : bump(tt, .4,.9)
        icon_visible = lambda tt : bump(tt, .6, .9)
        conj_lfunction.add_updater(lambda m: m.set_opacity(conj_visible(t.get_value())))
        lfunction.add_updater(lambda m: m.set_opacity(lfunction_visible(t.get_value())))
        zeta.add_updater(lambda m: m.set_opacity(zeta_visible(t.get_value())))
        icon.add_updater(lambda m: m.set_opacity(icon_visible(t.get_value())))

        self.add(icon, zeta, conj_lfunction)

        # TODO : Icon doesn't draw correctly and L on its own doesn' t show.

        self.play(t.animate.set_value(1),
                  run_time=20,
                  rate_func=rate_functions.ease_in_out_sine)
        self.remove(zeta, icon)
        self.play(FadeOut(bu), run_time=1)
        self.wait(3)


#  now render it
if __name__ == "__main__":
    scene = FifthScene()
    scene.render()

