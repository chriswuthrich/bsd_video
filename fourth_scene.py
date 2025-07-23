r"""
Part of the bsd_video

Here we illustrate the conjectures with moving graphs

The points forming the graphs are precalculated in
create_data_for_plots_of_conjectured_limit.ipynb

"""

from manim import *
import sage.all as sagemath
from character import two_characters_standing_next_to_each_other
from msage import smanim
from tools import *
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

#

class FourthScene(Scene):

    def construct(self):

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
        eq_m_t_factorial_source = VGroup(mu_hash_solutions_modulo_u[0][0], eq_t_factorial_again, mu_hash_solutions_modulo_u[0][2]).copy()
        path_mt = ArcBetweenPoints(eq_m_t_factorial_source.get_center(), eq_m_t_factorial_in_limit.get_center(), angle=- PI / 5)

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
        self.play( FadeOut(mu_hash_solutions_modulo_u, eq_u_t_factorial, nt_hash_bounded_rational_solutions))
        self.play(complete_limit_formula.animate.move_to(vec(2,1)), run_time=1)
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
        height_jump_point_1.scale(.5).move_to(axes_for_log_plot.c2p(np.log10(137593), 0) + vec(.45,.25))
        height_jump_point_2 = MathTex(r"3\,241\,792", color=WHITE)
        height_jump_point_2.scale(.5).move_to(axes_for_log_plot.c2p(np.log10(3241792), 0) + vec(.55, .25))

        self.play(Succession(FadeIn(point_out_pt1),
                             FadeIn(dashed_line_down_1),
                             FadeIn(height_jump_point_1),
                             FadeIn(eq_jump_point_1)),
                  run_time=1 )
        self.wait(.5)
        self.play(Succession(FadeIn(point_out_pt2),
                             FadeIn(dashed_line_down_2),
                             FadeIn(height_jump_point_2),
                             FadeIn(eq_jump_point_2)),
                  run_time=2 )

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
        standard_curve = smanim(standard_E.plot(color="yellow", thickness=2, alpha=0.3, xmax=7, ymin=-5, ymax=5))

        t = ValueTracker(0)

        # equation with changing coefficients with 2 digits
        eq_changing_curve = always_redraw(
            lambda: MathTex(
                f"y^2 = x^3 - {4-t.get_value():.2f}x + {t.get_value()+1:.2f}",
                color=YELLOW
            ).to_corner(UL)
        )

        shz(eq_changing_curve, 5)
        standard_curve.add_updater(lambda m: m.become(shorter_family_of_curves(t.get_value())))
        self.add(standard_curve, eq_changing_curve)

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
        log_graph.set_points_as_corners([axes_for_log_plot.c2p(x, y) for x, y in li if x>10])
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
        log_graph.set_points_as_corners([axes_for_log_plot.c2p(x, np.log(y)/np.log(10)/5 + 8) for x, y in li if x>10])
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



#

#  now render it
if __name__ == "__main__":
    scene = FourthScene()
    scene.render()
