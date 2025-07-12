r"""
Part of the bsd_video

Here the actual conjecture is
explained and illustrated
with graphs.

TODO

"""

from manim import *
import sage.all as sagemath
from character import StudentChar
from msage import smanim
from tools import *
import json

def my_point(centre=ORIGIN, colour=YELLOW, radius=0.1, z_index=10):
    """
    replacement for Dot3D(minus_P_centre, color=pointcolour, radius=pointradius, z_index=10))
    """
    v1 = Circle(radius, stroke_width=0, fill_color=colour, fill_opacity=1, stroke_color=colour, z_index=z_index)
    v2 = Circle(radius/3, stroke_width=0, fill_color=BLACK, fill_opacity=1, stroke_color=BLACK, z_index=z_index+.1)
    v = VGroup(v1, v2)
    v.move_to(centre)
    return v


def list_of_points(T, colour=WHITE):
    """
    Create a table of all points up to height T
    with T in [ 10, 100, 1000, 10000]

    returns a vgroup plaed on the left hand side,
    a list of points in form (X,Y,Z) and
    a list of indices to find the points in the vgroup
    """
    # points ordered by naive height(0, 1,0)
    pts = [ (0, 1,0),
            (0, 1,1),
            (-2, 1,1),
            (-1, 2,1),
            (2, 1,1),
            (3, 4,1),
            (4, 7,1),
            (2, 1,8),
            (-14, 13,8),
            (10, 31,1),
            (-6, 37,27),
            (12, 41,1),
            (-24, 53,27),
            (20, 89,1),
            (30, 29,125),
            (132, 79,64),
            (-80, 227,125),
            (-630, 503,343),
            (644, 113,343),
            (455, 736,125),
            (1160, 967,512),
            (114, 1217,1),
            (1386, 377,729),
            (-130, 2443,2197),
            (-1683, 2674,1331),
            (-2728, 1021,1331),
            (705, 3592,27),
            (1045, 4306,6859),
            (-16744, 24023,12167),
            (1274, 45473,1)
           ]

    # copied but O modified
    pts_str = \
           [r"$(0$, & $1$, & $0)$",
            r"$(0$, & $\pm 1$, & $1)$",
            r"$(-2$, & $\pm 1$, & $1)$",
            r"$(-1$, & $\pm 2$, & $1)$",
            r"$(2$, & $\pm 1$, & $1)$",
            r"$(3$, & $\pm 4$, & $1)$",
            r"$(4$, & $\pm 7$, & $1)$",
            r"$(2$, & $\pm 1$, & $8)$",
            r"$(-14$, & $\pm 13$, & $8)$",
            r"$(10$, & $\pm 31$, & $1)$",
            r"$(-6$, & $\pm 37$, & $27)$",
            r"$(12$, & $\pm 41$, & $1)$",
            r"$(-24$, & $\pm 53$, & $27)$",
            r"$(20$, & $\pm 89$, & $1)$",
            r"$(30$, & $\pm 29$, & $125)$",
            r"$(132$, & $\pm 79$, & $64)$",
            r"$(-80$, & $\pm 227$, & $125)$",
            r"$(-630$, & $\pm 503$, & $343)$",
            r"$(644$, & $\pm 113$, & $343)$",
            r"$(455$, & $\pm 736$, & $125)$",
            r"$(1160$, & $\pm 967$, & $512)$",
            r"$(114$, & $\pm 1217$, & $1)$",
            r"$(1386$, & $\pm 377$, & $729)$",
            r"$(-130$, & $\pm 2443$, & $2197)$",
            r"$(-1683$, & $\pm 2674$, & $1331)$",
            r"$(-2728$, & $\pm 1021$, & $1331)$",
            r"$(705$, & $\pm 3592$, & $27)$",
            r"$(1045$, & $\pm 4306$, & $6859)$",
            r"$(-16744$, & $\pm 24023$, & $12167)$",
            r"$(1274$, & $\pm 45473$, & $1)$"
           ]
    # lei[T] gives the number of items in
    # pts with height < T
    lei = {10: 8, 100: 14, 1000: 20, 10000: 28}

    template = TexTemplate()
    template.add_to_preamble(r"\usepackage{booktabs}")

    n = lei[T]
    tstr = r"\begin{tabular}{rcl}" + "\n"
    tstr += r"\toprule" + "\n"
    tstr += r"$(X$, & $Y$, & $Z)$ " + r"\\" + "\n"
    tstr += r"\midrule" + "\n"
    for P in pts_str[:n]:
        tstr += P + r" \\ " + "\n"
    # tstr += pts[n-1]
    tstr += r"\bottomrule" + "\n"
    tstr += r"\end{tabular}"
    v = Tex(tstr, tex_template=template, color=colour)
    v.scale(.5)
    v.move_to(vec(-5, 2))
    v.to_edge(UP)
    # the top point is v[0][10:15] etc
    # use self.add(index_labels(v1[0])) to determine these
    indices = [9,16,24,33,42,50,58,66,74,85,95,106,116,128,138,150,162,176,191,205,219]
    return v, pts[:n], indices


class ThirdScene(Scene):

    def construct(self):

        # 3.1 Count global points
        self.add(my_background())
        st = StudentChar()
        te = StudentChar(height=1.2, width=0.8, colour=GREEN, lid_colour=DARK_GRAY)
        st.scale(1)
        te.scale(1)
        stte = VGroup(st, te)
        stte.arrange()
        stte.to_corner(DL)
        shz(stte, 10)
        self.add(stte)

        # Title comes in
        tit = Text("Counting rational points", color=YELLOW)
        tit.shift(2*UP)
        self.play(GrowFromCenter(tit))
        self.wait(.5)
        ee = MathTex(r"Y^2 Z = X^3- 4\,XZ^2+ Z^3")
        ee.move_to(vec(3.6, -3.2))
        shz(ee, 5)
        self.add(ee)
        self.play(FadeOut(tit, shift=DOWN * 2, scale=1.5))
        self.wait(1)

        # recreate curve
        grid = VGroup()
        grid.add(my_fading_numberplane())
        grid.add(Line(vec(0, -4), vec(0, 4), color=WHITE, stroke_width=2))
        shz(grid, 1)
        E = sagemath.EllipticCurve([-4, 1])
        curve = smanim(E.plot(color="yellow", thickness=2, alpha=0.3, xmax=7, ymin=-5, ymax=5))
        shz(curve, 5)
        curvepic = VGroup(grid, curve)
        shift_grid = vec(2,0)
        curvepic.shift(shift_grid)
        self.add(curvepic, stte)

        # list points of height < 10
        v1, pts, indices = list_of_points(10)
        bdt = MathTex(r"\lvert X\rvert,\, \lvert Y \rvert,\, \lvert Z\rvert < 10")
        bdt.to_edge(UP)
        bdt.shift(vec(-.7, 0))
        self.play(FadeIn(v1),
                  FadeIn(bdt),
                  run_time=1)
        self.wait(1)
        pointcolour = BLUE_B
        pointradius = .07
        point_outside = VGroup(
            my_point(vec(3.5, 3.6) + shift_grid, radius=pointradius, colour=pointcolour),
            my_point(vec(3.5, -3.6) + shift_grid, radius=pointradius, colour=pointcolour),
            Arrow(vec(3.7, 3.6) + shift_grid, vec(3.8,3.9) + shift_grid),
            Arrow(vec(3.7, -3.6) + shift_grid, vec(3.8,-3.9) + shift_grid),
            )
        point_outside_shows = False
        for i in range(1, len(pts)):
            P = pts[i]
            P_str = v1[0][indices[i]:indices[i+1]]
            P_centre = vec(P[0]*1./P[2], P[1]*1./P[2]) + shift_grid
            minus_P_centre = vec(P[0]*1./P[2], - P[1]*1./P[2]) + shift_grid
            if P_centre[0] > 7.111 or P_centre[1] > 4:  # point outside screen
                self.add(point_outside)
                point_outside_shows = True
                point_to_flash = vec(3.5, 3.6) + shift_grid
                minus_point_to_flash = vec(3.5, 3.6) + shift_grid
            else:
                self.add(my_point(P_centre, colour=pointcolour, radius=pointradius),
                      my_point(minus_P_centre, radius=pointradius, colour=pointcolour))
                point_to_flash = P_centre
                minus_point_to_flash = minus_P_centre

            self.play(Indicate(P_str),
                      Flash(point_to_flash),
                      Flash(minus_point_to_flash),
                      runtime=.7)
            self.wait(.1)
            # P_str.set_color(WHITE)
            if point_outside_shows:
                self.remove(point_outside)

        self.play(FadeOut(v1, bdt))

        # now list them of height < 100
        v1, more_pts, indices = list_of_points(100)
        bdt = MathTex(r"\lvert X\rvert,\, \lvert Y \rvert,\, \lvert Z\rvert < 100")
        bdt.to_edge(UP)
        bdt.shift(vec(-.7, 0))
        self.play(FadeIn(v1),
                  FadeIn(bdt),
                  run_time=1)
        self.wait()
        for i in range(len(pts), len(more_pts)):
            P = more_pts[i]
            P_str = v1[0][indices[i]:indices[i+1]]
            P_centre = vec(P[0]*1./P[2], P[1]*1./P[2]) + shift_grid
            minus_P_centre = vec(P[0]*1./P[2], - P[1]*1./P[2]) + shift_grid
            if P_centre[0] > 7.111 or P_centre[1] > 4:  # point outside screen
                self.add(point_outside)
                point_outside_shows = True
                point_to_flash = vec(3.5, 3.6) + shift_grid
                minus_point_to_flash = vec(3.5, 3.6) + shift_grid
            else:
                self.add(my_point(P_centre, colour=pointcolour, radius=pointradius, z_index=10),
                         my_point(minus_P_centre, colour=pointcolour, radius=pointradius, z_index=10))
                point_to_flash = P_centre
                minus_point_to_flash = minus_P_centre

            self.play(Indicate(P_str),
                      Flash(point_to_flash),
                      Flash(minus_point_to_flash),
                      runtime=.7)
            self.wait(.1)
            if point_outside_shows:
                self.remove(point_outside)
        self.play(FadeOut(v1, bdt))

        # list up to height 1000
        v1, even_more_pts, indices = list_of_points(1000)
        bdt = MathTex(r"\lvert X\rvert,\, \lvert Y \rvert,\, \lvert Z\rvert < 1000")
        bdt.to_edge(UP)
        bdt.shift(vec(-.7, 0))

        # move up the list to reveal more points
        # opacity updater for new elements
        def op(i, tt):
            s = i - len(more_pts)
            n = len(even_more_pts) - len(more_pts)
            if tt<s/n:
                return 0
            elif tt<(s+1)/n:
                return n*tt-s
            else:
                return 1

        t = ValueTracker(0)
        start_v1 = vec(v1.get_center()[0], v1.get_center()[1])
        def place_v1(tt):
            return start_v1 + tt * vec(0,3)
        v1.add_updater(lambda m: m.move_to(place_v1(t.get_value())))
        for i in range(len(more_pts), len(even_more_pts)):
            for j in range(indices[i], indices[i+1]):
                # in the following the "i=i" is there to avoid late binding
                # otherwise all updaters will take the last value of i
                v1[0][j].add_updater(lambda m, i=i: m.set_opacity( op(i, t.get_value())))
        v1[0][-1].add_updater(lambda m, i=i: m.set_opacity( op(i, t.get_value())))
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
        self.add(v1)
        self.play(FadeIn(bdt),
                  t.animate.set_value(1), run_time=3, rate_func=linear)

        self.wait(1)



#  now render it
if __name__ == "__main__":
    with tempconfig({"renderer": "cairo", "quality": "medium_quality", "preview": True}):
        scene = ThirdScene()
        scene.render()
