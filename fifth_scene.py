r"""
Part of the bsd_video

In this scene we come to the original BSD formulation, definition of the rank.

create_data_for_plots_of_conjectured_limit.ipynb

"""
from jupyterlab.galata import configure_jupyter_server
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

        caption1 = Text("Bryan Birch    and")
        caption2 = Text("Sir Peter Swinnerton-Dyer")
        caption2.next_to(caption1, DOWN)
        caption1.shift(1.5*LEFT)
        caption2.shift(2*RIGHT)
        caption = VGroup(caption1, caption2)
        shz(caption, 5)
        caption.next_to(img, DOWN)
        self.add(caption)
        self.add(img)

        self.wait(2)
        self.remove(img, caption)

        # 5.2 Actual conjecture
        self.next_section("5.2 Actual Conjecture")

        cloud_centre = vec(-1, 2.6)
        original_cloud = thought_bubble(cloud_centre, 0.85)[0]
        shz(original_cloud, 1)

        conj_lfunction_1 = MathTex(r"\operatorname{ord}_{s=1}\ ")
        conj_lfunction_2 = MathTex(r"L(E,s)")
        conj_lfunction_3 = MathTex(r"\ =\operatorname{rank} E(\mathbb{Q})")
        conj_lfunction_2.next_to(conj_lfunction_1, RIGHT)
        conj_lfunction_3.next_to(conj_lfunction_2, RIGHT)
        for m in [conj_lfunction_1, conj_lfunction_2, conj_lfunction_3]:
            m.shift(2*UP+2*LEFT)
            shz(m, 10)
        zeta = MathTex(r"\zeta(s)", font_size=72)
        zeta.move_to(cloud_centre)
        zeta.shift(.4*UP)
        shz(zeta, 10)
        icon = little_curve_icon()
        icon.next_to(zeta, DOWN)
        shz(icon, 10)

        t = ValueTracker(0)
        initial_scale = 7.48
        final_scale = 1.2

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

        # TODO : Why does the conjecture string appear from the start, icon and zeta don't ???

        self.play(
                t.animate.set_value(1),
                Succession(Wait(2),
                            FadeIn(conj_lfunction_2),
                            Wait(3),
                            FadeIn(conj_lfunction_1),
                            FadeIn(conj_lfunction_3),
                            Wait(3),
                            FadeIn(zeta),
                            FadeOut(conj_lfunction_1, conj_lfunction_2, conj_lfunction_3),
                            Wait(2),
                            Add(icon),
                            Wait(3)),
                run_time=20,
                rate_func=rate_functions.ease_in_out_sine)

        self.remove(zeta, icon, conj_lfunction_1, conj_lfunction_2, conj_lfunction_3)
        self.play(FadeOut(bu), run_time=1)
        self.wait(3)


#  now render it
if __name__ == "__main__":
    scene = FifthScene()
    scene.render()

