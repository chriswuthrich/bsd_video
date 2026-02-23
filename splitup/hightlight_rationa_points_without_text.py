r"""
split scene
3.1 - 3.4
version with the text

no formulae either

"""

from manim import *
import sage.all as sagemath
from tools import vec, shz, dot_on_curve, fading_numberplane
from msage import smanim



class HighlightRationalPointsWithoutText(Scene):

    def construct(self):

        grid = fading_numberplane(x_tip=True,
                                  y_tip=True,
                                  x_label=True,
                                  y_label=True,
                                  axes_fading=False)
        shz(grid, 0)

        standard_E = sagemath.EllipticCurve([-4, 1])
        curve = smanim(standard_E.plot(color="yellow", thickness=2, alpha=0.3, xmax=7, ymin=-5, ymax=5))
        #eq_standard_curve = MathTex(r"y^2 = x^3", r"- 4\,", " x ", "+ 1")
        #eq_standard_curve.to_corner(UL)
        #shz([curve, eq_standard_curve], 2)
        self.add(grid, #eq_standard_curve,
                 curve)

        # 2.1 Rational points
        self.next_section("2.1 Rational points")
        # finds one rational point
        #eq_xy_in_Q = MathTex(r"x,y\in\mathbb{Q}", color=YELLOW)
        #eq_xy_in_Q.next_to(eq_standard_curve, DOWN)
        #shz(eq_xy_in_Q, 2)
        #self.play(FadeIn(eq_xy_in_Q), run_time=.3)
        self.wait(3)

        #eq_xy_in_Q.set_color(WHITE)
        #eq_x_0_y_pm_1 = MathTex(r"x=0,\ y=\pm 1")
        #eq_x_0_y_pm_1.next_to(eq_xy_in_Q, DOWN)
        #shz(eq_x_0_y_pm_1, 2)
        point_colour = BLUE_B
        point_radius = .07
        P01 = dot_on_curve(vec(0, -1), colour=point_colour, radius=point_radius, z_index=10)
        P02 = dot_on_curve(vec(0, 1), colour=point_colour, radius=point_radius, z_index=10)
        #self.add(eq_x_0_y_pm_1)
        self.play(Create(P01),
                  FadeIn(P02),
                  run_time=1)
        self.wait(1)
        self.play(#Indicate(eq_x_0_y_pm_1),
                  Flash(P02.get_center()),
                  Flash(P01.get_center()),
                  run_time=1)
        self.wait(4)

        # there are many more on this example
        #eq_pt0 = MathTex(r"(0,\pm 1),")
        #eq_pt1 = MathTex(r"(2,\pm 1)")
        P11 = dot_on_curve(vec(2, 1, .1), colour=point_colour, radius=point_radius, z_index=10)
        shz(P11, 10)
        P12 = dot_on_curve(vec(2, -1, .1), colour=point_colour, radius=point_radius, z_index=10)  # not on top?
        shz(P12, 10)
        #eq_pt2 = MathTex(r"(-1,\pm 2),")
        P21 = dot_on_curve(vec(-1, 2, .05), colour=point_colour, radius=point_radius, z_index=10)
        P22 = dot_on_curve(vec(-1, -2, .1), colour=point_colour, radius=point_radius, z_index=10)
        #eq_pt3 = MathTex(r"(-2,\pm 1)")
        P31 = dot_on_curve(vec(-2, 1, .1), colour=point_colour, radius=point_radius, z_index=10)
        P32 = dot_on_curve(vec(-2, -1, .1), colour=point_colour, radius=point_radius, z_index=10)
        #eq_pt4 = MathTex(r"(\tfrac{1}{4}, \pm\tfrac{1}{8}),")
        P41 = dot_on_curve(vec(.25, .125,.1), colour=point_colour, radius=point_radius, z_index=10)
        P42 = dot_on_curve(vec(.25, -.125,.1), colour=point_colour, radius=point_radius, z_index=10)
        #eq_pt5 = MathTex(r"(-\tfrac{7}{4}, \pm\tfrac{13}{8})")
        P51 = dot_on_curve(vec(-7./4, 13./8,.1), colour=point_colour, radius=point_radius, z_index=10)
        P52 = dot_on_curve(vec(-7./4, -13/8.,.1), colour=point_colour, radius=point_radius, z_index=10)

        #eq_pt0.next_to(eq_standard_curve, DOWN)
        #eq_pt0.to_edge(LEFT)
        #eq_pt1.next_to(eq_pt0, RIGHT)
        #eq_pt2.next_to(eq_pt0, DOWN)
        #eq_pt3.next_to(eq_pt2, RIGHT)
        #eq_pt4.next_to(eq_pt2, DOWN)
        #eq_pt5.next_to(eq_pt4, RIGHT)

        #self.remove(eq_x_0_y_pm_1, eq_xy_in_Q)
        self.add(#eq_pt0,
             P01, P02)

        self.add(#eq_pt1,
             P11, P12)
        self.play(Flash(P11.get_center()),
                  Flash(P12.get_center()),
                  run_time=1)
        self.wait(3)

        self.add(#eq_pt2,
             P21, P22)
        self.play(Flash(P21.get_center()),
                  Flash(P22.get_center()),
                  run_time=1)
        self.wait(1)
        self.add(P21, P22, #eq_pt3,
                  P31, P32)
        self.play(Flash(P31.get_center()),
                  Flash(P32.get_center()),
                  run_time=1)
        self.wait(1)
        self.add(#eq_pt4,
             P41, P42)
        self.play(Flash(P41.get_center()),
                  Flash(P42.get_center()),
                  run_time=1)
        self.wait(1)
        self.add(#eq_pt5,
             P51, P52)
        self.play(Flash(P51.get_center()),
                  Flash(P52.get_center()),
                  run_time=1)

        # one really large height point
        self.wait(1)
        #self.remove(eq_pt0, eq_pt1, eq_pt2, eq_pt3, eq_pt4, eq_pt5)
        # (6250080/33884041 : 102194916251/197239002661 :1)
        x_numerator = 6250080
        x_denominator = 33884041
        y_numerator = 102194916251
        y_denominator = 197239002661
        #x_text = r"\tfrac{" + str(x_numerator) + r"}{" + str(x_denominator) + r"}"
        #y_text = r"\tfrac{" + str(y_numerator) + r"}{" + str(y_denominator) + r"}"
        #eq_pt6 = MathTex(r"(" + x_text + r", \pm" + y_text + r")")
        P61 = dot_on_curve(vec(x_numerator * 1. / x_denominator, y_numerator * 1. / y_denominator, .1),
                           colour=point_colour,
                           radius=point_radius,
                           z_index=10)
        P62 = dot_on_curve(vec(x_numerator * 1. / x_denominator, -y_numerator * 1. / y_denominator, .1),
                           colour=point_colour,
                           radius=point_radius,
                           z_index=10)

        #eq_pt6.next_to(eq_standard_curve, DOWN)
        #eq_pt6.to_edge(LEFT)
        #shz(eq_pt6, 2)
        self.add(#eq_pt6,
             P61, P62)
        self.play(Flash(P61.get_center()),
                  Flash(P62.get_center()),
                  run_time=1)
        self.wait(1)

# now render it
if __name__ == "__main__":
    config.renderer = "cairo"
    config.format = "mp4"
    # config.transparent = True
    # config.write_to_movie = False

    # Optional but recommended
    config.background_color = BLACK

    scene = HighlightRationalPointsWithoutText()
    scene.render()
