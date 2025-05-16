from manim import *
from sage.all import *
from character import StudentChar
from msage import smanim

class FirstScene(Scene):
    def construct(self):
        st = StudentChar(centre=np.array([-6,-3.3,0.]))
        te = StudentChar(height=1.2, width=0.8,centre=np.array([-4.5,-3.3,0.]), colour=GREEN, lid_colour=DARK_GRAY, )
        self.add(st, te)
        te.half_close_right_eye()
        self.wait(0.3)
        te.open_right_eye()
        self.wait(0.5)

        # equation
        e1 = MathTex("y^2 = x^3 +4x+1")
        self.add(e1)
        p1 = MathTex("Y^2Z = X^3 + 4XZ^2+Z^3")
        self.play(Transform(e1,p1))
        self.wait(2)
        self.play(FadeOut(p1))

        # plot elliptic curve
        E = EllipticCurve(RR, [-.25,0.1])
        curve = smanim(E.plot(color="yellow", thickness=2, alpha=0.3, xmax = 7, ymin= -5, ymax = 5))
        self.play(Create(curve))
        self.wait(2)




with tempconfig({"quality": "medium_quality", "preview": True}):
    scene = FirstScene()
    scene.render()