r"""
Part of the bsd_video

This contains the intro
of projective coordinates
by going to a 3D scene.

The change of coordinates for the
fake projective curve is done in
calculation_for_fake_projective_curve.ipynb

TODO : The 3-d scene at the end needs some work

"""

from manim import *
import sage.all as sagemath
from character import two_characters_standing_next_to_each_other
from msage import smanim
from tools import *


def fake_numberplane():
    """
    Projective version of number plane for 3D view at infinity
    The point (0:1:0) is at (0,100),
    The points (1:0:0), (0,0) and (0,4) are fixed
    """
    colour = TEAL
    colour2 = TEAL_A
    thickness = 0.001
    v = VGroup()
    ymin = -10  # don't draw behind the camera.

    # filled rectangle at the horizon
    nu2 = 70
    yy = 100 * nu2 / (nu2 + 96)
    p = Polygon(
        vec(-50, yy), vec(50, yy), vec(100, 100), vec(-100, 100),
        stroke_width=0,
        fill_color=colour,
        fill_opacity=.8,
        color=colour)
    shz(p, -1)
    v.add(p)

    # horizontal lines y=const
    for yy in range(ymin, nu2):
        y2 = 100*yy/(yy+96)
        v.add(Line3D(
            vec(-30, y2),
            vec(30, y2),
            thickness=thickness,
            color=colour2 if yy != 0 else WHITE))

    # lines x=const meeting at O
    nu1 = 100
    for xx in range(-nu1, nu1):
        v.add(Line3D(
            vec(xx * (1 - ymin / 100), ymin),
            vec(0, 100),
            thickness=thickness,
            color=colour if xx != 0 else WHITE))

    # horizont line
    v.add(Line3D(
        vec(-100, 100),
        vec(100, 100),
        color=WHITE,
        thickness=thickness))

    # redraw axes
    v.add(Line3D(
            vec(-30, 0),
            vec(30, 0),
            thickness=thickness,
            color=WHITE))
    v.add(Line3D(
            vec(0, ymin),
            vec(0, 100),
            thickness=thickness,
            color=WHITE))

    return v


def fake_curve():
    """
    Create a version of the elliptic curve y^2 = x^3-4x+1
    in the fake number plane where (0:1:0) is at (0,100)
    Calculations done in notebook
    """
    def f(x, y):
        return 2500*x**3 - x*y**2 + 1843/80*y**3 + 200*x*y - 9213/4*y**2 - 10000*x - 75*y + 2500

    v = ImplicitFunction(f, x_range=[-15, 15], y_range=[-10, 99], color=YELLOW, stroke_width=6)
    # v.add_points_as_corners(vec(0,100))
    # v.append_points([v.points[-1], v.points[-1], vec(0,100), vec(0,100)])
    # print(v.points[-1], len(v.points))
    v.add_line_to(vec(0, 100))
    # print(v.points[-20:])

    # w = VGroup([v])
    # w.add(Line3D(v.points[-100],vec(0,100), color=RED, stroke_width=6))
    return v


class SecondScene(ThreeDScene):

    def construct(self):

        # 2 Rational points on projective curves

        # copied from first scene:
        background = cloud_background()
        shz(background, -1)
        stte = two_characters_standing_next_to_each_other()

        grid = fading_numberplane(x_tip=True,
                                  y_tip=True,
                                  x_label=True,
                                  y_label=True,
                                  axes_fading=False)
        shz(grid, 0)

        standard_E = sagemath.EllipticCurve([-4, 1])
        curve = smanim(standard_E.plot(color="yellow", thickness=2, alpha=0.3, xmax=7, ymin=-5, ymax=5))
        eq_standard_curve = MathTex(r"y^2 = x^3", r"- 4\,", " x ", "+ 1")
        eq_standard_curve.to_corner(UL)
        shz([curve, stte, eq_standard_curve], 2)
        self.add(background, grid,  stte, eq_standard_curve, curve)

        # 2.1 Rational points
        self.next_section("2.1 Rational points")
        # finds one rational point
        eq_xy_in_Q = MathTex(r"x,y\in\mathbb{Q}", color=YELLOW)
        eq_xy_in_Q.next_to(eq_standard_curve, DOWN)
        shz(eq_xy_in_Q, 2)
        self.play(FadeIn(eq_xy_in_Q))
        self.wait()

        eq_xy_in_Q.set_color(WHITE)
        eq_x_0_y_pm_1 = MathTex(r"x=0,\ y=\pm 1")
        eq_x_0_y_pm_1.next_to(eq_xy_in_Q, DOWN)
        shz(eq_x_0_y_pm_1, 2)
        point_colour = BLUE_B
        point_radius = .07
        P01 = dot_on_curve(vec(0, -1), colour=point_colour, radius=point_radius, z_index=10)
        P02 = dot_on_curve(vec(0, 1), colour=point_colour, radius=point_radius, z_index=10)
        self.add(eq_x_0_y_pm_1)
        self.play(Create(P01),
                  FadeIn(P02),
                  run_time=1)

        self.play(Indicate(eq_x_0_y_pm_1),
                  Flash(P02.get_center()),
                  Flash(P01.get_center()),
                  run_time=1)
        self.wait(1)

        # there are many more on this example
        eq_pt0 = MathTex(r"(0,\pm 1),")
        eq_pt1 = MathTex(r"(2,\pm 1)")
        P11 = dot_on_curve(vec(2, 1, .1), colour=point_colour, radius=point_radius, z_index=10)
        shz(P11, 10)
        P12 = dot_on_curve(vec(2, -1, .1), colour=point_colour, radius=point_radius, z_index=10)  # not on top?
        shz(P12, 10)
        eq_pt2 = MathTex(r"(-1,\pm 2),")
        P21 = dot_on_curve(vec(-1, 2, .05), colour=point_colour, radius=point_radius, z_index=10)
        P22 = dot_on_curve(vec(-1, -2, .1), colour=point_colour, radius=point_radius, z_index=10)
        eq_pt3 = MathTex(r"(-2,\pm 1)")
        P31 = dot_on_curve(vec(-2, 1, .1), colour=point_colour, radius=point_radius, z_index=10)
        P32 = dot_on_curve(vec(-2, -1, .1), colour=point_colour, radius=point_radius, z_index=10)
        eq_pt4 = MathTex(r"(\tfrac{1}{4}, \pm\tfrac{1}{8}),")
        P41 = dot_on_curve(vec(.25, .125,.1), colour=point_colour, radius=point_radius, z_index=10)
        P42 = dot_on_curve(vec(.25, -.125,.1), colour=point_colour, radius=point_radius, z_index=10)
        eq_pt5 = MathTex(r"(-\tfrac{7}{4}, \pm\tfrac{13}{8})")
        P51 = dot_on_curve(vec(-7./4, 13./8,.1), colour=point_colour, radius=point_radius, z_index=10)
        P52 = dot_on_curve(vec(-7./4, -13/8.,.1), colour=point_colour, radius=point_radius, z_index=10)

        eq_pt0.next_to(eq_standard_curve, DOWN)
        eq_pt0.to_edge(LEFT)
        eq_pt1.next_to(eq_pt0, RIGHT)
        eq_pt2.next_to(eq_pt0, DOWN)
        eq_pt3.next_to(eq_pt2, RIGHT)
        eq_pt4.next_to(eq_pt2, DOWN)
        eq_pt5.next_to(eq_pt4, RIGHT)

        self.remove(eq_x_0_y_pm_1, eq_xy_in_Q)
        self.add(eq_pt0, P01, P02)

        self.add(eq_pt1, P11, P12)
        self.play(Flash(P11.get_center()),
                  Flash(P12.get_center()),
                  run_time=1)
        self.wait(1)

        self.add(eq_pt2, P21, P22)
        self.play(Flash(P21.get_center()),
                  Flash(P22.get_center()),
                  run_time=1)
        self.add(P21, P22, eq_pt3, P31, P32)
        self.play(Flash(P31.get_center()),
                  Flash(P32.get_center()),
                  run_time=1)
        self.add(eq_pt4, P41, P42)
        self.play(Flash(P41.get_center()),
                  Flash(P42.get_center()),
                  run_time=1)

        self.add(eq_pt5, P51, P52)
        self.play(Flash(P51.get_center()),
                  Flash(P52.get_center()),
                  run_time=1)

        # one really large height point
        self.wait(1)
        self.remove(eq_pt0, eq_pt1, eq_pt2, eq_pt3, eq_pt4, eq_pt5)
        # (6250080/33884041 : 102194916251/197239002661 :1)
        x_numerator = 6250080
        x_denominator = 33884041
        y_numerator = 102194916251
        y_denominator = 197239002661
        x_text = r"\tfrac{" + str(x_numerator) + r"}{" + str(x_denominator) + r"}"
        y_text = r"\tfrac{" + str(y_numerator) + r"}{" + str(y_denominator) + r"}"
        eq_pt6 = MathTex(r"(" + x_text + r", \pm" + y_text + r")")
        P61 = dot_on_curve(vec(x_numerator * 1. / x_denominator, y_numerator * 1. / y_denominator, .1),
                           colour=point_colour,
                           radius=point_radius,
                           z_index=10)
        P62 = dot_on_curve(vec(x_numerator * 1. / x_denominator, -y_numerator * 1. / y_denominator, .1),
                           colour=point_colour,
                           radius=point_radius,
                           z_index=10)

        eq_pt6.next_to(eq_standard_curve, DOWN)
        eq_pt6.to_edge(LEFT)
        shz(eq_pt6, 2)
        self.add(eq_pt6, P61, P62)
        self.play(Flash(P61.get_center()),
                  Flash(P62.get_center()),
                  run_time=1)

        # 2.2
        # Passage from affine to projective
        self.next_section("2.2 Passage to projective equation")
        # self.clear()
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=.2)
        eq_standard_curve.move_to(ORIGIN)
        self.add(background, eq_standard_curve, stte)

        eq_xy_in_Q.to_corner(UL)
        eq_xy_in_Q.shift(0.2*RIGHT)
        self.play(FadeIn(eq_xy_in_Q))
        self.play(Indicate(eq_xy_in_Q), run_time=1)
        eq_x_frac_X_Z_y_frac_Y_Z = MathTex(r"x=\frac{X}{Z}\ \ y = \frac{Y}{Z}")
        eq_x_frac_X_Z_y_frac_Y_Z.next_to(eq_xy_in_Q, DOWN)
        eq_x_frac_X_Z_y_frac_Y_Z.to_edge(LEFT)
        eq_x_frac_X_Z_y_frac_Y_Z.shift(.2*RIGHT)
        eq_XYZ_in_Z = MathTex(r"X,Y,Z\in\mathbb{Z}")
        eq_XYZ_in_Z.next_to(eq_x_frac_X_Z_y_frac_Y_Z, DOWN)
        eq_XYZ_in_Z.to_edge(LEFT)
        eq_XYZ_in_Z.shift(.2*RIGHT)
        self.play(FadeIn(eq_XYZ_in_Z), FadeIn(eq_x_frac_X_Z_y_frac_Y_Z), run_time=1)
        self.play(Indicate(eq_x_frac_X_Z_y_frac_Y_Z), FadeIn(eq_XYZ_in_Z), run_time=1)

        self.play(eq_standard_curve.animate(run_time=1).move_to(UP))
        eq_subsitute_frations = MathTex(r"\Bigl(\frac{Y}{Z}\Bigr)^2 = \Bigl(\frac{X}{Z}\Bigr)^3",
                                        r"- 4\,", r" \Bigl(\frac{X}{Z}\Bigr)", "+ 1")
        eq_subsitute_frations.next_to(eq_standard_curve, 2*DOWN)
        self.play(FadeIn(eq_subsitute_frations))

        eq_multiply_by_Z = MathTex(r"\bigl\vert \cdot Z^3")
        eq_multiply_by_Z.next_to(eq_subsitute_frations, RIGHT, buff=1)
        self.play(FadeIn(eq_multiply_by_Z))
        self.play(Indicate(eq_multiply_by_Z), run_time=1)

        eq_projective_standard_curve = MathTex(r"Y^2 Z = X^3", r"- 4\,", r" XZ^2 ", r"+ Z^3")
        eq_projective_standard_curve.next_to(eq_subsitute_frations, 2*DOWN)
        self.play(FadeIn(eq_projective_standard_curve))
        self.wait(1)

        self.play(FadeOut(eq_subsitute_frations),
                  FadeOut(eq_multiply_by_Z),
                  eq_projective_standard_curve.animate().next_to(eq_standard_curve, 2*DOWN),
                  run_time=2)
        self.wait()
        self.remove(eq_subsitute_frations, eq_multiply_by_Z)

        eq_XYZ_minus_scale = MathTex(r"(X,Y,Z)\sim (-X, -Y, -Z)")
        eq_x_fraction_minus_scale = MathTex(r"x=\frac{X}{Z}=\frac{-X}{-Z}")
        semicolon_text = Text(":")
        scaling_text = VGroup(eq_XYZ_minus_scale,  semicolon_text, eq_x_fraction_minus_scale)
        scaling_text.arrange(RIGHT, buff=.3)
        scaling_text.next_to(eq_projective_standard_curve, 1.5*DOWN)
        self.play(FadeIn(scaling_text))
        # self.add(index_labels(seq_XYZ_minus_scale[0])) # shows parts

        eq_two = MathTex(r"2")
        eq_two_on_top = eq_two.copy().move_to(eq_x_fraction_minus_scale[0][6].get_center())
        eq_two_on_bottom = eq_two.copy().move_to(eq_x_fraction_minus_scale[0][9].get_center())
        eq_two_in_x = eq_two.copy().move_to(eq_XYZ_minus_scale[0][9].get_center())
        eq_two_in_y = eq_two.copy().move_to(eq_XYZ_minus_scale[0][12].get_center())
        eq_two_in_z = eq_two.copy().move_to(eq_XYZ_minus_scale[0][15].get_center())
        all_twos = VGroup(eq_two_on_top, eq_two_on_bottom, eq_two_in_x, eq_two_in_y, eq_two_in_z)
        all_twos.shift(.045*UP)
        self.wait()
        self.play(Transform(eq_XYZ_minus_scale[0][9], eq_two_in_x),
                  Transform(eq_XYZ_minus_scale[0][12], eq_two_in_y),
                  Transform(eq_XYZ_minus_scale[0][15], eq_two_in_z),
                  Transform(eq_x_fraction_minus_scale[0][6], eq_two_on_top),
                  Transform(eq_x_fraction_minus_scale[0][9], eq_two_on_bottom),
                  run_time=1
                  )
        self.wait()

        eq_x_of_O = MathTex(r"X=0,")
        eq_y_of_O = MathTex(r"Y=1,")
        eq_z_of_O = MathTex(r"Z=0")
        point_at_oo = VGroup(eq_x_of_O, eq_y_of_O, eq_z_of_O)
        point_at_oo.arrange(RIGHT, buff=.4)
        point_at_oo.next_to(scaling_text, DOWN)
        self.play(FadeIn(point_at_oo))
        self.wait()

        # print(f"{self.renderer.camera.phi=}, {self.renderer.camera.theta=}, {self.renderer.camera.frame_center=}")
        # self.renderer.camera.phi=0,
        # self.renderer.camera.theta=-1.5707963267948966,
        # self.renderer.camera.frame_center=array([0., 0., 0.])
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=.2)
        # build up everything
        self.clear()
        background = cloud_background()
        shz(background, -2)
        self.add(background)
        numberplane_for_3d = fake_numberplane()
        shz(numberplane_for_3d, 1)
        stte = two_characters_standing_next_to_each_other()
        shz(stte, 1)
        self.add(numberplane_for_3d, stte)
        projective_curve = fake_curve()
        shz(projective_curve, +2)
        self.add(projective_curve)

        # transform points to the 3d picture in fake coordinates
        for P in [P01, P02, P11, P12, P21, P22, P31, P32, P41, P42, P51, P52, P61, P62]:
            xP = P.get_center()[0]
            yP = P.get_center()[1]
            this_pt = dot_on_3dcurve(vec(96*xP/(96+yP), 100*yP/(96+yP), 0.1), point_colour, 0.05)
            shz(this_pt, 3)
            self.add(this_pt)

        # point at infinity
        pt_at_inf = dot_on_3dcurve(vec(0, 95, .1), radius=.35, colour=YELLOW)
        shz(pt_at_inf,3)

        text_at_inf = MathTex(r"(X=0,\,Y=1,\,Z=0)")
        text_at_inf.rotate(PI/2, axis=RIGHT)
        text_at_inf.move_to(vec(1, 1, 6))

        arrow_at_inf = Arrow3D(vec(1, 1, 5.5), vec(.1, 1, 4.1), color=WHITE)
        pointing_at_inf = VGroup(text_at_inf, arrow_at_inf)

        total_time_of_camera_move = 10.
        time_it_stands_still = 4.

        # what_happens_during_the_camera_move = Succession(
        #     Wait((total_time_of_camera_move-time_it_stands_still)/2),
        #     Add(pt_at_inf),
        #     FadeIn(pointing_at_inf, run_time=.05*total_time_of_camera_move),
        #     Wait(.9*time_it_stands_still),
        #     FadeOut(pointing_at_inf, run_time=.05*total_time_of_camera_move)
        # )
        what_happens_during_the_camera_move = Add(pt_at_inf, pointing_at_inf)

        my_there_and_back_with_pause = lambda tt : rate_functions.there_and_back_with_pause(tt, pause_ratio=time_it_stands_still/total_time_of_camera_move)

        self.move_camera(phi=PI/2,
                         frame_center=(0, -10, 5),
                         run_time=total_time_of_camera_move,
                         rate_func=my_there_and_back_with_pause,
                         added_anims=[what_happens_during_the_camera_move])

        self.wait(3)


#

# now render it
if __name__ == "__main__":
    scene = SecondScene()
    scene.render()
