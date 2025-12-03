

from manim import *
import sage.all as sagemath
# from character import two_characters_standing_next_to_each_other
from msage import smanim
from tools import shz, fading_numberplane


# import json


def shorter_family_of_curves(tt):
    r"""
    Family of elliptic curves, like in scene 1,
    but this stops at the singular curve in the middle
    """
    # avoid the singular curve
    if tt == .5:
        ttt = sagemath.RR(0.4999)
    else:
        ttt = sagemath.RR(tt)

    E = sagemath.EllipticCurve([2*ttt-4, 2*ttt+1])
    v = smanim(E.plot(color=rgb_to_color([0, 155*(tt/2), 155]),
                      thickness=2,
                      alpha=0.3,
                      xmax=7,
                      ymin=-5,
                      ymax=5))
    shz(v, 5)
    return v

def forth_back_stop(tt):
    if tt < .5:
        return 4.8*tt*tt*(1-tt/3)
    else:
        return 8.*tt**3-18*tt**2+12*tt-3/2

class Family(Scene):
    def construct(self):
        #self.camera.background_color = WHITE  # transparent

        bk = fading_numberplane(x_tip=True,
                                y_tip=True,
                                x_label=True,
                                y_label=True,
                                axes_fading=False,
                                colours=[GREEN, BLACK])
        self.add(bk)

        standard_E = sagemath.EllipticCurve([ -4, 1 ])
        standard_curve = smanim(standard_E.plot(color=rgb_to_color([0, 0, 155]), thickness=2, alpha=0.3, xmax=7, ymin=-5, ymax=5))

        self.add(standard_curve)
        self.wait(5)

        t = ValueTracker(0)

        # equation with changing coefficients with 2 digits
        eq_changing_curve = always_redraw(
            lambda: MathTex(
                f"y^2 = x^3 - {4 - 2*t.get_value():.2f}x + {2*t.get_value() + 1:.2f}",
                color=BLACK
            ).to_corner(UL)
        )

        shz(eq_changing_curve, 5)
        standard_curve.add_updater(lambda m: m.become(shorter_family_of_curves(t.get_value())))
        self.add(standard_curve, eq_changing_curve)

        self.play(t.animate.set_value(1), run_time=10, rate_func=forth_back_stop)
        self.remove_updater(eq_changing_curve)
        eq_singular_curve = MathTex(r"y^2 = x^3 - 3\,x + 2 ", color=BLACK)
        eq_singular_curve.to_corner(UL)
        self.play(FadeOut(eq_changing_curve), FadeIn(eq_singular_curve))
        self.wait(1)
        eq_factored = MathTex(r"y^2=(x-1)^2(x+2) ", color=BLACK)
        eq_factored.next_to(eq_singular_curve, direction=DOWN)
        self.play(FadeIn(eq_factored), run_time=.4)
        self.wait(1)
        eq_general_curve = MathTex(r"y^2 = x^3 + A x + B ", color=BLACK)
        eq_general_curve.to_corner(UL)
        eq_delta = MathTex(r"4\,A^3+27\,B^2=0", color=BLACK)
        eq_delta.next_to(eq_changing_curve, DOWN, aligned_edge=LEFT)
        self.play(Transform(eq_singular_curve, eq_general_curve),
                  FadeOut(eq_factored),
                  FadeIn(eq_delta))
        self.wait(4)




#  now render it
if __name__ == "__main__":

    scene = Family()
    scene.render()
