r"""
Part of the bsd_video

This will contain the intro
of projective coordinates
by going to a 3D scene.


"""

from manim import *
import sage.all as sagemath
from character import StudentChar
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

    # filled rectangle
    nu2 = 70
    yy = 100 * nu2 / (nu2 + 96)
    p = Polygon(
        vec(-50, yy), vec(50, yy), vec(100, 100), vec(-100, 100),
        stroke_width=0,
        fill_color=colour,
        fill_opacity=.9,
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
            color=colour2 if yy!=0 else WHITE))

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

        # copied from first scene:
        bgr = my_background()
        shz(bgr, -1)
        st = StudentChar()
        te = StudentChar(height=1.2, width=0.8, colour=GREEN, lid_colour=DARK_GRAY)
        st.scale(1)
        te.scale(1)
        stte = VGroup(st, te)
        stte.arrange()
        stte.to_corner(DL)
        grid = VGroup()
        grid.add(my_fading_numberplane())
        grid.add(Line(vec(0, -4), vec(0, 4), color=WHITE, stroke_width=2))
        xline = Line(vec(-7, 0, .1), vec(7, 0, .1), color=WHITE, stroke_width=2)
        grid.add(xline)
        shz(grid, 1)
        axex = Arrow(start=vec(0, 0),
                     end=vec(6.5, 0),
                     buff=0,
                     stroke_width=2,
                     tip_length=0.2,
                     tip_shape=BetterCurvyPointyTip,
                     color=WHITE)
        axey = Arrow(start=vec(0, 0),
                     end=vec(0, 3.7),
                     buff=0,
                     stroke_width=2,
                     tip_length=0.2,
                     tip_shape=BetterCurvyPointyTip,
                     color=WHITE)
        label_x = MathTex(r"x")
        label_x.scale(.8)
        label_x.move_to(vec(6.5, -0.4))
        label_y = MathTex(r"y")
        label_y.scale(.8)
        label_y.move_to(vec(0.4, 3.5))
        labelled_axes = VGroup(axex, axey, label_x, label_y)
        shz(labelled_axes, 1)
        E = sagemath.EllipticCurve([-4, 1])
        curve = smanim(E.plot(color="yellow", thickness=2, alpha=0.3, xmax=7, ymin=-5, ymax=5))
        shz(curve, 5)
        e1 = MathTex(r"y^2 = x^3", r"- 4\,", " x ", "+ 1")
        e1.to_corner(UL)
        shz(e1, 5)

        self.add(bgr, grid, labelled_axes, stte)
        self.add(e1, curve)

        # 2.1 Rational points

        self.next_section("2.1 Rational points")
        # finds one rational point
        xyQ = MathTex(r"x,y\in\mathbb{Q}", color=YELLOW)
        xyQ.next_to(e1, DOWN)
        self.play(FadeIn(xyQ))
        self.wait()
        xyQ.set_color(WHITE)
        pt = MathTex(r"x=0,\ y=\pm 1")
        pt.next_to(xyQ, DOWN)
        pointcolour = BLUE_B
        pointradius = .07
        P01 = Dot3D(vec(0, -1), color=pointcolour, radius=pointradius, z_index=10)
        P02 = Dot3D(vec(0, 1), color=pointcolour, radius=pointradius, z_index=10)
        self.add(pt)
        self.play(Create(P01),
                  FadeIn(P02),
                  run_time=1)

        self.play(Wiggle(pt),
                  Flash(P02.get_center()),
                  Flash(P01.get_center()),
                  run_time=1)
        self.wait(1)

        # there are many more on this example
        pt0 = MathTex(r"(0,\pm 1),")
        pt1 = MathTex(r"(2,\pm 1)")
        P11 = Dot3D(vec(2, 1, .1), color=pointcolour, radius=pointradius, z_index=10)
        shz(P11, 10)
        P12 = Dot3D(vec(2, -1, .2), color=pointcolour, radius=pointradius, z_index=10)
        shz(P12, 3)
        pt2 = MathTex(r"(-1,\pm 2),")
        P21 = Dot3D(vec(-1, 2, .05), color=pointcolour, radius=pointradius, z_index=10)
        P22 = Dot3D(vec(-1, -2, .02), color=pointcolour, radius=pointradius, z_index=10)
        pt3 = MathTex(r"(-2,\pm 1)")
        P31 = Dot3D(vec(-2, 1), color=pointcolour, radius=pointradius, z_index=10)
        P32 = Dot3D(vec(-2, -1), color=pointcolour, radius=pointradius, z_index=10)
        pt4 = MathTex(r"(\tfrac{1}{4}, \pm\tfrac{1}{8}),")
        P41 = Dot3D(vec(.25, .125), color=pointcolour, radius=pointradius, z_index=10)
        P42 = Dot3D(vec(.25, -.125), color=pointcolour, radius=pointradius, z_index=10)
        pt5 = MathTex(r"(-\tfrac{7}{4}, \pm\tfrac{13}{8})")
        P51 = Dot3D(vec(-7./4, 13./8), color=pointcolour, radius=pointradius, z_index=10)
        P52 = Dot3D(vec(-7./4, -13/8.), color=pointcolour, radius=pointradius, z_index=10)

        pt0.next_to(e1, DOWN)
        pt0.to_edge(LEFT)
        pt1.next_to(pt0, RIGHT)
        pt2.next_to(pt0, DOWN)
        pt3.next_to(pt2, RIGHT)
        pt4.next_to(pt2, DOWN)
        pt5.next_to(pt4, RIGHT)

        self.remove(pt, xyQ)
        self.add(pt0, P01, P02)

        self.add(pt1, P11, P12)
        self.play(Flash(P11.get_center()),
                  Flash(P12.get_center()),
                  run_time=1)
        self.wait(1)

        self.add(pt2, P21, P22)
        self.play(Flash(P21.get_center()),
                  Flash(P22.get_center()),
                  run_time=1)
        self.add(P21, P22, pt3, P31, P32)
        self.play(Flash(P31.get_center()),
                  Flash(P32.get_center()),
                  run_time=1)
        self.add(pt4, P41, P42)
        self.play(Flash(P41.get_center()),
                  Flash(P42.get_center()),
                  run_time=1)

        self.add(pt5, P51, P52)
        self.play(Flash(P51.get_center()),
                  Flash(P52.get_center()),
                  run_time=1)

        # one really large height point
        self.wait(1)
        self.remove(pt0, pt1, pt2, pt3, pt4, pt5)
        # (6250080/33884041 : 102194916251/197239002661 :1)
        x_numerator = 6250080
        x_denominator = 33884041
        y_numerator = 102194916251
        y_denominator = 197239002661
        x_text = r"\tfrac{" + str(x_numerator) + r"}{" + str(x_denominator) + r"}"
        y_text = r"\tfrac{" + str(y_numerator) + r"}{" + str(y_denominator) + r"}"
        pt6 = MathTex(r"(" + x_text + r", \pm" + y_text + r")")
        P61 = Dot(vec(x_numerator * 1. / x_denominator, y_numerator * 1. / y_denominator), color=pointcolour,
                  radius=pointradius, z_index=10)
        P62 = Dot(vec(x_numerator * 1. / x_denominator, -y_numerator * 1. / y_denominator), color=pointcolour,
                  radius=pointradius, z_index=10)

        pt6.next_to(e1, DOWN)
        pt6.to_edge(LEFT)
        self.add(pt6, P61, P62)
        self.play(Flash(P61.get_center()),
                  Flash(P62.get_center()),
                  run_time=1)

        # 2.2
        # Passage from affine to projective
        self.next_section("2.2 Passage to projective equation")
        self.clear()
        self.add(bgr, e1, stte)
        ee1 = MathTex(r"y^2 = x^3", r"- 4\,", r" x ", r"+ 1")
        self.play(Transform(e1, ee1), run_time=.4)

        xyQ.to_corner(UL)
        xyQ.shift(0.2*RIGHT)
        self.play(FadeIn(xyQ))
        self.play(Indicate(xyQ), run_time=1)
        quotsub = MathTex(r"x=\frac{X}{Z}\ \ y = \frac{Y}{Z}")
        quotsub.next_to(xyQ, DOWN)
        quotsub.to_edge(LEFT)
        quotsub.shift(.2*RIGHT)
        XYZ = MathTex(r"X,Y,Z\in\mathbb{Z}")
        XYZ.next_to(quotsub, DOWN)
        XYZ.to_edge(LEFT)
        XYZ.shift(.2*RIGHT)
        self.play(FadeIn(XYZ), FadeIn(quotsub), run_time=1)
        self.play(Indicate(quotsub), FadeIn(XYZ), run_time=1)

        self.play(e1.animate(run_time=1).move_to(UP))
        ee2 = MathTex(r"\Bigl(\frac{Y}{Z}\Bigr)^2 = \Bigl(\frac{X}{Z}\Bigr)^3",
                      r"- 4\,", r" \Bigl(\frac{X}{Z}\Bigr)", "+ 1")
        ee2.next_to(e1, 2*DOWN)
        self.play(FadeIn(ee2))

        multby = MathTex(r"\bigl\vert \cdot Z^3")
        multby.next_to(ee2, RIGHT, buff=1)
        self.play(FadeIn(multby))
        self.play(Indicate(multby), run_time=1)

        ee3 = MathTex(r"Y^2 Z = X^3", r"- 4\,", r" XZ^2 ", r"+ Z^3")
        ee3.next_to(ee2, 2*DOWN)
        self.play(FadeIn(ee3))
        self.wait(1)

        self.play(FadeOut(ee2),
                  FadeOut(multby),
                  ee3.animate().next_to(e1, 2*DOWN),
                  run_time=2)
        self.wait()
        self.remove(ee2, multby)

        scalethrough = MathTex(r"(X,Y,Z)\sim (-X, -Y, -Z)")
        asinfraction = MathTex(r"x=\frac{X}{Z}=\frac{-X}{-Z}")
        astext = Text(":")
        scaling_text = VGroup(scalethrough,  astext, asinfraction)
        scaling_text.arrange(RIGHT, buff=.3)
        scaling_text.next_to(ee3, 1.5*DOWN)
        self.play(FadeIn(scaling_text))
        # self.add(index_labels(scalethrough[0])) # shows parts

        two = MathTex(r"2")
        two_top = two.copy().move_to(asinfraction[0][6].get_center())
        two_bottom = two.copy().move_to(asinfraction[0][9].get_center())
        two_x = two.copy().move_to(scalethrough[0][9].get_center())
        two_y = two.copy().move_to(scalethrough[0][12].get_center())
        two_z = two.copy().move_to(scalethrough[0][15].get_center())
        v = VGroup(two_top, two_bottom, two_x, two_y, two_z)
        v.shift(.045*UP)
        self.wait()
        self.play(Transform(scalethrough[0][9], two_x),
                  Transform(scalethrough[0][12], two_y),
                  Transform(scalethrough[0][15], two_z),
                  Transform(asinfraction[0][6], two_top),
                  Transform(asinfraction[0][9], two_bottom),
                  run_time=1
                  )
        self.wait()

        oo_x = MathTex(r"X=0,")
        oo_y = MathTex(r"Y=1,")
        oo_z = MathTex(r"Z=0")
        point_at_oo = VGroup(oo_x, oo_y, oo_z)
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
        self.add(bgr)
        newgrid = fake_numberplane()
        shz(newgrid, 1)
        self.add(newgrid, stte)
        self.add(fake_curve())

        for P in [P01, P02, P11, P12, P21, P22, P31, P32, P41, P42, P51, P52, P61, P62]:
            xP = P.get_center()[0]
            yP = P.get_center()[1]
            P.move_to(vec(96*xP/(96+yP), 100*yP/(96+yP)))
            self.add(P)
        self.add(Dot3D(vec(0, 100), radius=.3, color=YELLOW))

        self.move_camera(phi=PI/2,
                         frame_center=(0, -10, 5),
                         run_time=1)  # will be slower later
        self.wait(3)



# now render it
if __name__ == "__main__":
    with tempconfig({"renderer": "cairo", "quality": "medium_quality", "preview": True}):
        scene = SecondScene()
        scene.render()
