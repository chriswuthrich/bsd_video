r"""
Part of the bsd_video

This uses the characters and introduces
elliptic curves with some 2d pictures.

"""

from manim import *
from manim.opengl import *
from sage.all import *
from character import StudentChar
from msage import smanim
from tools import *


class FirstScene(Scene):

    def construct(self):
        # ##1.1
        bg_image = nature_background()
        self.add(bg_image)

        # chars on path
        st = StudentChar()
        te = StudentChar(height=1.2, width=0.8, colour=GREEN, lid_colour=DARK_GRAY)
        te.shift(vec(0, 0.1))  # aligned below
        st.scale(1)
        te.scale(1)
        st.shift(vec(0.5, -.5))
        te.shift(vec(1.8, -.5))
        shz(st, 10)
        shz(te, 10)
        self.add(st, te)
        self.wait(1)

        # st thinks of zeta(s)
        th = thought_bubble(r"\zeta(s)")
        th.shift(vec(-1, 1.9))
        th.scale(.75)
        th[2].scale(2)  # text in bubble
        th[2].set_color(YELLOW)
        th[1][1].shift(vec(0.2, 0))  # shift middle bubble
        th[1][2].shift(vec(0.4, 0))
        shz(th, 5)
        shz(th[2], 6)
        self.add(th)
        self.wait(1)

        # te thinks of $E$
        # TODO Replace E by a curve?
        th[1][0].shift(vec(2, 1))
        th[1][1].shift(vec(2.2, 0.8))
        th[1][2].shift(vec(2, 0.6))
        the = MathTex(r"E", font_size=36)
        the.move_to(th[0].get_center()+vec(1, 0))
        shz(the, 6)
        the.set_color(WHITE)
        the.scale(2)
        self.play(FadeIn(the))
        self.wait(.3)

        # and the E kicks out the zeta
        # TODO: Wrong item flies off???
        t = ValueTracker(0)

        def ple(tt):
            """
            bouncing function cooked up with cubic splines
            """
            if tt < 0.4:
                return 9.375 * tt ** 3 - 1.875 * tt ** 2
            elif tt < 0.5:
                return -300 * tt ** 3 + 390 * tt ** 2 - 165 * tt + 23.1
            elif tt < 0.7:
                return 50 * tt ** 3 - 90 * tt ** 2 + 52.5 * tt - 9.4
            else:
                return (-400 * tt ** 3 + 1020 * tt ** 2 - 840 * tt + 229) / 9

        def plz(tt):
            if tt < 0.5:
                return 0
            else:
                return 6 * (tt - 0.5)

        def opz(tt):
            if tt < 0.5:
                return 1
            else:
                return 2 * (1 - tt)

        the_start = the.get_center()
        the.add_updater(lambda m: m.move_to(the_start + vec(- ple(t.get_value()), 0)))
        # white goes to yellow:
        # the.add_updater(lambda m: m.set_color(rgb_to_color([255, 255, 255*(1-t.get_value())])))
        zeta_start = th[2].get_center()
        th[2].add_updater(lambda m: m.move_to(zeta_start + vec(-plz(t.get_value()), 0)))
        th[2].add_updater(lambda m: m.set_opacity(opz(t.get_value())))
        self.play(t.animate.set_value(1), run_time=1, rate_func=linear)
        self.remove(th[2])
        self.wait(1)

        # as the walk to the forefront, the bubble increases
        # TODO : Currently does not work correctly, bubbles don't disappear
        th.clear_updaters()
        t = ValueTracker(0)
        pa = lambda tt: vec(-6*tt**2, -2.7*tt)

        def op(tt):
            if tt < .5:
                return 1-2*tt
            else:
                return 0

        original_cloud = th[0].copy()

        def scale_cloud_updater(m):
            scale_factor = 1 + 9*t.get_value()
            new_square = original_cloud.copy().scale(scale_factor)
            m.become(new_square)

        th[0].add_updater(scale_cloud_updater)

        te_start = te.get_center()
        st_start = st.get_center()
        th_start = th.get_center()
        the_start = the.get_center()
        te.add_updater(lambda m: m.move_to(te_start + pa(t.get_value())))
        st.add_updater(lambda m: m.move_to(st_start + pa(t.get_value())))
        th.add_updater(lambda m: m.move_to(th_start + pa(t.get_value())))
        for thi in th[1]:
            thi.add_updater(lambda m: m.scale(op(t.get_value())))
            thi.add_updater(lambda m: m.set_opacity(op(t.get_value())))
        the.add_updater(lambda m: m.move_to((1-t.get_value())*the_start+t.get_value()*vec(-3, 3)))

        def ope(tt):
            if tt < 0.333:
                return 1-3*tt
            else:
                return 0
        the.add_updater(lambda m: m.set_opacity(ope(t.get_value())))

        # title appears
        tit = Paragraph("The Birch and Swinnerton-Dyer", "conjecture",
                        font_size=40,
                        color=YELLOW,
                        opacity=0,
                        alignment="center"
                        )

        tit.move_to(vec(-1, 3))
        shz(tit, 10)
        tit.add()

        def scale_title_updater(m):
            new_tit = Paragraph("The Birch and Swinnerton-Dyer", "conjecture",
                                font_size=40,
                                # font="Liberation Sans",
                                color=YELLOW,
                                opacity=t.get_value()**2,
                                alignment="center"
                                )
            new_tit.move_to((1-t.get_value())*vec(-1, 3))
            shz(new_tit, 11)
            new_tit.scale(0.1+t.get_value())
            m.become(new_tit)

        tit.add_updater(scale_title_updater)

        self.play(t.animate.set_value(1), run_time=7, rate_func=linear)
        self.wait(1)

        self.remove(tit, the, bg_image)

# -------------------------------------------

        # # 1.2
        # what are elliptic curves
        # TODO : Transition for the background. Maybe better in an editor?
        # or keep the bubble for later.
        th.clear_updaters()
        bgr = my_background()
        shz(bgr, -10)
        shz(th, -10)
        t = ValueTracker(0)
        bgr.add_updater(lambda m: m.set_opacity(op(t.get_value())))
        th.add_updater(lambda m: m.set_opacity(1-t.get_value()))
        self.play(t.animate.set_value(1), run_time=1, rate_func=linear)

        # equations appear central
        e1 = MathTex(r"y^2 = x^3", r"- 4\,", " x ", "+ 1")
        shz(e1, 5)
        self.play(FadeIn(e1))
        self.wait(1)
        e2 = MathTex(r"y^2 = x^3", r" - 7\,", " x ", " + 6")
        shz(e2, 5)
        self.play(Transform(e1, e2))
        self.wait(1)

        # # plot elliptic curve, move equations out
        # axes = my_fading_numberplane()
        # shz(axes, 1)
        # self.add(axes)
        # E = EllipticCurve([-4, 1])
        # curve = smanim(E.plot(color="yellow", thickness=2, alpha=0.3, xmax=7, ymin=-5, ymax=5))
        # shz(curve, 5)
        # # self.add(e1)
        # self.add(curve)
        #
        # self.play(Create(curve),
        #           e1.animate.to_corner(UL),
        #           e2.animate.to_corner(UL),
        #           run_time=1 )
        # self.wait(1)
        #
        # framebox1 = SurroundingRectangle(e1[1], buff=.1)
        # framebox2 = SurroundingRectangle(e1[3], buff=.1)
        # self.add(framebox1, framebox2)
        #
        # # merge to another curve
        # E2 = EllipticCurve([-7, 6])
        # curve2 = smanim(E2.plot(color="yellow", thickness=2, alpha=0.3, xmax=7, ymin=-5, ymax=5))
        # shz(curve2, 5)
        # self.play(
        #     Transform(curve, curve2),
        #     Transform(e1, e2),
        #     run_time=1
        # )
        # self.wait(1)
        #
        # # try to give lots of curves
        # ABs = [(-7,6), (-4,1), (9,1), (0,2), (-3,-1)]
        # for A,B in ABs:
        #     self.remove(e1, curve)
        #     E2 = EllipticCurve([A, B])
        #     curve = smanim(E2.plot(color="yellow", thickness=2, alpha=0.3, xmax=7, ymin=-5, ymax=5))
        #     shz(curve, 5)
        #     if A >= 0:
        #         Astr = fr"+{A}\,"
        #     else:
        #         Astr = fr"-{-A}\,"
        #     if B >= 0:
        #         Bstr = fr"+{B}"
        #     else:
        #         Bstr = fr"-{-B}"
        #     e1 = MathTex(r"y^2 = x^3 ", Astr, " x ", Bstr)
        #     e1.to_corner(UL)
        #     self.add(curve, e1)
        #     self.wait(1)


# now render it
if __name__ == "__main__":
    with tempconfig({"renderer": "opengl", "quality": "medium_quality", "preview": True}):
        scene = FirstScene()
        scene.render()
