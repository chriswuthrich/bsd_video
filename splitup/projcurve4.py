r"""
split scene
3.5 to 3.12

"""

from manim import *
import sage.all as sagemath
from tools import vec, shz, dot_on_curve, fading_numberplane
from msage import smanim

class ToProjectiveCurve3b(Scene):

    def construct(self):

        eq_standard_curve = MathTex(r"y^2 = x^3", r"- 4\,", " x ", "+ 1")
        eq_standard_curve.to_corner(UL)
        eq_standard_curve.move_to(ORIGIN)
        self.add(eq_standard_curve)

        eq_xy_in_Q = MathTex(r"x,y\in\mathbb{Q}", color=WHITE)
        eq_xy_in_Q.next_to(eq_standard_curve, DOWN)
        shz(eq_xy_in_Q, 2)

        eq_xy_in_Q.to_corner(UL)
        eq_xy_in_Q.shift(0.2 * RIGHT)
        self.play(FadeIn(eq_xy_in_Q), run_time=.5)
        self.wait(2)
        self.play(Indicate(eq_xy_in_Q), run_time=1)

        eq_x_frac_X_Z_y_frac_Y_Z = MathTex(r"x=\frac{X}{Z}\ \ y = \frac{Y}{Z}")
        eq_x_frac_X_Z_y_frac_Y_Z.next_to(eq_xy_in_Q, DOWN)
        eq_x_frac_X_Z_y_frac_Y_Z.to_edge(LEFT)
        eq_x_frac_X_Z_y_frac_Y_Z.shift(.2 * RIGHT)
        eq_XYZ_in_Z = MathTex(r"X,Y,Z\in\mathbb{Z}")
        eq_XYZ_in_Z.next_to(eq_x_frac_X_Z_y_frac_Y_Z, DOWN)
        eq_XYZ_in_Z.to_edge(LEFT)
        eq_XYZ_in_Z.shift(.2 * RIGHT)
        self.play(FadeIn(eq_XYZ_in_Z), FadeIn(eq_x_frac_X_Z_y_frac_Y_Z), run_time=1)
        self.play(Indicate(eq_x_frac_X_Z_y_frac_Y_Z), run_time=3)
        self.wait(2)

        self.play(eq_standard_curve.animate(run_time=2).move_to(UP))
        eq_subsitute_frations = MathTex(r"\Bigl(\frac{Y}{Z}\Bigr)^2 = \Bigl(\frac{X}{Z}\Bigr)^3",
                                        r"- 4\,", r" \Bigl(\frac{X}{Z}\Bigr)", "+ 1")
        eq_subsitute_frations.next_to(eq_standard_curve, 2 * DOWN)
        self.play(FadeIn(eq_subsitute_frations))
        self.wait(2)

        eq_multiply_by_Z = MathTex(r"\bigl\vert \cdot Z^3")
        eq_multiply_by_Z.next_to(eq_subsitute_frations, RIGHT, buff=1)
        self.play(FadeIn(eq_multiply_by_Z))
        self.play(Indicate(eq_multiply_by_Z), run_time=2)

        eq_projective_standard_curve = MathTex(r"Y^2 Z = X^3", r"- 4\,", r" XZ^2 ", r"+ Z^3")
        eq_projective_standard_curve.next_to(eq_subsitute_frations, 2 * DOWN)
        self.play(FadeIn(eq_projective_standard_curve), run_time=.5)
        self.wait(2)

        self.play(FadeOut(eq_subsitute_frations),
                  FadeOut(eq_multiply_by_Z),
                  eq_projective_standard_curve.animate().next_to(eq_standard_curve, 2 * DOWN),
                  run_time=2)
        self.wait(2)
        self.remove(eq_subsitute_frations, eq_multiply_by_Z)

        eq_XYZ_minus_scale = MathTex(r"(X,Y,Z)\sim (-X, -Y, -Z)")
        eq_x_fraction_minus_scale = MathTex(r"x=\frac{X}{Z}=\frac{-X}{-Z}")
        semicolon_text = Text(":")
        scaling_text = VGroup(eq_XYZ_minus_scale, semicolon_text, eq_x_fraction_minus_scale)
        scaling_text.arrange(RIGHT, buff=.3)
        scaling_text.next_to(eq_projective_standard_curve, 1.5 * DOWN)
        self.play(FadeIn(scaling_text), run_time=.5)
        # self.add(index_labels(seq_XYZ_minus_scale[0])) # shows parts

        eq_two = MathTex(r"2")
        eq_two_on_top = eq_two.copy().move_to(eq_x_fraction_minus_scale[0][6].get_center())
        eq_two_on_bottom = eq_two.copy().move_to(eq_x_fraction_minus_scale[0][9].get_center())
        eq_two_in_x = eq_two.copy().move_to(eq_XYZ_minus_scale[0][9].get_center())
        eq_two_in_y = eq_two.copy().move_to(eq_XYZ_minus_scale[0][12].get_center())
        eq_two_in_z = eq_two.copy().move_to(eq_XYZ_minus_scale[0][15].get_center())
        all_twos = VGroup(eq_two_on_top, eq_two_on_bottom, eq_two_in_x, eq_two_in_y, eq_two_in_z)
        all_twos.shift(.045 * UP)
        self.wait(2)
        self.play(Transform(eq_XYZ_minus_scale[0][9], eq_two_in_x),
                  Transform(eq_XYZ_minus_scale[0][12], eq_two_in_y),
                  Transform(eq_XYZ_minus_scale[0][15], eq_two_in_z),
                  Transform(eq_x_fraction_minus_scale[0][6], eq_two_on_top),
                  Transform(eq_x_fraction_minus_scale[0][9], eq_two_on_bottom),
                  run_time=.7
                  )
        self.wait(2)

        eq_x_of_O = MathTex(r"X=0,")
        eq_y_of_O = MathTex(r"Y=1,")
        eq_z_of_O = MathTex(r"Z=0")
        point_at_oo = VGroup(eq_x_of_O, eq_y_of_O, eq_z_of_O)
        point_at_oo.arrange(RIGHT, buff=.4)
        point_at_oo.next_to(scaling_text, DOWN)
        self.play(FadeIn(point_at_oo), run_time=.5)

        # print(f"{self.renderer.camera.phi=}, {self.renderer.camera.theta=}, {self.renderer.camera.frame_center=}")
        # self.renderer.camera.phi=0,
        # self.renderer.camera.theta=-1.5707963267948966,
        # self.renderer.camera.frame_center=array([0., 0., 0.])
        self.wait(1)

# now render it
if __name__ == "__main__":
    config.renderer = "cairo"
    config.format = "png"
    config.transparent = True
    config.write_to_movie = False
    #config.preview = True

    # Optional but recommended
    config.background_color = None

    scene = ToProjectiveCurve3b()
    scene.render()
