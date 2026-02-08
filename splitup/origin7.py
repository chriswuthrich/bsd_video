r"""
split scene
7

"""

from manim import *
import sage.all as sagemath
from tools import vec,  shz, thought_bubble, little_curve_icon
from msage import smanim
import json



# now
# ---------------------------------

class Origin7(Scene):

    def construct(self):

        # 5 Origin
        # 5.1 Origin
        self.next_section("5.1 Origin")
        self.clear()
        bu =  thought_bubble(ORIGIN, size=7.48)  # usual background
        shz(bu, 1)
        self.add( bu)

        img = ImageMobject("../pics/bandsd.jpg")
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

        self.wait(4)
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

        def cloud_updater(m, a, b, tt):
            ss = a + (b-a)*tt
            scale_factor = initial_scale+ss*(final_scale-initial_scale)
            mo = original_cloud.copy().scale(scale_factor)
            ce = ss * cloud_centre
            ce += vec(0, 0, 1/100)
            mo.move_to(ce)
            m.become(mo)


        bu.add_updater(lambda m: cloud_updater(m, 0, .2, t.get_value()))
        self.add(conj_lfunction_2)
        self.play(t.animate.set_value(1),
                  rate_func = rate_functions.linear,
                  run_time=2)
        bu.clear_updaters()

        t = ValueTracker(0)
        bu.add_updater(lambda m: cloud_updater(m, .2, .5, t.get_value()))
        self.add(conj_lfunction_1, conj_lfunction_3)
        self.play(t.animate.set_value(1),
                  rate_func = rate_functions.linear,
                  run_time=3)
        bu.clear_updaters()

        self.add(zeta)
        self.remove(conj_lfunction_1, conj_lfunction_2, conj_lfunction_3)
        t = ValueTracker(0)
        bu.add_updater(lambda m: cloud_updater(m, .5, .8, t.get_value()))
        self.play(t.animate.set_value(1),
                  rate_func = rate_functions.linear,
                  run_time=3)
        bu.clear_updaters()

        self.add(icon)
        t = ValueTracker(0)
        bu.add_updater(lambda m: cloud_updater(m, .8, 1, t.get_value()))
        self.play(t.animate.set_value(1),
                  rate_func = rate_functions.linear,
                  run_time=2)
        bu.clear_updaters()

        # self.play(
        #         t.animate.set_value(1),
        #         Succession(Wait(2),
        #                     FadeIn(conj_lfunction_2),
        #                     Wait(3),
        #                     FadeIn(conj_lfunction_1),
        #                     FadeIn(conj_lfunction_3),
        #                     Wait(3),
        #                     FadeIn(zeta),
        #                     FadeOut(conj_lfunction_1, conj_lfunction_2, conj_lfunction_3),
        #                     Wait(2),
        #                     Add(icon),
        #                     Wait(3)),
        #         run_time=20,
        #         rate_func=rate_functions.ease_in_out_sine)

        self.remove(zeta, icon)
        self.play(FadeOut(bu), run_time=.5)
        self.wait(3)




# render it


if __name__ == "__main__":
    config.renderer = "cairo"
    config.format = "png"
    config.transparent = True
    config.write_to_movie = False
    #config.preview = True

    # Optional but recommended
    config.background_color = None

    scene = Origin7()
    scene.render()
