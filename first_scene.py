from manim import *
from sage.all import *
from character import StudentChar
from msage import smanim


def subtitle(said):
    r"""
    This prints a text in small white at the bottom of the screen.
    """
    vt = Text(said, font_size=15, color="white", font="sans-serif")

    # Create a black rectangle with size matching the text
    background_box = Rectangle(
        width = vt.width + 0.1,  # Add some padding around the text
        height = vt.height + 0.1,  # Add some padding around the text
        color = BLACK
    )
    background_box.set_fill(BLACK, opacity=1)  # Set the fill color to black

    # add them together and shift to bottom of screen
    v = VGroup()
    v.add(background_box)
    v.add(vt)
    v.to_edge(DOWN)
    v.set_z_index(1) # a bit in the foreground
    return v


class FirstScene(Scene):

    def construct(self):
        # initiate (needs to change a lot)
        st = StudentChar()
        te = StudentChar(height=1.2, width=0.8, colour=GREEN, lid_colour=DARK_GRAY)
        st.shift(LEFT)
        te.shift(RIGHT+0.1*UP)
        self.add(st, te)
        self.wait(1)
        t1 = subtitle("Are you working on the Riemann hypothesis?")
        t1.shift(LEFT)
        self.add(t1)
        self.wait(1)
        self.remove(t1)
        t1 = subtitle("No, my work is connected to another important conjecture in number theory.")
        t1.shift(2*RIGHT)
        self.add(t1)
        st.half_close_left_eye()
        self.wait(.3)
        st.open_left_eye()
        self.wait(1)
        self.remove(t1)
        t1 = subtitle("What is that about")
        t1.shift(2*LEFT)
        self.add(t1)
        self.wait(1)

        # 2
        # what are elliptic curves
        # move chars out to corner
        self.remove(t1)
        self.play(
            st.animate.shift(np.array([-5, -3.3, 0.])),
            te.animate.shift(np.array([-6, -3.3, 0.])),
            run_time=1
        )

        # equation
        e1 = MathTex(r"y^2 = x^3 - 4\,x + 1")
        t1 = subtitle("It concerns equation like this...")
        self.add(e1,t1)
        self.wait(1)
        self.remove(t1)
        e2 = MathTex(r"y^2 = x^3 - 7\,x + 6")
        t1 = subtitle("..or this")
        self.add(t1)
        self.play(Transform(e1,e2))
        self.wait(1)

        # plot elliptic curve
        axes = NumberPlane()
        axes.set_z_index(0.1)
        self.add(axes)
        E = EllipticCurve([-4, 1])
        curve = smanim(E.plot(color="yellow", thickness=2, alpha=0.3, xmax=7, ymin=-5, ymax=5))
        curve.set_z_index(3)
        self.remove(e2)
        e2.to_corner(UL)
        self.add(e1)
        self.play(
            Create(curve),
            e1.animate.to_corner(UL),
            run_time=1
        )
        self.wait(1)

        # merge to another curve
        E2 = EllipticCurve([-7, 6])
        curve2 = smanim(E2.plot(color="yellow", thickness=2, alpha=0.3, xmax=7, ymin=-5, ymax=5))
        curve2.set_z_index(3)
        self.play(
            Transform(curve, curve2),
            Transform(e1,e2),
            run_time=1
        )
        self.wait(1)

        # try to give lots of curves
        ABs = [(-7,6), (-4,1), (9,1), (0,2), (-3,-1)]
        for A,B in ABs:
            self.remove(e1,curve)
            E2 = EllipticCurve([A,B])
            curve = smanim(E2.plot(color="yellow", thickness=2, alpha=0.3, xmax=7, ymin=-5, ymax=5))
            curve.set_z_index(3)
            if A>=0:
                Astr = fr"+{A}\,"
            else:
                Astr = fr"-{-A}\,"
            if B>= 0:
                Bstr = fr"+{B}"
            else:
                Bstr = fr"-{-B}"
            e1 = MathTex(r"y^2 = x^3 "+Astr+" x "+Bstr)
            e1.to_corner(UL)
            self.add(curve,e1)
            self.wait(1)


# now render it
if __name__ == "__main__":
    with tempconfig({"quality": "medium_quality", "preview": True}):
        scene = FirstScene()
        scene.render()
