r"""
Part of the bsd_video

This uses the characters and introduces
elliptic curves with some 2d pictures.

Many things are precalculated in
basic_calculation_with_favourite_elliptic_curve.ipynb

TODO:
* The cloud should grow to a certain size and then this
is the background in all other scenes including the 3D one.
* Switch back to original curve and variation through
examples is not done yet

"""

from manim import *
import sage.all as sagemath
from character import StudentChar, two_characters_standing_next_to_each_other
from msage import smanim
from tools import *


def little_curve_icon():
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

def family_of_curves(tt):
    if tt == .5:
        ttt = sagemath.RR(.49)
    else:
        ttt = sagemath.RR(tt)

    E = sagemath.EllipticCurve([2*ttt-4,2*ttt+1])
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
        ## 1.1 From real to maths world

        self.next_section("Walk on path")
        background_image = natural_initial_background()
        self.add(background_image)

        # chars on stand on the path
        stte = two_characters_standing_next_to_each_other(to_corner=False)
        stte_start = vec(1.2, -0.415)
        stte.move_to(stte_start)
        st = stte[0]
        te = stte[1]
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

        def icon_movement(tt):
            s = icon_start
            s += vec(0, tt**2)
            return s

        icon.add_updater(lambda m : m.move_to(icon_movement(t.get_value())))

        # put in the correct order
        self.remove(thoughts, icon, title, stte, background_image)
        self.add(background_image, thoughts, title, icon, stte)

        self.play(t.animate.set_value(1),
                  run_time=7,
                  rate_func=rate_functions.ease_in_out_sine)
        self.wait(1)

        self.clear()
        self.add(thoughts[0])
        self.add(stte)

# -------------------------------------------

        # # 1.2
        # what are elliptic curves
        # TODO : Transition for the background. Maybe better in an editor?
        # or keep the bubble for later.
        self.next_section("1.2 What are elliptic curves?")
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
        grid.add(Line(vec(0, -4), vec(0, 4), color=WHITE, stroke_width=2))
        xline = Line(vec(-7, 0, .1), vec(7, 0, .1), color=WHITE, stroke_width=2)
        grid.add(xline)
        shz(grid, 1)
        self.add(grid)

        axex = Arrow(start=vec(0,0),
                     end=vec(6.5,0),
                     buff=0,
                     stroke_width=2,
                     tip_length=0.3,
                     tip_shape=BetterCurvyPointyTip,
                     color=WHITE)
        axey = Arrow(start=vec(0, 0),
                     end=vec(0, 3.7),
                     buff=0,
                     stroke_width=2,
                     tip_length=0.3,
                     tip_shape=BetterCurvyPointyTip,
                     color=WHITE)
        label_x = MathTex(r"x")
        label_x.scale(.8)
        label_x.move_to(vec(6.5, -0.4))
        label_y = MathTex(r"y")
        label_y.scale(.8)
        label_y.move_to(vec(0.4, 3.5))
        labelled_axes = VGroup(axex, axey, label_x, label_y)
        shz(labelled_axes,1)

        E = sagemath.EllipticCurve([-4, 1])
        curve = smanim(E.plot(color="yellow", thickness=2, alpha=0.3, xmax=7, ymin=-5, ymax=5))
        shz(curve, 5)
        self.add(curve)
        ellc.add_updater(lambda m: m.next_to(e1, DOWN))
        self.play(Create(curve),
                  e1.animate.to_corner(UL),
                  FadeIn(labelled_axes),
                  run_time=1)
        self.wait(1)

        #  opengl problem in SurroundingRectangle solved in tools
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
        old_curve = curve.copy()
        self.play(
            Transform(curve, new_curve),
            Transform(e1, new_e1),
            run_time=1
        )
        self.remove(curve)
        self.wait(1)

        # switch back
        new_e1 = MathTex(r"y^2 = x^3", r" +A\,", " x ", " + B")
        new_e1.to_corner(UL)
        shz(new_e1, 5)
        self.remove(framebox1, framebox2)
        self.play(
            FadeTransform(e1, new_e1),
            Transform(new_curve, old_curve),
            run_time=1
        )
        curve = old_curve

        # now run through a family of curves
        self.remove(curve, new_curve, old_curve)
        t = ValueTracker(0)
        curve.add_updater(lambda m:m.become(family_of_curves(t.get_value())))
        self.add(curve)
        self.play(t.animate.set_value(1), run_time=10, rate_func=rate_functions.there_and_back)

        self.wait(1)

        # they are all symmetric ?
        self.clear()
        self.add(bgr, grid, labelled_axes, te, st)
        self.remove(e1, new_e1, new_curve, curve, framebox1, framebox2)
        E = sagemath.EllipticCurve([-4, 1])
        curve = smanim(E.plot(color="yellow", thickness=2, alpha=0.3, xmax=7, ymin=-5, ymax=5))
        shz(curve, 5)
        e1 = MathTex(r"(-y)^2 = y^2 = x^3", r"- 4\,", " x ", "+ 1")
        e1.to_corner(UL)
        ellc.next_to(e1, DOWN)
        arrow_1 = Arrow(vec(-1, -1.8), vec(-1,1.8), stroke_width=3, buff=0, tip_shape=BetterCurvyPointyTip)
        arrow_1r = Arrow(vec(-1, 1.8), vec(-1, -1.8), stroke_width=3, buff=0, tip_shape=BetterCurvyPointyTip)
        arrow_2 = Arrow(vec(2.8, -3), vec(2.8, 3), stroke_width=3, buff=0, tip_shape=BetterCurvyPointyTip)
        arrow_2r = Arrow(vec(2.8, 3), vec(2.8, -3), stroke_width=3, buff=0, tip_shape=BetterCurvyPointyTip)
        self.play(Create(curve),
                  Create(e1),
                  run_time=.3)
        self.play(Create(arrow_1),
                  Create(arrow_1r),
                  FadeIn(arrow_2),
                  FadeIn(arrow_2r),
                  run_time=.4)
        self.wait(2)


# now render it
if __name__ == "__main__":
    with tempconfig({"renderer": "cairo", "quality": "medium_quality", "preview": True}):
        scene = FirstScene()
        scene.render()
