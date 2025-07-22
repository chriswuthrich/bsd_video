r"""
Part of the bsd_video

Here the actual conjecture is
explained and illustrated
with graphs.

"""

from manim import *
import sage.all as sagemath
from character import two_characters_standing_next_to_each_other
from msage import smanim
from tools import *
import json



def list_of_points(T, colour=WHITE):
    """
    Create a table of all points up to height T
    with T in [ 10, 100, 1000, 10000]

    returns a vgroup placed on the left hand side,
    a list of points in form (X,Y,Z) and
    a list of indices to find the points in the vgroup
    """
    # this list comes from
    # basic_calculation_with_favourite_elliptic_curve.ipynb
    # points ordered by naive height(0, 1,0)
    pts = [(0, 1, 0),
           (0, 1, 1),
           (-2, 1, 1),
           (-1, 2, 1),
           (2, 1, 1),
           (3, 4, 1),
           (4, 7, 1),
           (2, 1, 8),
           (-14, 13, 8),
           (10, 31, 1),
           (-6, 37, 27),
           (12, 41, 1),
           (-24, 53, 27),
           (20, 89, 1),
           (30, 29, 125),
           (132, 79, 64),
           (-80, 227, 125),
           (-630, 503, 343),
           (644, 113, 343),
           (455, 736, 125),
           (1160, 967, 512),
           (114, 1217, 1),
           (1386, 377, 729),
           (-130, 2443, 2197),
           (-1683, 2674, 1331),
           (-2728, 1021, 1331),
           (705, 3592, 27),
           (1045, 4306, 6859),
           (-16744, 24023, 12167),
           (1274, 45473, 1)
           ]

    # copied but O modified
    pts_strings = \
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
    # number_of_points_below_powers_of_ten[T] gives the number of items in
    # pts with height < T
    number_of_points_below_powers_of_ten = {10: 8, 100: 14, 1000: 20, 10000: 28}

    n = number_of_points_below_powers_of_ten[T]
    tabular_string = r"\begin{tabular}{rcl}" + "\n"
    tabular_string += r"\toprule" + "\n"
    tabular_string += r"$(X$, & $Y$, & $Z)$ " + r"\\" + "\n"
    tabular_string += r"\midrule" + "\n"
    for P in pts_strings[:n]:
        tabular_string += P + r" \\ " + "\n"
    tabular_string += r"\bottomrule" + "\n"
    tabular_string += r"\end{tabular}"
    v = Tex(tabular_string, color=colour)
    v.scale(.5)
    v.move_to(vec(-5, 2))
    v.to_edge(UP)
    # the top point is v[0][10:15] etc
    # use self.add(index_labels(v1[0])) to determine these
    indices = [9, 16, 24, 33, 42, 50, 58,
               66, 74, 85, 95, 106, 116,
               128, 138, 150, 162, 176,
               191, 205, 219]
    return v, pts[:n], indices


class ThirdScene(Scene):

    def construct(self):

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
        standard_curve = smanim(standard_E.plot(color="yellow", thickness=2, alpha=0.3, xmax=7, ymin=-5, ymax=5))
        shz(standard_curve, 5)
        curvepic = VGroup(grid, standard_curve)
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

        equivmod.move_to(vec(-5,0))

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
        mu_group= VGroup(mu, mu_text).arrange(RIGHT)
        mu_group.to_edge(UP)
        self.play(FadeIn(mu_group))
        self.wait(1)

        mu_graph = [[2, 3], [3, 7], [4, 8], [5, 9], [6, 21], [7, 12], [8, 24],
                    [9, 21], [10, 27], [11, 15], [12, 56], [13, 18], [14, 36],
                    [15, 63], [16, 48], [17, 25], [18, 63], [19, 25], [20, 72],
                    [21, 84], [22, 45], [23, 30], [24, 168], [25, 45], [26, 54],
                    [27, 63], [28, 96], [29, 22], [30, 189]]

        mu_val = [m[1] for m in mu_graph]
        mu_labels = [ str(m[0]) if m[0]%5==0 else "" for m in mu_graph]
        bc = BarChart(mu_val,
                      bar_names = mu_labels,
                      y_range=[0, 200, 50],
                      y_length=5,
                      tips=True,
                      x_axis_config={"tip_shape": CurvyPointyTip, "tip_height": 0.2},
                      y_axis_config={"tip_shape": CurvyPointyTip}
                      )
        bc.scale(.8)
        bc.shift(vec(1, 0))
        u_label = MathTex(r"U")
        u_label.move_to(vec(6.4,-2.3))
        self.add(u_label)
        self.play(Create(bc))
        self.wait()
#

#  now render it
if __name__ == "__main__":
    with tempconfig({"renderer": "cairo", "quality": "medium_quality", "preview": True}):
        scene = ThirdScene()
        scene.render()
