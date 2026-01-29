r"""
split scene
2.1 to 2.8
version with the text at the same times
36 s.
"""

from manim import *
import sage.all as sagemath
from tools import vec, shz, MySurroundingRectangle, standard_curve, fading_numberplane, CurvyPointyTip
from msage import smanim



def family_of_curves(tt):
    if tt == .5:
        ttt = sagemath.RR(.49)
    else:
        ttt = sagemath.RR(tt)

    E = sagemath.EllipticCurve([2*ttt-4, 2*ttt+1])
    v = smanim(E.plot(color=rgb_to_color([255, 255*(1-tt), 0]),
                      thickness=2,
                      alpha=0.3,
                      xmax=7,
                      ymin=-5,
                      ymax=5))
    shz(v, 5)
    return v

class EllipticCurves2_with_text(Scene):

    def construct(self):

        eq_standard_curve = MathTex(r"y^2 = x^3", r"- 4\,", " x ", "+ 1")
        shz(eq_standard_curve, 5)
        self.play(FadeIn(eq_standard_curve))
        self.wait(4)
        text_elliptic_curve = Text("Elliptic curve", font="Noto Sans")
        text_elliptic_curve.next_to(eq_standard_curve, DOWN)
        self.play(FadeIn(text_elliptic_curve))
        self.wait(5)

        # plot elliptic curve, move equations out
        grid = fading_numberplane(x_tip=True,
                                  y_tip=True,
                                  x_label=True,
                                  y_label=True,
                                  axes_fading=False)
        curve = standard_curve()
        self.add(curve)

        text_elliptic_curve.add_updater(lambda m: m.next_to(eq_standard_curve, DOWN))

        self.play(Create(curve),
                  eq_standard_curve.animate.to_corner(UL),
                  FadeIn(grid),
                  run_time=1)
        self.wait(5)

        #  opengl problem in SurroundingRectangle solved in tools
        framebox1 = MySurroundingRectangle(eq_standard_curve[1], color=YELLOW, buff=.1)
        framebox2 = MySurroundingRectangle(eq_standard_curve[3], color=YELLOW, buff=.1)
        self.add(framebox1, framebox2)

        # merge to another curve and come back
        second_E = sagemath.EllipticCurve([-7, 6])
        second_curve = smanim(second_E.plot(color="yellow", thickness=2, alpha=0.3, xmax=7, ymin=-5, ymax=5))
        shz(second_curve, 5)
        eq_second_curve = MathTex(r"y^2 = x^3", r" - 7\,", " x ", " + 6")
        eq_second_curve.to_corner(UL)
        shz(eq_second_curve, 5)

        self.play(Transform(curve, second_curve),
                  Transform(eq_standard_curve, eq_second_curve),
                  run_time=3,
                  rate_func=rate_functions.there_and_back_with_pause
                  )
        self.wait(1)
        self.remove(framebox1, framebox2)

        # switch back
        eq_general_curve = MathTex(r"y^2 = x^3", r" +A\,", " x ", " + B")
        eq_general_curve.to_corner(UL)
        shz(eq_general_curve, 5)
        self.play(FadeOut(eq_standard_curve),
                  FadeIn(eq_general_curve),
                  run_time=1)
        self.wait(1)

        # run through a family of curves
        t = ValueTracker(0)
        curve.add_updater(lambda m: m.become(family_of_curves(t.get_value())))
        self.add(curve)
        self.play(t.animate.set_value(1),
                  run_time=10,
                  rate_func=rate_functions.there_and_back)
        self.wait(1)

        # they are all symmetric
        self.clear()
        self.add(grid, curve)
        eq_symmetric = MathTex(r"(-y)^2 = y^2 = x^3+A\,x+B")
        eq_symmetric.to_corner(UL)
        self.add(eq_symmetric)
        # text_elliptic_curve.next_to(eq_standard_curve, DOWN)
        arrow_1 = Arrow(vec(-1, -1.8), vec(-1, 1.8), stroke_width=3, buff=0, tip_shape=CurvyPointyTip)
        arrow_1r = Arrow(vec(-1, 1.8), vec(-1, -1.8), stroke_width=3, buff=0, tip_shape=CurvyPointyTip)
        arrow_2 = Arrow(vec(2.8, -3), vec(2.8, 3), stroke_width=3, buff=0, tip_shape=CurvyPointyTip)
        arrow_2r = Arrow(vec(2.8, 3), vec(2.8, -3), stroke_width=3, buff=0, tip_shape=CurvyPointyTip)

        arrows_pointing = AnimationGroup(FadeIn(arrow_1),
                                         FadeIn(arrow_1r),
                                         FadeIn(arrow_2),
                                         FadeIn(arrow_2r))
        self.play( arrows_pointing,
                  run_time=1)

        self.wait(3)


# now render it
if __name__ == "__main__":
    config.renderer = "cairo"
    config.format = "mov"
    config.transparent = True
    config.write_to_movie = True

    # Optional but recommended
    config.background_color = None

    scene = EllipticCurves2_with_text()
    scene.render()

