r"""

Temporary complete scene combining what is in the other files


"""

from manim import *
import sage.all as sagemath
from character import two_characters_standing_next_to_each_other
from msage import smanim


from tools import (thought_bubble,
                   cloud_background,
                   fading_numberplane,
                   glow_dot,
                   MySurroundingRectangle,
                   standard_curve,
                   dot_on_curve,
                   CurvyPointyTip)

from first_scene import *
from second_scene import *
from third_scene import *
from fourth_scene import *
from fifth_scene import *


class AllScenes(ThreeDScene):

    def construct(self):

        # 1
        # 1.1 From real to maths world

        self.next_section("Walk on path")
        background_image = natural_initial_background()
        self.add(background_image)

        # chars on stand on the path
        stte = two_characters_standing_next_to_each_other(to_corner=False)
        stte_start = vec(1.2, -0.415)
        stte.move_to(stte_start)
        self.add(stte)
        self.wait(1)

        # st thinks of zeta(s)
        # TODO: Should we add 1000000 $ ?
        cloud_centre = vec(-1, 2.6)
        thoughts = thought_bubble(cloud_centre, 0.85)
        # shift small bubbles a little
        thoughts[1][0].shift(vec(0, 0.2))
        thoughts[1][1].shift(vec(0.2, 0.2))
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
        icon = little_curve_icon()
        icon.move_to(cloud_centre + vec(1.3, 0))
        shz(icon, 5)
        self.play(FadeIn(icon))
        self.wait(.3)

        # and the curve kicks out the zeta
        t = ValueTracker(0)

        # the elliptic curve icon moves and changes colour
        def icon_movement(tt):
            """
            bouncing function cooked up with cubic splines
            """
            # this was created in
            # bump_rate_function_for_first_scene.ipynb
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
                                             - vec(icon_movement(t.get_value()), 0)))
        # white goes to yellow:
        icon.add_updater(lambda m: m.set_color(rgb_to_color([255, 255, 255 * (1 - t.get_value())])))

        # the zeta gets kicked out and vanishes
        def zeta_movement(tt):
            if tt < 0.5:
                return 0
            else:
                return 6 * (tt - 0.5)

        def zeta_opacity(tt):
            if tt < 0.5:
                return 1
            else:
                return 2 * (1 - tt)

        zeta.add_updater(lambda m: m.move_to(cloud_centre
                                             - vec(zeta_movement(t.get_value()), 0)))
        zeta.add_updater(lambda m: m.set_opacity(zeta_opacity(t.get_value())))

        self.play(t.animate.set_value(1), run_time=2, rate_func=linear)
        self.play(icon.animate.move_to(cloud_centre), run_time=0.3)
        self.wait(.7)
        self.remove(zeta)

        # bubble grows, title appears, and characters move to the lower left corner
        t = ValueTracker(0)

        # bubble grows
        thoughts.clear_updaters()
        original_cloud = thoughts[0].copy()
        self.remove(thoughts[1])

        def scale_cloud_updater(m):
            if t.get_value() < .72:
                scale_factor = 1 + 9*t.get_value()
            else:
                scale_factor = 7.48  # value at .72
            mo = original_cloud.copy().scale(scale_factor)
            m.become(mo)

        # move to the centre
        def cloud_movement(tt):
            s = (1-tt) * cloud_centre
            s += vec(0, 0, 1/100)
            return s

        thoughts.add_updater(lambda m: m.move_to(cloud_movement(t.get_value())))
        thoughts.add_updater(scale_cloud_updater)

        # title
        title = Paragraph("The Birch and Swinnerton-Dyer", "conjecture",
                          font_size=40,
                          color=YELLOW,
                          opacity=1,
                          alignment="center"
                          )
        title.move_to(vec(-1, 3))
        shz(title, 5)

        def title_updater(m):
            new_title = Paragraph("The Birch and Swinnerton-Dyer", "conjecture",
                                  font_size=40,
                                  color=YELLOW,
                                  opacity=1,
                                  alignment="center"
                                  )
            new_title.scale(0.1 + t.get_value())
            new_title.move_to((1 - t.get_value()) * vec(-1, 3))
            shz(new_title, 5)
            m.become(new_title)

        title.add_updater(title_updater)

        # characters move
        stte_target_position = two_characters_standing_next_to_each_other(to_corner=True).get_center()

        def stte_movement(tt):
            s = stte_start
            s += vec(0, 0, 10/100)
            a = stte_target_position[0] - stte_start[0]
            b = stte_target_position[1] - stte_start[1]
            s += vec(a * tt ** 2, b * tt)
            return s

        stte.add_updater(lambda m: m.move_to(stte_movement(t.get_value())))

        # the icon moves out quickly
        icon.clear_updaters()  # not needed
        icon_start = icon.get_center()

        def icon_second_movement(tt):
            s = icon_start
            s += vec(0, np.sqrt(tt))
            return s

        icon.add_updater(lambda m: m.move_to(icon_second_movement(t.get_value())))

        # put in the correct order
        self.remove(thoughts, icon, title, stte, background_image)
        self.add(background_image, thoughts, title, icon, stte)

        self.play(t.animate.set_value(1),
                  run_time=7,
                  rate_func=rate_functions.ease_in_out_sine)
        self.remove(icon)
        self.wait(1)

# -------------------------------------------

        # # 1.2
        # what are elliptic curves
        self.next_section("1.2 What are elliptic curves?")
        self.clear()
        thoughts.clear_updaters()
        stte.clear_updaters()
        background = cloud_background()
        shz(background, -1)
        self.add(background, stte)
        self.wait(.2)

        # equations appear central
        eq_standard_curve = MathTex(r"y^2 = x^3", r"- 4\,", " x ", "+ 1")
        shz(eq_standard_curve, 5)
        self.play(FadeIn(eq_standard_curve))
        self.wait(1)
        text_elliptic_curve = Text("Elliptic curve", font="Noto Sans")
        text_elliptic_curve.next_to(eq_standard_curve, DOWN)
        self.play(FadeIn(text_elliptic_curve))
        self.wait(1)

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
        self.wait(1)

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
                  run_time=2,
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
        self.add(background, grid, stte, curve)
        eq_symmetric = MathTex(r"(-y)^2 = y^2 = x^3+A\,x+B")
        eq_symmetric.to_corner(UL)
        self.add(eq_symmetric)
        # text_elliptic_curve.next_to(eq_standard_curve, DOWN)
        arrow_1 = Arrow(vec(-1, -1.8), vec(-1, 1.8), stroke_width=3, buff=0, tip_shape=CurvyPointyTip)
        arrow_1r = Arrow(vec(-1, 1.8), vec(-1, -1.8), stroke_width=3, buff=0, tip_shape=CurvyPointyTip)
        arrow_2 = Arrow(vec(2.8, -3), vec(2.8, 3), stroke_width=3, buff=0, tip_shape=CurvyPointyTip)
        arrow_2r = Arrow(vec(2.8, 3), vec(2.8, -3), stroke_width=3, buff=0, tip_shape=CurvyPointyTip)
        self.play(Create(arrow_1),
                  Create(arrow_1r),
                  FadeIn(arrow_2),
                  FadeIn(arrow_2r),
                  run_time=1)
        self.wait(2)




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
        shz(grid, 1)

        standard_E = sagemath.EllipticCurve([-4, 1])
        curve = smanim(standard_E.plot(color="yellow", thickness=2, alpha=0.3, xmax=7, ymin=-5, ymax=5))
        shz(curve, 5)
        eq_standard_curve = MathTex(r"y^2 = x^3", r"- 4\,", " x ", "+ 1")
        eq_standard_curve.to_corner(UL)
        shz(eq_standard_curve, 5)
        self.add(background, grid,  stte, eq_standard_curve, curve)

        # 2.1 Rational points
        self.next_section("2.1 Rational points")
        # finds one rational point
        eq_xy_in_Q = MathTex(r"x,y\in\mathbb{Q}", color=YELLOW)
        eq_xy_in_Q.next_to(eq_standard_curve, DOWN)
        self.play(FadeIn(eq_xy_in_Q))
        self.wait()

        eq_xy_in_Q.set_color(WHITE)
        eq_x_0_y_pm_1 = MathTex(r"x=0,\ y=\pm 1")
        eq_x_0_y_pm_1.next_to(eq_xy_in_Q, DOWN)
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
        P12 = dot_on_curve(vec(2, -1, .2), colour=point_colour, radius=point_radius, z_index=10)  # not on top?
        shz(P12, 3)
        eq_pt2 = MathTex(r"(-1,\pm 2),")
        P21 = dot_on_curve(vec(-1, 2, .05), colour=point_colour, radius=point_radius, z_index=10)
        P22 = dot_on_curve(vec(-1, -2, .02), colour=point_colour, radius=point_radius, z_index=10)
        eq_pt3 = MathTex(r"(-2,\pm 1)")
        P31 = dot_on_curve(vec(-2, 1), colour=point_colour, radius=point_radius, z_index=10)
        P32 = dot_on_curve(vec(-2, -1), colour=point_colour, radius=point_radius, z_index=10)
        eq_pt4 = MathTex(r"(\tfrac{1}{4}, \pm\tfrac{1}{8}),")
        P41 = dot_on_curve(vec(.25, .125), colour=point_colour, radius=point_radius, z_index=10)
        P42 = dot_on_curve(vec(.25, -.125), colour=point_colour, radius=point_radius, z_index=10)
        eq_pt5 = MathTex(r"(-\tfrac{7}{4}, \pm\tfrac{13}{8})")
        P51 = dot_on_curve(vec(-7./4, 13./8), colour=point_colour, radius=point_radius, z_index=10)
        P52 = dot_on_curve(vec(-7./4, -13/8.), colour=point_colour, radius=point_radius, z_index=10)

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
        P61 = dot_on_curve(vec(x_numerator * 1. / x_denominator, y_numerator * 1. / y_denominator),
                           colour=point_colour,
                           radius=point_radius,
                           z_index=10)
        P62 = dot_on_curve(vec(x_numerator * 1. / x_denominator, -y_numerator * 1. / y_denominator),
                           colour=point_colour,
                           radius=point_radius,
                           z_index=10)

        eq_pt6.next_to(eq_standard_curve, DOWN)
        eq_pt6.to_edge(LEFT)
        self.add(eq_pt6, P61, P62)
        self.play(Flash(P61.get_center()),
                  Flash(P62.get_center()),
                  run_time=1)

        # 2.2
        # Passage from affine to projective
        self.next_section("2.2 Passage to projective equation")
        self.clear()
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
        self.clear()
        # TODO : point at infinity + label, cloud shaped background, grid on top
        self.add(background)
        numberplane_for_3d = fake_numberplane()
        shz(numberplane_for_3d, 1)
        self.add(numberplane_for_3d, stte)
        self.add(fake_curve())

        # transform points to the 3d picture in fake coordinates
        for P in [P01, P02, P11, P12, P21, P22, P31, P32, P41, P42, P51, P52, P61, P62]:
            xP = P.get_center()[0]
            yP = P.get_center()[1]
            P.move_to(vec(96*xP/(96+yP), 100*yP/(96+yP)))
            self.add(P)
        self.add(Dot3D(vec(0, 100, .1), radius=.3, color=YELLOW))

        self.move_camera(phi=PI/2,
                         frame_center=(0, -10, 5),
                         run_time=5)  # will be slower later
        self.wait(3)


        # 3.1 Count global points
        self.next_section("3.1 Count global points")
        self.add(cloud_background())
        stte = two_characters_standing_next_to_each_other()
        self.add(stte)

        # Title comes in
        title_counting_rational_points = Text("Counting rational points", color=YELLOW)
        title_counting_rational_points.shift(2*UP)
        self.play(GrowFromCenter(title_counting_rational_points))
        self.wait(.5)

        # For some curves like $y^2=x^3-4x-2$ there are only four points.
        eq_curve_of_rank_0 = MathTex(r"y^2 = x^3 - 4\,x - 2")
        eq_curve_of_rank_0.to_corner(UL)
        shz(eq_curve_of_rank_0, 5)
        self.add(eq_curve_of_rank_0)
        self.play(FadeOut(title_counting_rational_points, shift=DOWN * 2, scale=1.5))
        self.wait(.5)

        # create curve
        grid = fading_numberplane(x_tip=True,
                                  y_tip=True,
                                  x_label=False,
                                  y_label=False,
                                  axes_fading=True
                                  )
        shz(grid, 1)
        rank_zero_E = sagemath.EllipticCurve([-2, 1])
        eq_curve_rank_zero = smanim(rank_zero_E.plot(color="yellow", thickness=2, alpha=0.3, xmax=7, ymin=-5, ymax=5))
        shz(eq_curve_rank_zero, 5)
        grid_and_curve_of_rank_zero = VGroup(grid, eq_curve_rank_zero)
        shift_grid = vec(2, 0)
        grid_and_curve_of_rank_zero.shift(shift_grid)
        self.add(grid_and_curve_of_rank_zero, stte)
        self.wait(1)

        point_colour = BLUE_B
        point_radius = .07
        one_point_outside = VGroup(
            dot_on_curve(vec(3.5, 3.6) + shift_grid, radius=point_radius, colour=point_colour),
            Arrow(vec(3.7, 3.6) + shift_grid, vec(3.8, 3.9) + shift_grid)
            )
        points_up_to_10 = [((0, 1), r"(0,1)", vec(.5, .4)),
               ((0, -1), r"(0,-1)", vec(.55, -.4)),
               ((1, 0), r"(1,0)", vec(.7, .3)),
               ((100, 100), r"(X=0,Y=1,Z=0)", vec(0, 0))]
        all_pts_and_labels = VGroup()
        self.add(all_pts_and_labels)
        for P, Pstr, sh in points_up_to_10:
            P_centre = vec(P[0] * 1., P[1] * 1.) + shift_grid
            eq_P_label = MathTex(Pstr, color=YELLOW)
            eq_P_label.move_to(P_centre + sh)
            if P[0] > 7.111 or P[1] > 4:  # point outside screen
                v = one_point_outside
                eq_P_label.move_to(ORIGIN).to_edge(UP).shift(1.7*RIGHT)
                point_to_flash = vec(3.5, 3.6) + shift_grid
            else:
                v = dot_on_curve(P_centre, colour=point_colour, radius=point_radius, z_index=10)
                point_to_flash = P_centre
            all_pts_and_labels.add(v, eq_P_label)
            self.play(Indicate(eq_P_label),
                      Flash(point_to_flash),
                      runtime=.7)
            self.wait(.1)

        # Back to favourite curve
        self.remove(eq_curve_of_rank_0, all_pts_and_labels)
        standard_E = sagemath.EllipticCurve([-4, 1])
        st_curve = smanim(standard_E.plot(color="yellow", thickness=2, alpha=0.3, xmax=7, ymin=-5, ymax=5))
        shz(st_curve, 5)
        curvepic = VGroup(grid, st_curve)
        curvepic.shift(shift_grid)
        eq_standard_curve = MathTex(r"{{y^2}}   = {{x}}^3- 4\, {{x}} +  {{1}}")
        shz(eq_standard_curve, 5)
        eq_standard_curve.to_corner(UL)
        self.add(eq_standard_curve)
        self.play(Transform(grid_and_curve_of_rank_zero, curvepic),
                  run_time=1
                  )
        self.wait(.5)
        eq_projective_standard_curve = MathTex(r"{{Y^2 Z}} = {{X}}^3- 4\,{{XZ^2}}+ {{Z^3}}")
        shz(eq_projective_standard_curve, 5)
        eq_projective_standard_curve.to_corner(UL)
        self.play(TransformMatchingTex(eq_standard_curve, eq_projective_standard_curve))
        self.play(eq_projective_standard_curve.animate.move_to(vec(0, -3.2)))
        self.wait(1)

        # list points of height < 10
        table_up_to_10, points_up_to_10, indices = list_of_points(10)
        eq_XYZ_less_10 = MathTex(r"\lvert X\rvert,\, \lvert Y \rvert,\, \lvert Z\rvert < 10")
        eq_XYZ_less_10.to_edge(UP)
        eq_XYZ_less_10.shift(vec(-.7, 0))
        self.play(FadeIn(table_up_to_10),
                  FadeIn(eq_XYZ_less_10),
                  run_time=1)
        self.wait(1)
        point_colour = BLUE_B
        point_radius = .07
        point_outside = VGroup(
            dot_on_curve(vec(3.5, 3.6) + shift_grid, radius=point_radius, colour=point_colour),
            dot_on_curve(vec(3.5, -3.6) + shift_grid, radius=point_radius, colour=point_colour),
            Arrow(vec(3.7, 3.6) + shift_grid, vec(3.8, 3.9) + shift_grid),
            Arrow(vec(3.7, -3.6) + shift_grid, vec(3.8, -3.9) + shift_grid),
            )
        point_outside_shows = False
        for i in range(1, len(points_up_to_10)):
            P = points_up_to_10[i]
            P_str = table_up_to_10[0][indices[i]:indices[i+1]]
            P_centre = vec(P[0]*1./P[2], P[1]*1./P[2]) + shift_grid
            minus_P_centre = vec(P[0]*1./P[2], - P[1]*1./P[2]) + shift_grid
            if P_centre[0] > 7.111 or P_centre[1] > 4:  # point outside screen
                self.add(point_outside)
                point_outside_shows = True
                point_to_flash = vec(3.5, 3.6) + shift_grid
                minus_point_to_flash = vec(3.5, -3.6) + shift_grid
            else:
                self.add(dot_on_curve(P_centre, colour=point_colour, radius=point_radius),
                         dot_on_curve(minus_P_centre, radius=point_radius, colour=point_colour))
                point_to_flash = P_centre
                minus_point_to_flash = minus_P_centre

            self.play(Indicate(P_str),
                      Flash(point_to_flash),
                      Flash(minus_point_to_flash),
                      runtime=.7)
            self.wait(.1)
            if point_outside_shows:
                self.remove(point_outside)

        self.play(FadeOut(table_up_to_10, eq_XYZ_less_10))

        # now list them of height < 100
        table_up_to_100, points_up_to_100, indices = list_of_points(100)
        eq_XYZ_less_100 = MathTex(r"\lvert X\rvert,\, \lvert Y \rvert,\, \lvert Z\rvert < 100")
        eq_XYZ_less_100.to_edge(UP)
        eq_XYZ_less_100.shift(vec(-.7, 0))
        self.play(FadeIn(table_up_to_100),
                  FadeIn(eq_XYZ_less_100),
                  run_time=1)
        self.wait()
        for i in range(len(points_up_to_10), len(points_up_to_100)):
            P = points_up_to_100[i]
            P_str = table_up_to_100[0][indices[i]:indices[i+1]]
            P_centre = vec(P[0]*1./P[2], P[1]*1./P[2]) + shift_grid
            minus_P_centre = vec(P[0]*1./P[2], - P[1]*1./P[2]) + shift_grid
            if P_centre[0] > 7.111 or P_centre[1] > 4:  # point outside screen
                self.add(point_outside)
                point_outside_shows = True
                point_to_flash = vec(3.5, 3.6) + shift_grid
                minus_point_to_flash = vec(3.5, -3.6) + shift_grid
            else:
                self.add(dot_on_curve(P_centre, colour=point_colour, radius=point_radius, z_index=10),
                         dot_on_curve(minus_P_centre, colour=point_colour, radius=point_radius, z_index=10))
                point_to_flash = P_centre
                minus_point_to_flash = minus_P_centre

            self.play(Indicate(P_str),
                      Flash(point_to_flash),
                      Flash(minus_point_to_flash),
                      runtime=.7)
            self.wait(.1)
            if point_outside_shows:
                self.remove(point_outside)
        self.play(FadeOut(table_up_to_100, eq_XYZ_less_100))

        # list up to height 1000
        table_up_to_1000, points_up_to_1000, indices = list_of_points(1000)
        eq_XYZ_less_1000 = MathTex(r"\lvert X\rvert,\, \lvert Y \rvert,\, \lvert Z\rvert < 1000")
        eq_XYZ_less_1000.to_edge(UP)
        eq_XYZ_less_1000.shift(vec(-.7, 0))

        # move up the list to reveal more points
        # opacity updater for new elements
        def op(i, tt):
            s = i - len(points_up_to_100)
            n = len(points_up_to_1000) - len(points_up_to_100)
            if tt < s/n:
                return 0
            elif tt < (s+1)/n:
                return n*tt-s
            else:
                return 1

        t = ValueTracker(0)
        start_v1 = vec(table_up_to_1000.get_center()[0], table_up_to_1000.get_center()[1])

        def place_v1(tt):
            return start_v1 + tt * vec(0, 3)

        table_up_to_1000.add_updater(lambda m: m.move_to(place_v1(t.get_value())))
        for i in range(len(points_up_to_100), len(points_up_to_1000)):
            for j in range(indices[i], indices[i+1]):
                # in the following the "i=i" is there to avoid late binding
                # otherwise all updaters will take the last value of i
                table_up_to_1000[0][j].add_updater(lambda m, i=i: m.set_opacity(op(i, t.get_value())))
        table_up_to_1000[0][-1].add_updater(lambda m, i=i: m.set_opacity(op(i, t.get_value())))
        # this was used to print the value on screen,
        # leave here if needed later elsewhere
        # temporary_t = DecimalNumber(
        #     t.get_value(),
        #     num_decimal_places=2,
        #     include_sign=False,
        # ).scale(.4)
        # temporary_t.add_updater(
        #     lambda m: m.set_value(t.get_value())
        # )
        # temporary_t.to_corner(UR)
        # self.add(temporary_t)
        self.add(table_up_to_1000)
        self.play(FadeIn(eq_XYZ_less_1000),
                  t.animate.set_value(1), run_time=3, rate_func=linear)

        self.wait(1)

        # Now define N and give a graph for this curve.
        self.clear()
        self.add(cloud_background(), stte)

        nt = MathTex(r"\mathcal{N}(T) = \# \Bigl\{ P \in E(\mathbb{Q})\ : " +
                     r"\ \lvert X\rvert,\,\lvert Y \rvert,\, \lvert Z\rvert \leqslant T \Bigr\}")
        nt.to_edge(UP)
        self.play(FadeIn(nt))
        # self.add(index_labels(nt[0]))
        self.wait(1)

        with open('data/nt_graph.json', 'r') as file:
            gra = json.load(file)

        gra_axes = Axes(
                        x_range=[0, 40, 10],
                        y_range=[0, 25, 5],
                        x_length=10,
                        y_length=5,
                        x_axis_config={"include_numbers": True, 'tip_shape': CurvyPointyTip},
                        y_axis_config={"include_numbers": True, 'tip_shape': CurvyPointyTip}
                        )
        label_x = MathTex(r"T")
        label_x.move_to(vec(5.5, -3))
        gra_nt = VMobject(color=YELLOW)
        gra_nt.set_points_as_corners([gra_axes.c2p(x, y) for x, y in gra[:40]])
        gra_nt.set_style(stroke_width=2)
        gra_shift = vec(1, 0)
        gra_axes.shift(gra_shift)
        gra_nt.shift(gra_shift)
        self.add(gra_axes, label_x)

        self.play(Create(gra_nt), run_time=3, rate_func=linear)
        self.wait()

        # 3.2 Counting modulo
        #
        self.next_section("3.2 Counting points modulo")
        self.clear()
        self.add(cloud_background(), stte)

        # Title comes in
        title_counting_rational_points = Text("Counting points modulo", color=YELLOW)
        title_counting_rational_points.shift(2*UP)
        self.play(GrowFromCenter(title_counting_rational_points))
        self.wait(.5)

        # equation in centre goes modulo
        eq_projective_standard_curve = MathTex(r"{{y^2}} {{=}} {{x^3- 4\,x + 1}}", color=YELLOW)
        self.add(eq_projective_standard_curve)
        eemod = MathTex(r"{{y^2}} {{\equiv}} {{x^3- 4\,x +1}} \pmod{10}", color=YELLOW)
        self.play(TransformMatchingTex(eq_projective_standard_curve, eemod),
                  FadeOut(title_counting_rational_points, shift=UP, scale=1.5))
        self.wait()
        self.play(eemod.animate.move_to(vec(1.4, -3.219)))
        self.wait(.5)

        # points from basic_calculation_with_favourite_elliptic_curve.ipynb
        pts_mod_ten = [(0, 1, 1), (2, 1, 1), (8, 1, 1), (9, 2, 1), (4, 3, 1),
                       (3, 4, 1), (5, 4, 1), (7, 4, 1), (3, 6, 1), (5, 6, 1),
                       (7, 6, 1), (4, 7, 1), (9, 8, 1), (0, 9, 1), (2, 9, 1),
                       (8, 9, 1), (8, 1, 2), (0, 3, 2), (4, 3, 2), (6, 3, 2),
                       (0, 7, 2), (4, 7, 2), (6, 7, 2), (8, 9, 2), (0, 1, 5),
                       (5, 2, 5), (0, 1, 0)]

        affine_pts_mod_ten = [(x, y) for (x, y, z) in pts_mod_ten if z == 1]
        pts_v = {(x, y, z): VGroup(MathTex(r"("+str(x)+r","+str(y)+r")").scale(.8),
                                   MathTex(r"("+str(x)+r","+str(y)+r"," + str(z) + ")").scale(.8))
                 for (x, y, z) in pts_mod_ten}

        for (x, y) in affine_pts_mod_ten:
            pts_v[(x, y, 1)].move_to(vec(.95*x-2.6, .4*y-2.2))
            self.play(FadeIn(pts_v[(x, y, 1)][0]), run_time=.1)
        self.wait(1)

        emod = MathTex(r"Y^2 Z \equiv X^3- 4\,XZ^2 + Z^3}} \pmod{10}", color=YELLOW)
        emod.move_to(eemod.get_center())
        equivmod = MathTex(r"(X,Y,Z)\sim \\ ({{3}}X, {{3}}Y, {{3}}Z)", color=YELLOW)

        equivmod.move_to(vec(-5, 0))

        self.play(FadeOut(eemod),
                  FadeIn(emod))
        self.wait()
        self.add(equivmod)
        self.wait(1)
        for (x, y) in affine_pts_mod_ten:
            self.play(FadeTransform(pts_v[(x, y, 1)][0], pts_v[(x, y, 1)][1]), run_time=0.1)
        i = 0

        # give points at infinity on two lines at the top
        separation_between_points = 2.
        for (x, y, z) in pts_mod_ten:
            if z != 1:
                if i < 6:
                    pts_v[(x, y, z)].move_to(vec(separation_between_points*(i-2.5), 3.3))
                    self.add(pts_v[(x, y, z)][1])
                else:
                    pts_v[(x, y, z)].move_to(vec(separation_between_points*(i-8), 2.7))
                    self.add(pts_v[(x, y, z)][1])
                i += 1
        self.wait()

        # graph the number of points modulo Q
        self.clear()
        self.add(cloud_background(), stte)
        mu = MathTex(r"\mathcal{M}(U) = \# E\bigl({}^{\mathbb{Z}}\!/\!{}_{U \mathbb{Z}}\bigr)")
        mu_text = MathTex(r"= \text{ number of solutions modulo }U.")
        mu_group = VGroup(mu, mu_text).arrange(RIGHT)
        mu_group.to_edge(UP)
        self.play(FadeIn(mu_group))
        self.wait(1)

        mu_graph = [[2, 3], [3, 7], [4, 8], [5, 9], [6, 21], [7, 12], [8, 24],
                    [9, 21], [10, 27], [11, 15], [12, 56], [13, 18], [14, 36],
                    [15, 63], [16, 48], [17, 25], [18, 63], [19, 25], [20, 72],
                    [21, 84], [22, 45], [23, 30], [24, 168], [25, 45], [26, 54],
                    [27, 63], [28, 96], [29, 22], [30, 189]]

        mu_val = [m[1] for m in mu_graph]
        mu_labels = [str(m[0]) if m[0] % 5 == 0 else "" for m in mu_graph]
        bc = BarChart(mu_val,
                      bar_names=mu_labels,
                      y_range=[0, 200, 50],
                      y_length=5,
                      tips=True,
                      x_axis_config={"tip_shape": CurvyPointyTip, "tip_height": 0.2},
                      y_axis_config={"tip_shape": CurvyPointyTip}
                      )
        bc.scale(.8)
        bc.shift(vec(1, 0))
        u_label = MathTex(r"U")
        u_label.move_to(vec(6.4, -2.3))
        self.add(u_label)
        self.play(Create(bc))
        self.wait()
#

        # 4 The conjecture
        # 4.1 State the conjecture
        self.next_section("4.1 State the conjecture")
        # recreate background
        self.add(cloud_background())
        stte = two_characters_standing_next_to_each_other()
        self.add(stte)

        # define N(T)
        eq_definition_of_nt = Tex(r"$\mathcal{N}(T) = " +
                                  r"\# \Bigl\{ P\in E(\mathbb{Q}) \, " +
                                  r": \, \lvert X\rvert, \lvert Y\rvert, " +
                                  r"\lvert Z\rvert \leq T \Bigr\} $")
        self.add(eq_definition_of_nt)
        # now add an animation counting points
        self.wait(2)

        eq_definition_of_mu = Tex(r"$\mathcal{M}(U) = \# E\bigl({}^{\mathbb{Z}}\!/\!{}_{U\mathbb{Z}}\bigr)$")
        self.remove(eq_definition_of_nt)
        self.add(eq_definition_of_mu)
        # add an animation counting points modulo increasing T
        self.wait(2)

        self.remove(eq_definition_of_mu)
        te_compare = Text("Compare")
        te_compare.shift(2*LEFT)

        rhs = VGroup()
        eq_nt = Tex(r"$\mathcal{N}(T)$")
        eq_equality_hash = Tex(r"$ = \# $")
        bounded_rational_solutions = Text("bounded \n" + "rational \n" + "solutions").scale(.8)
        nt_hash_bounded_rational_solutions = VGroup(eq_nt, eq_equality_hash, bounded_rational_solutions)
        nt_hash_bounded_rational_solutions.arrange(RIGHT, buff=0.2)

        mu_hash_solutions_modulo_u = mu()  # M(U) = # solutions modulo U

        eq_u_t_factorial = Tex(r"$U = T! = 1 \cdot 2 \cdots T$")
        rhs.add(nt_hash_bounded_rational_solutions,
                mu_hash_solutions_modulo_u,
                eq_u_t_factorial)
        rhs.arrange(DOWN, buff=1.1, aligned_edge=LEFT)
        rhs.shift(3.5*RIGHT)
        self.add(rhs)

        # change U to T!
        eq_t_factorial = Tex(r"$T!$")
        eq_u_in_mu_at_the_end = mu_hash_solutions_modulo_u[1][1][1]
        eq_t_factorial.shift(eq_u_in_mu_at_the_end.get_center())
        eq_t_factorial_again = Tex(r"$T!$")
        eq_u_in_mu_at_start = mu_hash_solutions_modulo_u[0][1]
        eq_t_factorial_again.shift(eq_u_in_mu_at_start.get_center())
        self.play(Transform(eq_u_in_mu_at_the_end, eq_t_factorial),
                  Transform(eq_u_in_mu_at_start, eq_t_factorial_again),
                  run_time=1)
        self.wait(2)

        self.remove(te_compare)
        complete_limit_formula = limit_expression()
        complete_limit_formula.scale(1.7)
        complete_limit_formula.shift(3*LEFT)
        # start with the bar of the fraction
        self.add(complete_limit_formula[1][1])  # ---
        self.wait(1)

        # move N(T)
        eq_nt_in_limit = complete_limit_formula[1][0][2][0]  # N(T)
        eq_nt_source = eq_nt.copy()
        path_nt = ArcBetweenPoints(eq_nt_source.get_center(), eq_nt_in_limit.get_center(), angle=PI/5)

        # moves m along the path_nt and scaling it at the same time
        def nt_updater(m, alpha):
            point = path_nt.point_from_proportion(alpha)
            scale = interpolate(1, eq_nt_in_limit.width/eq_nt_source.width, alpha)
            m.move_to(point)
            m.set(width=eq_nt_source.width * scale)

        self.play(UpdateFromAlphaFunc(eq_nt_source, nt_updater), run_time=3)
        self.wait(1)

        # add square and highlight it
        eq_square_in_limit = complete_limit_formula[1][0][2][1]  # "^2"
        self.add(eq_square_in_limit)
        self.play(Indicate(eq_square_in_limit), run_time=1)
        self.add(complete_limit_formula[1][0][2])
        self.remove(eq_nt_source)

        # move the M(T!) to the fraction
        eq_m_t_factorial_in_limit = complete_limit_formula[1][2]  # M(T!) target
        eq_m_t_factorial_source = VGroup(mu_hash_solutions_modulo_u[0][0],
                                         eq_t_factorial_again,
                                         mu_hash_solutions_modulo_u[0][2]).copy()
        path_mt = ArcBetweenPoints(eq_m_t_factorial_source.get_center(),
                                   eq_m_t_factorial_in_limit.get_center(),
                                   angle=- PI / 5)

        def mt_updater(m, alpha):
            point = path_mt.point_from_proportion(alpha)
            scale = interpolate(1, eq_m_t_factorial_in_limit.width/eq_m_t_factorial_source.width, alpha)
            m.move_to(point)
            m.set(width=eq_m_t_factorial_source.width * scale)

        self.play(UpdateFromAlphaFunc(eq_m_t_factorial_source, mt_updater), run_time=3)
        complete_limit_formula[1][2] = eq_m_t_factorial_source
        self.wait(1)

        self.add(complete_limit_formula[1][0])  # numerator
        self.wait(1)
        self.add(complete_limit_formula[0])   # lim
        self.wait(1)

        # centre the fraction and hide the definition
        self.play(FadeOut(mu_hash_solutions_modulo_u, eq_u_t_factorial, nt_hash_bounded_rational_solutions))
        self.play(complete_limit_formula.animate.move_to(vec(2, 1)), run_time=1)
        self.wait(1)

        conjecture = Text("Conjecture:", color=YELLOW)
        conjecture.shift(2.5*UP+4*LEFT)
        self.add(conjecture)
        converges_to_a = Text("converges to a")
        positive_real_number = Text("positive real number.")
        incomplete_conjecture = VGroup(complete_limit_formula, converges_to_a, positive_real_number)
        incomplete_conjecture.arrange(DOWN, aligned_edge=LEFT)
        converges_to_a.shift(.5*DOWN)
        positive_real_number.shift(.5*DOWN)
        self.add(incomplete_conjecture)
        self.wait(2)

        # 4.2
        # Evidence shown in graphs of the limit
        self.next_section("4.2 Show evidence")
        self.clear()
        self.add(cloud_background(), stte)

        # data created in illustrate_conj_plots.ipynb
        li = load_list("data/plotpts_curve_aa-4_up_to_9.json")

        # ValueTracker to animate max x-value
        t = ValueTracker(3)  # start at 1000 = 10^3
        x_max = lambda tt: 10**tt
        ticks = lambda tt: 10**(np.floor(tt)-1)

        def get_axes():
            axes = Axes(
                        x_range=[0, x_max(t.get_value()), ticks(t.get_value())],
                        y_range=[0, 7, 1],
                        x_length=10,
                        y_length=5,
                        x_axis_config={"include_numbers": False, "include_tip": False},
                        y_axis_config={"include_numbers": True, "include_tip": False}
                        )

            # Create and add a custom tip for the x-axis
            x_tip = CurvyPointyTip().scale(0.3)
            x_tip.next_to(axes.x_axis.get_end(), RIGHT, buff=0)
            axes.x_axis.add(x_tip)

            # Create and add a custom tip for the y-axis
            y_tip = ArrowSquareTip().scale(0.3)
            y_tip.next_to(axes.y_axis.get_end(), UP, buff=0)
            axes.y_axis.add(y_tip)

            floor_t = sagemath.floor(t.get_value())
            i = 10**floor_t
            label = MathTex(f"10^{str(floor_t)}").scale(0.8)
            label.next_to(axes.c2p(i, 0), DOWN)
            axes.add(label)
            label_before = MathTex(f"10^{str(floor_t-1)}").scale(0.8)
            label_before.next_to(axes.c2p(i/10, 0), DOWN)
            axes.add(label_before)
            if t.get_value() < np.log10(5) + floor_t:
                i = floor_t - 1
            else:
                i = floor_t
            label_in_middle = MathTex(f"5\\cdot 10^{str(i)}").scale(0.8)
            label_in_middle.next_to(axes.c2p(5*10**i, 0), DOWN)
            axes.add(label_in_middle)
            axes.shift(vec(1, 0))
            return axes

        axes = always_redraw(get_axes)
        self.add(axes)

        def get_graph():
            axes = get_axes()
            v = VMobject(color=YELLOW)
            list_of_visible_points = [np.array([x, y]) for x, y in li if x < 0.95 * x_max(t.get_value())]
            v.set_points_as_corners([axes.c2p(x, y) for x, y in list_of_visible_points])
            return v

        graph_to_be_redrawn = always_redraw(get_graph)
        self.add(graph_to_be_redrawn)
        self.wait(2)

        # play from 10^3 to 10^(9)
        self.play(t.animate.set_value(9),
                  run_time=15,
                  rate_func=rate_functions.ease_in_out_sine)
        self.wait(2)

        # compare to other curves
        self.clear()
        self.add(cloud_background(), stte)
        # plot several in logarithmic coordinates
        axes_for_log_plot = Axes(x_range=[3, 9, 1],
                                 y_range=[0, 7, 1],
                                 x_length=10,
                                 y_length=5,
                                 x_axis_config={"include_numbers": False, 'tip_shape': CurvyPointyTip},
                                 y_axis_config={"include_numbers": True, 'tip_shape': CurvyPointyTip}
                                 )
        for i in range(3, 9):
            label = MathTex(f"10^{str(i)}").scale(0.7)
            label.next_to(axes_for_log_plot.c2p(i, 0), DOWN)
            axes_for_log_plot.add(label)

        shift_the_full_graph = vec(1, 1)
        axes_for_log_plot.shift(shift_the_full_graph)
        self.add(axes_for_log_plot)

        # first draw the usual curve
        li = load_list(f"data/plotpts_curve_aa-4_up_to_9.json")
        log_graph = VMobject(color=YELLOW)
        log_graph.set_points_as_corners([axes_for_log_plot.c2p(np.log10(x), y) for x, y in li if x > 1000])
        log_graph.set_style(stroke_width=2)
        eq_changing_curve = MathTex(r"y^2 = x^3 - 4\,x + 1 ")
        eq_changing_curve.to_edge(DOWN)
        self.add(log_graph, eq_changing_curve)
        previous_log_graph = log_graph
        self.wait(2)
        self.remove(eq_changing_curve)

        # for each A draw the new draw and fade the old
        for aa in [-3, -2, -1, 0, 1, 2, 3, 4]:
            li = load_list(f"data/plotpts_curve_aa{aa}_up_to_9.json")
            log_graph = VMobject(color=YELLOW)
            log_graph.set_points_as_corners([axes_for_log_plot.c2p(np.log10(x), y) for x, y in li if x > 1000])
            log_graph.set_style(stroke_width=2)
            if aa < -1:
                eq_changing_curve = MathTex(f"y^2 = x^3 - {-aa} \\,x + 1 ")
            elif aa == -1:
                eq_changing_curve = MathTex(r"y^2 = x^3 \ - x + 1 ")
            elif aa == 0:
                eq_changing_curve = MathTex(r"y^2 = x^3 \phantom{-4\,x}+ 1 ")
            elif aa == 1:
                eq_changing_curve = MathTex(r"y^2 = x^3 \ + x + 1 ")
            else:
                eq_changing_curve = MathTex(f"y^2 = x^3 + {aa} \\,x + 1 ")
            eq_changing_curve.to_edge(DOWN)
            self.add(eq_changing_curve)
            self.play(Create(log_graph),
                      FadeOut(previous_log_graph, rate_func=rate_functions.ease_out_circ),
                      Indicate(eq_changing_curve),
                      run_time=2)
            self.remove(eq_changing_curve)
            previous_log_graph = log_graph

        self.wait(1)

        # point out the jumps in the last one
        eq_jump_point_1 = MathTex(r"\bigl(\tfrac{2664}{49}, \pm \tfrac{137593}{343}\bigr)")
        eq_jump_point_2 = MathTex(r"\bigl(-\tfrac{4319}{21904}, \pm\tfrac{1462833}{3241792}\bigr)")
        eq_jump_points = VGroup(eq_jump_point_1, eq_jump_point_2)
        eq_jump_points.arrange(RIGHT, buff=1)
        eq_jump_points.to_edge(DOWN)
        eq_jump_points.shift(vec(1.5, 0))
        x_jump_point_1 = axes_for_log_plot.c2p(np.log10(137593), 0)[0]
        x_jump_point_2 = axes_for_log_plot.c2p(np.log10(3241792), 0)[0]
        point_out_pt1 = Arrow(vec(x_jump_point_1 - 1.5, 2),
                              vec(x_jump_point_1 - 0.02, 0.4),
                              tip_shape=CurvyPointyTip,
                              color=WHITE)
        point_out_pt2 = Arrow(vec(x_jump_point_2 - 1.5, 2),
                              vec(x_jump_point_2 - 0.02, 0.4),
                              tip_shape=CurvyPointyTip,
                              color=WHITE)
        dashed_line_down_1 = DashedLine(vec(x_jump_point_1, .4),
                                        axes_for_log_plot.c2p(np.log10(137593), 0),
                                        stroke_width=1.5,
                                        color=WHITE,
                                        dash_length=.1)
        dashed_line_down_2 = DashedLine(vec(x_jump_point_2, .4),
                                        axes_for_log_plot.c2p(np.log10(3241792), 0),
                                        stroke_width=1.5,
                                        color=WHITE,
                                        dash_length=.1)
        height_jump_point_1 = MathTex(r"137\,593", color=WHITE)
        height_jump_point_1.scale(.5).move_to(axes_for_log_plot.c2p(np.log10(137593), 0) + vec(.45, .25))
        height_jump_point_2 = MathTex(r"3\,241\,792", color=WHITE)
        height_jump_point_2.scale(.5).move_to(axes_for_log_plot.c2p(np.log10(3241792), 0) + vec(.55, .25))

        self.play(Succession(FadeIn(point_out_pt1),
                             FadeIn(dashed_line_down_1),
                             FadeIn(height_jump_point_1),
                             FadeIn(eq_jump_point_1)),
                  run_time=1
                  )
        self.wait(.5)
        self.play(Succession(FadeIn(point_out_pt2),
                             FadeIn(dashed_line_down_2),
                             FadeIn(height_jump_point_2),
                             FadeIn(eq_jump_point_2)),
                  run_time=2
                  )

        self.wait()

        # now point out that singular curves behave differently
        # first show the family again, halting at the singular curve.
        self.clear()
        self.add(cloud_background(), stte)
        grid = fading_numberplane(x_tip=True,
                                  y_tip=True,
                                  x_label=True,
                                  y_label=True,
                                  axes_fading=True
                                  )
        shz(grid, 1)
        self.add(grid)

        standard_E = sagemath.EllipticCurve([-4, 1])
        st_curve = smanim(standard_E.plot(color="yellow", thickness=2, alpha=0.3, xmax=7, ymin=-5, ymax=5))

        t = ValueTracker(0)

        # equation with changing coefficients with 2 digits
        eq_changing_curve = always_redraw(
            lambda: MathTex(
                f"y^2 = x^3 - {4-t.get_value():.2f}x + {t.get_value()+1:.2f}",
                color=YELLOW
            ).to_corner(UL)
        )

        shz(eq_changing_curve, 5)
        st_curve.add_updater(lambda m: m.become(shorter_family_of_curves(t.get_value())))
        self.add(st_curve, eq_changing_curve)

        self.play(t.animate.set_value(1), run_time=2, rate_func=rate_functions.ease_in_out_sine)
        self.remove_updater(eq_changing_curve)
        eq_singular_curve = MathTex(r"y^2 = x^3 - 3\,x + 2 ", color=YELLOW)
        eq_singular_curve.to_corner(UL)
        self.play(FadeOut(eq_changing_curve), FadeIn(eq_singular_curve))
        self.wait(1)
        eq_general_curve = MathTex(r"y^2 = x^3 + A x + B ", color=YELLOW)
        eq_general_curve.to_corner(UL)
        eq_delta = MathTex(r"4\,A^3+27\,B^2=0")
        eq_delta.next_to(eq_changing_curve, DOWN, aligned_edge=LEFT)
        self.play(Transform(eq_singular_curve, eq_general_curve),
                  FadeIn(eq_delta),
                  run_time=0.5)
        self.wait(1)

        # then show that the graph drops quickly for the singular curve.
        self.clear()
        self.add(cloud_background(), stte)
        axes_for_log_plot = Axes(
                        x_range=[0, 1000, 200],
                        y_range=[0, 2, 1],
                        x_length=10,
                        y_length=5,
                        x_axis_config={"include_numbers": True, 'tip_shape': CurvyPointyTip},
                        y_axis_config={"include_numbers": True, 'tip_shape': CurvyPointyTip}
                        )
        shift_the_full_graph = vec(1, 1)
        axes_for_log_plot.shift(shift_the_full_graph)
        self.add(axes_for_log_plot)

        # first draw the usual curve
        li = load_list(f"data/singular_plot_points.json")
        log_graph = VMobject(color=YELLOW)
        log_graph.set_points_as_corners([axes_for_log_plot.c2p(x, y) for x, y in li if x > 10])
        log_graph.set_style(stroke_width=2)

        eq_changing_curve = MathTex(r"y^2 = x^3 - 3\,x + 2 ")
        eq_changing_curve.to_edge(DOWN)
        self.play(FadeIn(log_graph),
                  FadeIn(eq_changing_curve))
        self.wait(2)

        self.clear()
        self.add(cloud_background(), stte)
        axes_for_log_plot = Axes(
                        x_range=[0, 1000, 200],
                        y_range=[0, 10, 2],
                        x_length=10,
                        y_length=5,
                        x_axis_config={"include_numbers": True, 'tip_shape': CurvyPointyTip},
                        y_axis_config={"include_numbers": False, 'tip_shape': CurvyPointyTip}
                        )
        shift_the_full_graph = vec(1, 1)
        label = MathTex("1").scale(.7)
        label.next_to(axes_for_log_plot.c2p(0, 8), LEFT)
        axes_for_log_plot.add(label)
        for i in range(1, 5):
            s = str(10*i-50)
            label = MathTex(r"10^{" + s + "}").scale(0.7)
            label.next_to(axes_for_log_plot.c2p(0, 2*i-2), LEFT)
            axes_for_log_plot.add(label)
        axes_for_log_plot.shift(shift_the_full_graph)
        self.add(axes_for_log_plot)

        # first draw the usual curve
        li = load_list(f"data/singular_plot_points.json")
        log_graph = VMobject(color=YELLOW)
        log_graph.set_points_as_corners([axes_for_log_plot.c2p(x, np.log(y)/np.log(10)/5 + 8) for x, y in li if x > 10])
        log_graph.set_style(stroke_width=2)

        eq_changing_curve = MathTex(r"y^2 = x^3 - 3\,x + 2 ")
        eq_changing_curve.to_edge(DOWN)
        self.play(FadeIn(log_graph),
                  FadeIn(eq_changing_curve))
        self.wait(2)

        # restate conjecture
        self.clear()
        self.add(cloud_background(), stte)
        conjecture.to_corner(UL)
        self.add(complete_limit_formula, conjecture, incomplete_conjecture)
        text_if = Text("If").next_to(conjecture, RIGHT, buff=1)
        eq_discriminant = MathTex(r"A^3+27B^2\neq 0").scale(1.3)
        eq_discriminant.next_to(text_if, RIGHT)
        text_comma_then = Text(", then")
        text_comma_then.next_to(eq_discriminant, RIGHT, buff=0.1)
        # align them by hand
        text_if.shift(vec(0, .09))
        eq_discriminant.shift(vec(0, .04))
        text_comma_then.shift(vec(0, .03))
        self.add(text_if, eq_discriminant, text_comma_then)
        self.wait(1)




# now render it
if __name__ == "__main__":
    scene = AllScenes()
    scene.render()