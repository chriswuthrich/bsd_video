from manim import *
from sage.all import *
from character import StudentChar
from msage import smanim


def subtitle(said):
    r"""
    This prints a text in small white at the bottom of the screen.
    """
    v = Text(said, font_size=15, color="white", font="sans-serif")
    v.shift(3*DOWN)
    v.set_z_index(1) # a bit in the foreground
    return v


class FirstScene(Scene):
    def construct(self):
        st = StudentChar(centre=np.array([-6, -3.3, 0.]))
        te = StudentChar(height=1.2, width=0.8, centre=np.array([-4.5, -3.3, 0.]), colour=GREEN, lid_colour=DARK_GRAY)
        t1 = subtitle("Do you know the Riemann hypothesis?")
        self.add(st, te, t1)
        te.half_close_right_eye()
        self.wait(0.3)
        te.open_right_eye()
        self.wait(0.5)
        self.remove(t1)
        t2 = subtitle("Yeah, and you have heard of BSD?")
        self.add(t2)

        # equation
        e1 = MathTex("y^2 = x^3 +4x+1")
        self.add(e1)
        p1 = MathTex("Y^2Z = X^3 + 4XZ^2+Z^3")
        self.play(Transform(e1, p1))
        self.wait(2)
        self.play(FadeOut(e1))

        # plot elliptic curve
        axes = NumberPlane()
        axes.set_z_index(0.1)
        self.add(axes)
        E = EllipticCurve(RR, [-.25, 0.1])
        curve = smanim(E.plot(color="yellow", thickness=2, alpha=0.3, xmax=7, ymin=-5, ymax=5))
        curve.set_z_index(3)
        self.play(Create(curve))
        self.wait(1)

        #
        self.wait(2)


# now render it
if __name__ == "__main__":
    with tempconfig({"quality": "medium_quality", "preview": True}):
        scene = FirstScene()
        scene.render()
