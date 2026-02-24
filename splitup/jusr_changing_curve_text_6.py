r"""
split scene
6
without text, cut the start
"""

from manim import *
import sage.all as sagemath
from tools import vec, CurvyPointyTip, shz, fading_numberplane
from msage import smanim
import json

def load_list(fi):
    r"""
    read json file fi into as a list
    """
    with open(fi, "r") as f:
        li = json.load(f)
    return li


def limit_expression():
    r"""
    Constructs the main limit expression
    $\lim_{T\to\infty} \frac{T!\cdot \mathcal{N}(T)^2}{\mathcal{M}(T!)}$
    as a group of objects

    [0] is lim_T->oo
    [1][0][0] is T!
    [1][0][1] is cdot
    [1][0][2] is N(T)^2
    [1][1] is the fraction line
    [1][2] is M(T!)
    """
    # Tex(r"$\lim_{T\to\infty} \frac{T!\cdot \mathcal{N}(T)^2}{\mathcal{M}(T!)}$")
    v = VGroup()
    limit = MathTex(r"\displaystyle\lim_{T\to\infty}")
    numerator = VGroup()
    t_factorial = MathTex(r"T!")
    cdot = MathTex(r"\cdot")
    nt_sq = MathTex(r"\mathcal{N}(T)", "{}^{2}")
    numerator.add(t_factorial, cdot, nt_sq)
    numerator.arrange(RIGHT, buff=0.1)
    denominator = MathTex(r"\mathcal{M}(T!)")
    fraction = VGroup()
    denominator_line = Line(np.array([-1, 0, 0]), np.array([1, 0, 0]))
    fraction.add(numerator, denominator_line, denominator)
    fraction.arrange(DOWN, buff=0.2)
    v.add(limit, fraction)
    v.arrange(RIGHT, buff=.1)
    return v


def mu():
    r"""
    Writes M(U) = # solutions modulo U
    """
    m_and_opening_parenthesis = Tex(r"$\mathcal{M}($")
    just_u = Tex("$U$")
    closing_parenthesis = Tex(r"$)$")
    equality_and_hash = Tex(r"$= \# $")
    eq_m_of_u_equal_hash = VGroup(m_and_opening_parenthesis,
                                  just_u,
                                  closing_parenthesis,
                                  equality_and_hash)
    eq_m_of_u_equal_hash.arrange(RIGHT, buff=0.1)
    solutions = Text("solutions").scale(0.8)
    modulo = Text("modulo ").scale(.8)
    u_again = Tex(r"$U$")
    modulo_u = VGroup(modulo, u_again)
    modulo_u.arrange(RIGHT, buff=.2)
    modulo_u[1].shift(0.05 * DOWN)
    solutions_modulo_u = VGroup(solutions, modulo_u)
    solutions_modulo_u.arrange(DOWN, buff=0.1, aligned_edge=LEFT)
    v = VGroup(eq_m_of_u_equal_hash, solutions_modulo_u)
    v.arrange(RIGHT, buff=0.2)
    return v


def shorter_family_of_curves(tt):
    r"""
    Family of elliptic curves, like in scene 1,
    but this stops at the singular curve in the middle
    """
    # avoid the singular curve
    if tt == 1:
        ttt = sagemath.RR(0.999)
    else:
        ttt = sagemath.RR(tt)

    E = sagemath.EllipticCurve([ttt-4, ttt+1])
    v = smanim(E.plot(color=rgb_to_color([255, 255*(1-tt/2), 0]),
                      thickness=2,
                      alpha=0.3,
                      xmax=7,
                      ymin=-5,
                      ymax=5))
    shz(v, 5)
    return v

# ---------------------------------

class JustChangingEquation6(Scene):

    def construct(self):

        self.wait(2)

        t = ValueTracker(0)

        # equation with changing coefficients with 2 digits
        eq_changing_curve = always_redraw(
            lambda: MathTex(
                f"y^2 = x^3 - {4-t.get_value():.2f}x + {t.get_value()+1:.2f}",
                color=YELLOW
            ).to_corner(UL)
        )

        shz(eq_changing_curve, 5)
        #standard_curve.add_updater(lambda m: m.become(shorter_family_of_curves(t.get_value())))
        self.add(#standard_curve,
                 eq_changing_curve)

        self.play(t.animate.set_value(1), run_time=2, rate_func=rate_functions.ease_in_out_sine)
        self.remove_updater(eq_changing_curve)
        #eq_singular_curve = MathTex(r"y^2 = x^3 - 3\,x + 2 ", color=YELLOW)
        # eq_singular_curve.to_corner(UL)
        # self.play(FadeOut(eq_changing_curve), FadeIn(eq_singular_curve))
        self.wait(2)
        # eq_general_curve = MathTex(r"y^2 = x^3 + A x + B ", color=YELLOW)
        # eq_general_curve.to_corner(UL)
        # eq_delta = MathTex(r"4\,A^3+27\,B^2=0")
        # eq_delta.next_to(eq_changing_curve, DOWN, aligned_edge=LEFT)
        #self.play(Transform(eq_singular_curve, eq_general_curve),
        #          FadeIn(eq_delta),
        #          run_time=.3)
        # self.wait(3)
        #
        # # then show that the graph drops quickly for the singular curve.
        # self.clear()
        # axes_for_log_plot = Axes(
        #                 x_range=[0, 1000, 200],
        #                 y_range=[0, 2, 1],
        #                 x_length=10,
        #                 y_length=5,
        #                 x_axis_config={"include_numbers": True, 'tip_shape': CurvyPointyTip},
        #                 y_axis_config={"include_numbers": True, 'tip_shape': CurvyPointyTip}
        #                 )
        # shift_the_full_graph = vec(1, 1)
        # axes_for_log_plot.shift(shift_the_full_graph)
        # self.add(axes_for_log_plot)
        # self.wait(.2)
        #
        # # first draw the usual curve
        # li = load_list(f"../data/singular_plot_points.json")
        # log_graph = VMobject(color=YELLOW)
        # log_graph.set_points_as_corners([axes_for_log_plot.c2p(x, y) for x, y in li if x > 10])
        # log_graph.set_style(stroke_width=2)
        #
        # # eq_changing_curve = MathTex(r"y^2 = x^3 - 3\,x + 2 ")
        # eq_changing_curve.to_edge(DOWN)
        # self.play(FadeIn(log_graph),
        #           #FadeIn(eq_changing_curve)
        #           )
        # self.wait(2)
        #
        # self.clear()
        # axes_for_log_plot = Axes(
        #                 x_range=[0, 1000, 200],
        #                 y_range=[0, 10, 2],
        #                 x_length=10,
        #                 y_length=5,
        #                 x_axis_config={"include_numbers": True, 'tip_shape': CurvyPointyTip},
        #                 y_axis_config={"include_numbers": False, 'tip_shape': CurvyPointyTip}
        #                 )
        # shift_the_full_graph = vec(1, 1)
        # label = MathTex("1").scale(.7)
        # label.next_to(axes_for_log_plot.c2p(0, 8), LEFT)
        # axes_for_log_plot.add(label)
        # for i in range(1, 5):
        #     s = str(10*i-50)
        #     label = MathTex(r"10^{" + s + "}").scale(0.7)
        #     label.next_to(axes_for_log_plot.c2p(0, 2*i-2), LEFT)
        #     axes_for_log_plot.add(label)
        # axes_for_log_plot.shift(shift_the_full_graph)
        # self.add(axes_for_log_plot)
        # self.wait(.2)
        #
        # # first draw the usual curve
        # li = load_list(f"../data/singular_plot_points.json")
        # log_graph = VMobject(color=YELLOW)
        # log_graph.set_points_as_corners([axes_for_log_plot.c2p(x, np.log(y)/np.log(10)/5 + 8) for x, y in li if x > 10])
        # log_graph.set_style(stroke_width=2)
        #
        # #eq_changing_curve = MathTex(r"y^2 = x^3 - 3\,x + 2 ")
        # #eq_changing_curve.to_edge(DOWN)
        # self.play(FadeIn(log_graph),
        #           #FadeIn(eq_changing_curve)
        #           )
        # self.wait(2)

        # restate conjecture
        self.clear()

# now render it
if __name__ == "__main__":
    config.renderer = "cairo"
    config.format = "mp4"
    #config.transparent = True
    #config.write_to_movie = False
    config.preview = True

    # Optional but recommended
    config.background_color = BLACK

    scene = JustChangingEquation6()
    scene.render()
