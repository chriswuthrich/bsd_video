from manim import *
from sage.all import *
from character import StudentChar
from msage import smanim
from first_scene import subtitle


class ThirdScene(Scene):

    def construct(self):

        te_compare = Text("Compare")
        te_compare.shift(2*LEFT)

        rhs = VGroup()

        te_nt1 = Tex(r"$\mathcal{N}(T) = $")
        te_nt2 = Tex("bounded rational \n solutions")
        te_nt = VGroup(te_nt1,te_nt2)
        te_nt.arrange(RIGHT)

        te_mq1 = Tex(r"$\mathcal{M}(Q) = $")
        te_mq2 = Tex(r"solutions \\ modulo ", r"$Q$")
        te_mq = VGroup(te_mq1,te_mq2)
        te_mq.arrange(RIGHT)

        te_qt = Tex(r"$Q = T! = 1 \cdot 2 \cdots T$")
        rhs.add(te_nt,te_mq,te_qt)
        rhs.arrange(DOWN, buff=1.1)
        rhs.shift(3*RIGHT)
        self.add(rhs)
        self.wait(2)


        self.remove(te_compare)
        te_lim = Tex(r"$\lim_{T\to\infty} \frac{T!\cdot \mathcal{N}(T)^2}{\mathcal{M}(T!)}$")
        te_lim.scale(2)
        te_lim.shift(2*LEFT)
        self.add(te_lim)
        self.wait()

        self.remove(te_mq, te_qt, te_nt)
        self.play(te_lim.animate.move_to(ORIGIN), run_time=1)
        self.wait(1)

        te_con = Text("Conjecture", color=YELLOW)
        te_con.shift(2*UP+3*LEFT)
        self.add(te_con)
        te_conv = Text("converges to a positive real number.")
        te_conv.shift(2*DOWN)
        self.add(te_conv)
        self.wait(2)


#  now render it
if __name__ == "__main__":
    with tempconfig({"quality": "medium_quality", "preview": True}):
        scene = ThirdScene()
        scene.render()
