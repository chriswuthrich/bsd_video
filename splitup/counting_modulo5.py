r"""
split scene
5

"""

from manim import *
import sage.all as sagemath
from tools import vec, CurvyPointyTip
from msage import smanim


class CountingModulo5(Scene):

    def construct(self):

        # 3.2 Counting modulo
        #
        self.next_section("3.2 Counting points modulo")

        # Title comes in
        #title_counting_rational_points = Text("Counting points modulo", color=YELLOW)
        #title_counting_rational_points.shift(2 * UP)
        #self.play(GrowFromCenter(title_counting_rational_points))
        #self.wait(.5)

        # equation in centre goes modulo
        eq_projective_standard_curve = MathTex(r"{{y^2}} {{=}} {{x^3- 4\,x + 1}}", color=YELLOW)
        self.add(eq_projective_standard_curve)
        eemod = MathTex(r"{{y^2}} {{\equiv}} {{x^3- 4\,x +1}} \pmod{10}", color=YELLOW)
        self.play(TransformMatchingTex(eq_projective_standard_curve, eemod),
                  #FadeOut(title_counting_rational_points, shift=UP, scale=1.5)
                  run_time=1)
        self.wait(1)
        self.play(eemod.animate.move_to(vec(1.4, -3.219)), run_time=1)
        self.wait(5)

        # points from basic_calculation_with_favourite_elliptic_curve.ipynb
        pts_mod_ten = [(0, 1, 1), (2, 1, 1), (8, 1, 1), (9, 2, 1), (4, 3, 1),
                       (3, 4, 1), (5, 4, 1), (7, 4, 1), (3, 6, 1), (5, 6, 1),
                       (7, 6, 1), (4, 7, 1), (9, 8, 1), (0, 9, 1), (2, 9, 1),
                       (8, 9, 1), (8, 1, 2), (0, 3, 2), (4, 3, 2), (6, 3, 2),
                       (0, 7, 2), (4, 7, 2), (6, 7, 2), (8, 9, 2), (0, 1, 5),
                       (5, 2, 5), (0, 1, 0)]

        affine_pts_mod_ten = [(x, y) for (x, y, z) in pts_mod_ten if z == 1]
        pts_v = {(x, y, z): VGroup(MathTex(r"(" + str(x) + r"," + str(y) + r")").scale(.8),
                                   MathTex(r"(" + str(x) + r"," + str(y) + r"," + str(z) + ")").scale(.8))
                 for (x, y, z) in pts_mod_ten}

        for (x, y) in affine_pts_mod_ten:
            pts_v[(x, y, 1)].move_to(vec(.95 * x - 2.6, .4 * y - 2.2))
            self.play(FadeIn(pts_v[(x, y, 1)][0]), run_time=.2)
        self.wait(10)

        emod = MathTex(r"Y^2 Z \equiv X^3- 4\,XZ^2 + Z^3}} \pmod{10}", color=YELLOW)
        emod.move_to(eemod.get_center())
        equivmod = MathTex(r"(X,Y,Z)\sim \\ ({{3}}X, {{3}}Y, {{3}}Z)", color=YELLOW)
        equivmod.move_to(vec(-5, 0))

        self.play(FadeOut(eemod),
                  FadeIn(emod),
                  run_time=2)
        self.wait(1)
        self.add(equivmod)
        self.wait(1)
        for (x, y) in affine_pts_mod_ten:
            self.play(FadeTransform(pts_v[(x, y, 1)][0], pts_v[(x, y, 1)][1]), run_time=0.2)
        i = 0

        # give points at infinity on two lines at the top
        separation_between_points = 2.
        for (x, y, z) in pts_mod_ten:
            if z != 1:
                if i < 6:
                    pts_v[(x, y, z)].move_to(vec(separation_between_points * (i - 2.5), 3.3))
                    self.add(pts_v[(x, y, z)][1])
                else:
                    pts_v[(x, y, z)].move_to(vec(separation_between_points * (i - 8), 2.7))
                    self.add(pts_v[(x, y, z)][1])
                i += 1
                self.wait(.1)
        self.wait(7)

        # graph the number of points modulo Q
        self.clear()
        mu = MathTex(r"\mathcal{M}(U) = \# E\bigl({}^{\mathbb{Z}}\!/\!{}_{U \mathbb{Z}}\bigr)")
        mu_text = MathTex(r"= \text{ number of solutions modulo }U.")
        mu_group = VGroup(mu, mu_text).arrange(RIGHT)
        mu_group.to_edge(UP)
        self.play(FadeIn(mu_group))
        self.wait(10)

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
        self.play(Create(bc), run_time=2)
        self.wait(2)

# now render it
if __name__ == "__main__":
    config.renderer = "cairo"
    config.format = "mp4"
    #config.transparent = True
    #config.write_to_movie = False
    config.preview = True

    # Optional but recommended
    config.background_color = BLACK

    scene = CountingModulo5()
    scene.render()
