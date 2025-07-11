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



def list_of_points(T, colour=WHITE):
    """
    Create a table of all points up to height T
    with T in [ 10, 30, 50, 100, 200, 1000, 5000]

    returns a vgroup plaed on the left hand side,
    a list of points in form (X,Y,Z) and
    a list of indices to find the points in the vgroup
    """
    # points ordered by naive height(0, 1,0)
    pts = [ (0, 1,0),
            (0, 1,1),
            (-1, 2,1),
            (-1, 2,1),
            (2, 1,1),
            (-2, 1,1),
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
            (1045, 4306,6859)
          ]

    pts_str = \
          [r"$(0$, & $1$, & $0)$",
           r"$(0$, & $\pm 1$, & $1)$",
           r"$(-1$, & $\pm 2$, & $1)$",
           r"$(-1$, & $\pm 2$, & $1)$",
           r"$(2$, & $\pm 1$, & $1)$",
           r"$(-2$, & $\pm 1$, & $1)$",
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
           r"$(1045$, & $\pm 4306$, & $6859)$"
           ]
    # lei[T] gives the number of items in
    # pts with height < T
    lei = {10: 9, 30: 10, 50: 13, 100: 15, 200: 18, 1000: 22, 5000: 29}

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
    # the top point is v[0][9:15] etc
    indices = [9,16,24,33,42,50,59,67,75,83,94,104,115,125,137,147]
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
        # xline = Line(vec(-7, 0, .1), vec(7, 0, .1), color=WHITE, stroke_width=2)
        # grid.add(xline)
        shz(grid, 1)
        # axex = Arrow(start=vec(0,0),
        #              end=vec(6.5,0),
        #              buff=0,
        #              stroke_width=2,
        #              tip_length=0.2,
        #              tip_shape=BetterCurvyPointyTip,
        #              color=WHITE)
        # axey = Arrow(start=vec(0, 0),
        #              end=vec(0, 3.7),
        #              buff=0,
        #              stroke_width=2,
        #              tip_length=0.2,
        #              tip_shape=BetterCurvyPointyTip,
        #              color=WHITE)
        # axes = VGroup(axex, axey)
        # shz(axes,1)
        E = sagemath.EllipticCurve([-4, 1])
        curve = smanim(E.plot(color="yellow", thickness=2, alpha=0.3, xmax=7, ymin=-5, ymax=5))
        shz(curve, 5)
        curvepic = VGroup(grid, curve)
        shift_grid = vec(2,0)
        curvepic.shift(shift_grid)
        self.add(curvepic, stte)

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
            Dot3D(vec(3.5, 3.6) + shift_grid, color=pointcolour, radius=pointradius, z_index=10),
            Dot3D(vec(3.5, -3.6) + shift_grid, color=pointcolour, radius=pointradius, z_index=10),
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
                self.add(Dot3D(P_centre, color=pointcolour, radius=pointradius, z_index=10),
                         Dot3D(minus_P_centre, color=pointcolour, radius=pointradius, z_index=10))
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

        v1, more_pts, indices = list_of_points(100)
        v1.shift(DOWN)
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
                self.add(Dot3D(P_centre, color=pointcolour, radius=pointradius, z_index=10),
                         Dot3D(minus_P_centre, color=pointcolour, radius=pointradius, z_index=10))
                point_to_flash = P_centre
                minus_point_to_flash = minus_P_centre

            self.play(Indicate(P_str),
                      Flash(point_to_flash),
                      Flash(minus_point_to_flash),
                      runtime=.7)
            self.wait(.1)
            if point_outside_shows:
                self.remove(point_outside)

            self.wait(2)



#  now render it
if __name__ == "__main__":
    with tempconfig({"renderer": "cairo", "quality": "medium_quality", "preview": True}):
        scene = ThirdScene()
        scene.render()
