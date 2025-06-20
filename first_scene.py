r"""
Part of the bsd_video

This uses the characters and introduces
elliptic curves with some 2d pictures.

"""

from manim import *
from manim.opengl import *
import sage.all as sagemath
from character import StudentChar
from msage import smanim
from tools import *

def little_curve():
    # the svg file is a simplified output from
    # sage modified with inkscape
    ellicon = SVGMobject("pics/ellicon3.svg",
                        stroke_width=8
                        )
    # part 0 and 1 are boxes
    v = ellicon[2]  # this is the curve
    v.set_color(WHITE)
    v.scale(.5)
    return v


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
        st_start = vec(1.8, -.5)
        te_start = vec(.5,-.5)
        st.shift(st_start)
        te.shift(te_start)
        shz(st, 10)
        shz(te, 10)
        self.add(st, te)
        self.wait(1)

        # st thinks of zeta(s)
        cloud_centre = vec(-1, 2.6)
        thoughts = thought_bubble(cloud_centre, 0.85)
        # shift small bubbles a little
        thoughts[1][0].shift(vec(0, 0.2))
        thoughts[1][1].shift(vec(0.2, 0.2))  # shift middle little bubble
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
        icon = little_curve()
        icon.move_to(cloud_centre+vec(1.3, 0))
        shz(icon, 5)
        self.play(FadeIn(icon))
        self.wait(.3)

        # and the curve kicks out the zeta
        t = ValueTracker(0)

        def ple(tt):
            """
            bouncing function cooked up with cubic splines
            """
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
                                             - vec(ple(t.get_value()), 0)))
        # white goes to yellow:
        icon.add_updater(lambda m: m.set_color(rgb_to_color([255, 255, 255 * (1 - t.get_value())])))

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

        # TODO check there is no little jump anymore in zeta before move.
        zeta.add_updater(lambda m: m.move_to(cloud_centre
                                             - vec(plz(t.get_value()), 0)))
        zeta.add_updater(lambda m: m.set_opacity(opz(t.get_value())))

        self.play(t.animate.set_value(1), run_time=2, rate_func=linear)
        self.play(icon.animate.move_to(cloud_centre), run_time=0.3)
        self.wait(.7)

        # title appears
        tit = Paragraph("The Birch and Swinnerton-Dyer", "conjecture",
                        font_size=40,
                        font="Noto Sans",
                        color=YELLOW,
                        opacity=1,
                        alignment="center"
                        )

        tit.move_to(vec(-1, 3))
        shz(tit, 5)
        # self.play(Write(tit))
        # self.wait(.5)

        # as the walk to the forefront, the bubble increases
        self.remove(zeta)
        thoughts.clear_updaters()
        icon.clear_updaters()
        self.remove(thoughts, icon, tit, st, te, bg_image)
        self.add(bg_image, thoughts, tit, icon, st, te)  # put in the correct order

        t = ValueTracker(0)
        pa = lambda tt: vec(-6*tt**2, -2.5*tt)

        def op(tt):
            if tt < .5:
                return 1-2*tt
            else:
                return 0

        original_cloud = thoughts[0].copy()

        def scale_cloud_updater(m):
            scale_factor = 1 + 9*t.get_value()
            mo = original_cloud.copy().scale(scale_factor)
            m.become(mo)

        thoughts[0].add_updater(scale_cloud_updater)

        te.add_updater(lambda m: m.move_to(te_start
                                           + pa(t.get_value())
                                           + vec(0,0, z=10/100)))
        st.add_updater(lambda m: m.move_to(st_start
                                           + pa(t.get_value())
                                           + vec(0,0, z=10/100)))
        thoughts.add_updater(lambda m: m.move_to(cloud_centre
                                                 + pa(t.get_value())
                                                 + vec(0, 0, z=1/100)))
        # for thi in thoughts[1]:
        #    thi.add_updater(lambda m: m.scale(op(t.get_value())))
        #    thi.add_updater(lambda m: m.set_opacity(op(t.get_value())))

        # i_path = lambda tt : vec(5*tt,0)
        # icon.add_updater(lambda m: m.move_to(cloud_centre
        #                                      + i_path(t.get_value())
        #                                      + vec(0, 0, z=5/100)))
        #icon.add_updater(lambda m: m.set_opacity(1-t.get_value()))
        self.remove(thoughts[1])

        def title_updater(m):
            new_tit = Paragraph("The Birch and Swinnerton-Dyer", "conjecture",
                                font_size=40,
                                font="Noto Sans",
                                color=YELLOW,
                                opacity=1,  # t.get_value()**2,
                                alignment="center"
                                )
            new_tit.scale(0.1 + t.get_value())
            new_tit.move_to((1 - t.get_value()) * vec(-1, 3))
            shz(new_tit, 5)
            m.become(new_tit)

        tit.add_updater(title_updater)

        self.play(t.animate.set_value(1),
                  # TODO What to do with the icon here?
                  FadeOut(icon),
                  run_time=7,
                  rate_func=linear)
        self.wait(1)

        self.remove(tit, icon, bg_image)
        self.clear()
        self.add(thoughts[0])
        self.add(st, te)

# -------------------------------------------

        # # 1.2
        # what are elliptic curves
        # TODO : Transition for the background. Maybe better in an editor?
        # or keep the bubble for later.
        thoughts.clear_updaters()
        st.clear_updaters()
        te.clear_updaters()
        bgr = my_background()
        shz(bgr, -1)
        shz(thoughts, -1)
        t = ValueTracker(0)
        bgr.add_updater(lambda m: m.set_opacity(op(t.get_value())))
        thoughts.add_updater(lambda m: m.set_opacity(1-t.get_value()))
        self.play(t.animate.set_value(1), run_time=1, rate_func=linear)

        self.remove(thoughts)
        bgr.set_opacity(1)
        bgr.clear_updaters()
        self.add(bgr)
        self.add(st, te)
        self.wait(.2)

        # equations appear central
        e1 = MathTex(r"y^2 = x^3", r"- 4\,", " x ", "+ 1")
        shz(e1, 5)
        self.play(FadeIn(e1))
        self.wait(1)
        ellc = Text("Elliptic curve", font="Noto Sans")
        ellc.next_to(e1, DOWN)
        self.play(FadeIn(ellc))
        self.wait(1)

        # plot elliptic curve, move equations out
        grid = VGroup()
        grid.add(my_fading_numberplane())
        grid.add(Line(vec(-7.112,0), vec(7.112, 0), color=WHITE, stroke_width=2))
        grid.add(Line(vec(0, -4), vec(0, 4), color=WHITE, stroke_width=2))
        shz(grid, 1)
        self.add(grid)
        axex = Arrow(start=vec(0,0),
                     end=vec(6.5,0),
                     buff=0,
                     stroke_width=2,
                     tip_length=0.2,
                     color=WHITE)
        axey = Arrow(start=vec(0, 0),
                     end=vec(0, 3.5),
                     buff=0,
                     stroke_width=2,
                     tip_length=0.2,
                     color=WHITE)
        shz(axex,1)
        shz(axey, 1)
        E = sagemath.EllipticCurve([-4, 1])
        curve = smanim(E.plot(color="yellow", thickness=2, alpha=0.3, xmax=7, ymin=-5, ymax=5))
        shz(curve, 5)
        self.add(curve)
        ellc.add_updater(lambda m: m.next_to(e1, DOWN))
        self.play(Create(curve),
                  e1.animate.to_corner(UL),
                  FadeIn(axex, axey),
                  run_time=1)
        self.wait(1)

        # doesn't work yet? opengl problem?
        framebox1 = MySurroundingRectangle(e1[1], color=YELLOW, buff=.1)
        framebox2 = MySurroundingRectangle(e1[3], color=YELLOW, buff=.1)
        self.add(framebox1, framebox2)

        # merge to another curve
        E2 = sagemath.EllipticCurve([-7, 6])
        new_curve = smanim(E2.plot(color="yellow", thickness=2, alpha=0.3, xmax=7, ymin=-5, ymax=5))
        shz(new_curve, 5)
        new_e1 = MathTex(r"y^2 = x^3", r" - 7\,", " x ", " + 6")
        new_e1.to_corner(UL)
        shz(new_e1, 5)
        self.play(
            Transform(curve, new_curve),
            Transform(e1, new_e1),
            run_time=1
        )
        self.wait(1)

        # try to give lots of curves
        ABs = [(-7,6), (-4,1), (9,1), (0,2), (-3,-1)]
        for A,B in ABs:
            E2 = sagemath.EllipticCurve([A, B])
            new_curve = smanim(E2.plot(color="yellow", thickness=2, alpha=0.3, xmax=7, ymin=-5, ymax=5))
            shz(curve, 5)
            if A >= 0:
                Astr = fr"+{A}\,"
            else:
                Astr = fr"-{-A}\,"
            if B >= 0:
                Bstr = fr"+{B}"
            else:
                Bstr = fr"-{-B}"
            new_e1 = MathTex(r"y^2 = x^3 ", Astr, " x ", Bstr)
            new_e1.to_corner(UL)
            self.play(
                Transform(curve, new_curve),
                Transform(e1, new_e1),
                run_timr=10)
            self.wait(1)


# now render it
if __name__ == "__main__":
    with tempconfig({"renderer": "opengl", "quality": "medium_quality", "preview": True}):
        scene = FirstScene()
        scene.render()
