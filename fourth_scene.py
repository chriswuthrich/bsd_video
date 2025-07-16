r"""
Part of the bsd_video

Here we illustrate the conjectures with moving graphs

The points forming the graphs are precalculated in
create_data_for_plots_of_conjectured_limit.ipynb

"""

from manim import *
from manim.opengl import *
import sage.all as sagemath
from character import StudentChar
from msage import smanim
from first_scene import subtitle
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
    lim = MathTex(r"\displaystyle\lim_{T\to\infty}")
    num = VGroup()
    t_factorial = MathTex(r"T!")
    cdot = MathTex(r"\cdot")
    nt_sq = MathTex(r"\mathcal{N}(T)", "{}^{2}")
    num.add(t_factorial, cdot, nt_sq)
    num.arrange(RIGHT, buff=0.1)
    den = MathTex(r"\mathcal{M}(T!)")
    fraction = VGroup()
    li = Line(np.array([-1, 0, 0]), np.array([1, 0, 0]))
    fraction.add(num, li, den)
    fraction.arrange(DOWN, buff=0.2)
    v.add(lim, fraction)
    v.arrange(RIGHT, buff=.1)
    return v


def mu():
    r"""
    Writes M(U) = # solutions modulo U

    """
    te_mu1a = Tex(r"$\mathcal{M}($")
    te_mu1b = Tex("$U$")
    te_mu1c = Tex(r"$)$")
    te_mu1d = Tex(r"$= \# $")
    te_mu1 = VGroup(te_mu1a, te_mu1b, te_mu1c, te_mu1d)
    te_mu1.arrange(RIGHT, buff=0.1)
    te_mu2 = Text("solutions").scale(0.8)
    te_mu3 = Text("modulo ").scale(.8)
    te_mu4 = Tex(r"$U$")
    te_mua = VGroup(te_mu3, te_mu4)
    te_mua.arrange(RIGHT, buff=.2)
    te_mua[1].shift(0.05 * DOWN)
    te_mub = VGroup(te_mu2, te_mua)
    te_mub.arrange(DOWN, buff=0.1, aligned_edge=LEFT)
    te_mu = VGroup(te_mu1, te_mub)
    te_mu.arrange(RIGHT, buff=0.2)
    return te_mu

class FourthScene(Scene):

    def construct(self):

        # 4 The conjecture
        # 4.1 State the conjecture
        self.next_section("4.1 State the conjecture")
        # recreate background
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

        # define N(T)
        te_defnt = Tex(r"$\mathcal{N}(T) = " +
                       r"\# \Bigl\{ P\in E(\mathbb{Q}) \, " +
                       r": \, \lvert X\rvert, \lvert Y\rvert, " +
                       r"\lvert Z\rvert \leq T \Bigr\} $")
        self.add(te_defnt)
        # now add an animation counting points
        self.wait(2)

        te_defmu = Tex(r"$\mathcal{M}(U) = \# E\bigl({}^{\mathbb{Z}}\!/\!{}_{U\mathbb{Z}}\bigr)$")
        self.remove(te_defnt)
        self.add(te_defmu)
        # add an animation counting points modulo increasing T
        self.wait(2)

        self.remove(te_defmu)
        te_compare = Text("Compare")
        te_compare.shift(2*LEFT)

        rhs = VGroup()
        te_nt1 = Tex(r"$\mathcal{N}(T)$")
        te_nt2 = Tex(r"$ = \# $")
        te_nt3 = Text("bounded \n" + "rational \n" + "solutions").scale(.8)
        te_nt = VGroup(te_nt1, te_nt2, te_nt3)
        te_nt.arrange(RIGHT, buff=0.2)

        te_mu = mu()  # M(U) = # solutions modulo U

        te_ut = Tex(r"$U = T! = 1 \cdot 2 \cdots T$")
        rhs.add(te_nt, te_mu, te_ut)
        rhs.arrange(DOWN, buff=1.1, aligned_edge=LEFT)
        rhs.shift(3.5*RIGHT)
        self.add(rhs)

        # change U to T!
        new_te_mu4 = Tex(r"$T!$")
        te_mu4 = te_mu[1][1][1]
        new_te_mu4.shift(te_mu4.get_center())
        new_te_mu0 = Tex(r"$T!$")
        te_mu0 = te_mu[0][1]
        new_te_mu0.shift(te_mu0.get_center())
        self.play(Transform(te_mu4, new_te_mu4),
                  Transform(te_mu0, new_te_mu0),
                  run_time=1)
        self.wait(2)

        self.remove(te_compare)
        te_lim = limit_expression()
        te_lim.scale(2)
        te_lim.shift(3*LEFT)
        self.add(te_lim[1][1])  # ---
        self.wait(1)

        # move N(T)
        te_nt_target = te_lim[1][0][2][0]  # N(T)
        te_nt_source = te_nt1.copy()
        path_nt = ArcBetweenPoints(te_nt_source.get_center(), te_nt_target.get_center(), angle=PI/5)

        def updater_nt(mob, alpha):
            point = path_nt.point_from_proportion(alpha)
            scale = interpolate(1, te_nt_target.width/te_nt_source.width, alpha)
            mob.move_to(point)
            mob.set(width=te_nt_source.width * scale)

        self.play(UpdateFromAlphaFunc(te_nt_source, updater_nt), run_time=3)
        # te_lim[1][0][2][0] = te_nt_source
        self.wait(1)

        # add square and highlight it
        te_sq = te_lim[1][0][2][1]  # "^2"
        self.add(te_sq)
        self.play(Indicate(te_sq), run_time=1)
        self.add(te_lim[1][0][2])
        self.remove(te_nt_source)

        # move the M(T!) to the fraction
        te_mt1 = te_lim[1][2]  # M(T!) target
        te_mt2 = VGroup(te_mu[0][0], new_te_mu0, te_mu[0][2]).copy()
        path_mt = ArcBetweenPoints(te_mt2.get_center(), te_mt1.get_center(), angle=- PI / 5)

        def updater_mt(mob, alpha):
            point = path_mt.point_from_proportion(alpha)
            scale = interpolate(1, te_mt1.width/te_mt2.width, alpha)
            mob.move_to(point)
            mob.set(width=te_mt2.width * scale)

        self.play(UpdateFromAlphaFunc(te_mt2, updater_mt), run_time=3)
        te_lim[1][2] = te_mt2
        self.wait(1)

        self.add(te_lim[1][0])  # numerator
        self.wait(1)
        self.add(te_lim[0])   # lim
        self.wait(1)

        self.remove(te_mu, te_ut, te_nt)
        self.play(te_lim.animate.move_to(vec(2,1)), run_time=1)
        self.wait(1)

        te_con = Text("Conjecture", color=YELLOW)
        te_con.shift(2.5*UP+4*LEFT)
        self.add(te_con)
        te_conv1 = Text("converges to a")
        te_conv2 = Text("positive real number.")
        te_conv = VGroup(te_conv1, te_conv2)
        te_conv.arrange(DOWN, aligned_edge=LEFT)
        te_conv.shift(2.5*DOWN)
        self.add(te_conv)
        self.wait(2)

        # 4.2
        # Evidence shown in graphs of the limit
        self.next_section("4.2 Show evidence")
        self.clear()
        gradient_rect = my_background()
        self.add(gradient_rect)

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
                        x_axis_config={"include_numbers": False, 'tip_shape': BetterCurvyPointyTip},
                        y_axis_config={"include_numbers": True, 'include_tip': False}
                        )
            ft = sagemath.floor(t.get_value())
            i = 10**ft
            label = MathTex(f"10^{str(ft)}").scale(0.8)
            label.next_to(axes.c2p(i, 0), DOWN)
            axes.add(label)
            label1 = MathTex(f"10^{str(ft-1)}").scale(0.8)
            label1.next_to(axes.c2p(i/10, 0), DOWN)
            axes.add(label1)
            if t.get_value() < np.log10(5) + ft:
                i = ft - 1
            else:
                i = ft
            label2 = MathTex(f"5\\cdot 10^{str(i)}").scale(0.8)
            label2.next_to(axes.c2p(5*10**i, 0), DOWN)
            axes.add(label2)
            return axes

        axes = always_redraw(get_axes)
        self.add(axes)

        def get_graph():
            axes = get_axes()
            gr = VMobject(color=YELLOW)
            lit = [np.array([x, y]) for x, y in li if x < 0.9 * x_max(t.get_value())]
            gr.set_points_as_corners([axes.c2p(x, y) for x, y in lit])
            return gr

        gr = always_redraw(get_graph)
        self.add(gr)
        self.wait(2)

        # play from 10^3 to 10^(9)
        self.play(t.animate.set_value(9), run_time=15, rate_func=linear)
        self.wait(2)

        # compare to other curves

        self.clear()
        # plot several in logarithmic coordinates
        new_axes = Axes(
                        x_range=[3, 9, 1],
                        y_range=[0, 7, 1],
                        x_length=10,
                        y_length=5,
                        x_axis_config={"include_numbers": False, 'tip_shape': BetterCurvyPointyTip},
                        y_axis_config={"include_numbers": True, 'include_tip': False}
                        )
        for i in range(9):
            label = MathTex(f"10^{str(i)}").scale(0.5)
            label.next_to(new_axes.c2p(i, 0), DOWN)
            new_axes.add(label)
        self.add(new_axes)

        # first draw usual curve
        li = load_list(f"data/plotpts_curve_aa-4_up_to_9.json")
        graa = VMobject(color=YELLOW)
        graa.set_points_as_corners([new_axes.c2p(np.log10(x), y) for x, y in li if x > 1000])
        graa.set_style(stroke_width=1)
        self.add(graa)
        last_graa = graa

        # for each A draw the new draw and fade the old
        for aa in [-3, -2, -1, 0, 1, 2, 3, 4]:
            li = load_list(f"data/plotpts_curve_aa{aa}_up_to_9.json")
            graa = VMobject(color=YELLOW)
            graa.set_points_as_corners([new_axes.c2p(np.log10(x), y) for x, y in li if x > 1000])
            graa.set_style(stroke_width=1)
            if aa < 0:
                eqaa = MathTex(f"y^2 = x^3 - {-aa} \\,x + 1 ")
            elif aa == 0:
                eqaa = MathTex(r"y^2 = x^3 \phantom{-4\,x}+ 1 ")
            else:
                eqaa = MathTex(f"y^2 = x^3 + {aa} \\,x + 1 ")
            eqaa.to_edge(DOWN)
            self.add(eqaa)
            self.play(Create(graa),
                      FadeOut(last_graa),
                      run_time=2)
            last_graa = graa

        self.wait(1)


#  now render it
if __name__ == "__main__":
    with tempconfig({"renderer": "cairo", "quality": "medium_quality", "preview": True}):
        scene = FourthScene()
        scene.render()
