r"""
Part of the bsd_video

Here the actual conjecture is
explained and illustrated
with graphs.

"""

from manim import *
from sage.all import *
from character import StudentChar
from msage import smanim
from first_scene import subtitle


def my_background():
    r"""
    A gradient background
    """
    gradient_rect = Rectangle(
        width=config.frame_height,
        height=config.frame_width,
        fill_opacity=1,
    )
    gradient_rect.set_fill(
        color=[rgb_to_color([0.0, 0.0, 0.3]), BLACK],
        opacity=1
    )
    gradient_rect.rotate(PI/2)
    return gradient_rect


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
    li = Line(np.array([-1,0,0]), np.array([1,0,0]))
    fraction.add(num, li, den)
    fraction.arrange(DOWN, buff=0.2)
    v.add(lim, fraction)
    v.arrange(RIGHT, buff=.1)
    return v

def mq():
    r"""
    Writes M(Q) = # solutions modulo Q

    """
    te_mq1a = Tex(r"$\mathcal{M}($")
    te_mq1b = Tex("$Q$")
    te_mq1c = Tex(r"$)$")
    te_mq1d = Tex(r"$= \# $")
    te_mq1 = VGroup(te_mq1a, te_mq1b, te_mq1c, te_mq1d)
    te_mq1.arrange(RIGHT, buff=0.1)
    te_mq2 = Text("solutions").scale(0.8)
    te_mq3 = Text("modulo ").scale(.8)
    te_mq4 = Tex(r"$Q$")
    te_mqa = VGroup(te_mq3, te_mq4)
    te_mqa.arrange(RIGHT, buff=.2)
    te_mqa[1].shift(0.05 * DOWN)
    te_mqb = VGroup(te_mq2,te_mqa)
    te_mqb.arrange(DOWN, buff=0.1, aligned_edge=LEFT)
    te_mq = VGroup(te_mq1,te_mqb)
    te_mq.arrange(RIGHT, buff=0.2)
    return te_mq

class ThirdScene(Scene):

    def construct(self):
        gradient_rect = my_background()
        self.add(gradient_rect)

        # define N(T)
        te_defnt = Tex(r"$\mathcal{N}(T) = \# \Bigl\{ P\in E(\mathbb{Q}) \, : \, \lvert X\rvert, \lvert Y\rvert, \lvert Z\rvert \leq T \Bigr\} $")
        self.add(te_defnt)
        # now add an animation counting points
        self.wait(2)

        te_defmq = Tex(r"$\mathcal{M}(Q) = \# E\bigl({}^{\mathbb{Z}}\!/\!{}_{Q\mathbb{Z}}\bigr)$")
        self.remove(te_defnt)
        self.add(te_defmq)
        # add an animation counting points modulo increasing T
        self.wait(2)

        self.remove(te_defmq)
        te_compare = Text("Compare")
        te_compare.shift(2*LEFT)

        rhs = VGroup()
        te_nt1 = Tex(r"$\mathcal{N}(T)$")
        te_nt2 = Tex(r"$ = \# $")
        te_nt3 = Text("bounded \n" + "rational \n" + "solutions").scale(.8)
        te_nt = VGroup(te_nt1,te_nt2, te_nt3)
        te_nt.arrange(RIGHT, buff=0.2)

        te_mq = mq()  # M(Q) = # solutions modulo Q

        te_qt = Tex(r"$Q = T! = 1 \cdot 2 \cdots T$")
        rhs.add(te_nt,te_mq,te_qt)
        rhs.arrange(DOWN, buff=1.1, aligned_edge=LEFT)
        rhs.shift(3.5*RIGHT)
        self.add(rhs)

        new_te_mq4 = Tex(r"$T!$")
        te_mq4 = te_mq[1][1][1]
        new_te_mq4.shift(te_mq4.get_center())
        new_te_mq0 = Tex(r"$T!$")
        te_mq0 = te_mq[0][1]
        new_te_mq0.shift(te_mq0.get_center())
        self.play(Transform(te_mq4,new_te_mq4),
                  Transform(te_mq0, new_te_mq0),
                  run_time=1)
        self.wait(2)

        self.remove(te_compare)
        te_lim = limit_expression()  #  Tex(r"$\lim_{T\to\infty} \frac{T!\cdot \mathcal{N}(T)^2}{\mathcal{M}(T!)}$")
        te_lim.scale(2)
        te_lim.shift(3*LEFT)
        self.add(te_lim[1][1])  # ---
        self.wait(1)
        self.add(te_lim[1][0][2])  # N(T)^2
        self.wait(1)
        te_mt1 = te_lim[1][2]  # M(T!)
        te_mt2 = VGroup(te_mq[0][0], new_te_mq0, te_mq[0][2])
        self.play(Transform(te_mt2,te_mt1), run_time=2)
        self.wait(1)
        self.add(te_lim[1][0])  # numerator
        self.wait(1)
        self.add(te_lim[0])   # lim
        self.wait(1)

        self.remove(te_mq, te_qt, te_nt)
        self.play(te_lim.animate.move_to(ORIGIN), run_time=1)
        self.wait(1)

        te_con = Text("Conjecture", color=YELLOW)
        te_con.shift(2.5*UP+4*LEFT)
        self.add(te_con)
        te_conv = Text("converges to a positive real number.")
        te_conv.shift(2.5*DOWN)
        self.add(te_conv)
        self.wait(2)


#  now render it
if __name__ == "__main__":
    with tempconfig({"quality": "medium_quality", "preview": True}):
        scene = ThirdScene()
        scene.render()
