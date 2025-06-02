from manim import *
from sage.all import *
from character import StudentChar
from msage import smanim
from first_scene import subtitle


class ThirdScene(Scene):

    def construct(self):

        te_compare = Text("Compare")
        te_compare.shift(2*LEFT)
        te_nt = Tex(r"$\mathcal{N}(T) = $ bounded rational solutions")
        te_nt.shift(2*RIGHT+1*UP)
        te_mq = Tex(r"$\mathcal{M}(Q) = $",  " solutions modulo ", r"$Q$")
        te_mq.shift(2*RIGHT+1*DOWN)
        te_mq.set_color_by_tex("Q", RED)
        self.add(te_compare, te_nt, te_mq)
        self.wait(2)

        self.remove(te_compare)





#  now render it
if __name__ == "__main__":
    with tempconfig({"quality": "medium_quality", "preview": True}):
        scene = ThirdScene()
        scene.render()
