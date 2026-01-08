r"""
Part of the bsd_video

This uses the characters and introduces
elliptic curves with some 2d pictures.

Many things are precalculated in
basic_calculation_with_favourite_elliptic_curve.ipynb

"""

# TODO:
# currently the characters move out of the picture, but I can't see what is wrong with stte_movement
# One might add a bag of coins and 1000000 $ later

from manim import *
import sage.all as sagemath
from character import two_characters_standing_next_to_each_other
from msage import smanim
from tools import *




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


class FirstScene(Scene):

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
        stte_x_move = stte_target_position[0] - stte_start[0]
        stte_y_move = stte_target_position[1] - stte_start[1]

        def stte_movement(tt):
            return stte_start + vec(stte_x_move * tt ** 2, stte_y_move * tt, 10/100)

        print(stte_start, stte_target_position, stte_x_move, stte_y_move, stte_movement(1.))

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
        shz(background, -2)
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
        self.clear()
#

# now render it
if __name__ == "__main__":
    scene = FirstScene()
    scene.render()
