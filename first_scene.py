r"""
Part of the bsd_video

This uses the characters and introduces
elliptic curves with some 2d pictures.

"""

from manim import *
from sage.all import *
from character import StudentChar
from msage import smanim
from tools import subtitle, my_background, nature_background, thought_bubble


class FirstScene(Scene):

    def construct(self):
        # ##1.1
        bg_image = nature_background()
        self.add(bg_image)

        # initiate (needs to change a lot)
        st = StudentChar()
        te = StudentChar(height=1.2, width=0.8, colour=GREEN, lid_colour=DARK_GRAY)
        st.shift(LEFT)
        te.shift(RIGHT+0.1*UP)
        self.add(st, te)
        self.wait(1)
        self.add(thought_bubble())

        self.wait(1)
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

        # 1.2
        # what are elliptic curves
        # move chars out to corner
        self.remove(bg_image)
        self.add(my_background())
        self.play(
            st.animate.shift(np.array([-5, -3.3, 0.])),
            te.animate.shift(np.array([-6, -3.3, 0.])),
            run_time=1
        )

        # equation
        e1 = MathTex(r"y^2 = x^3", r"- 4\,", " x ", "+ 1")
        t1 = subtitle("It concerns equation like this...")
        self.add(e1, t1)
        self.wait(1)
        self.remove(t1)
        e2 = MathTex(r"y^2 = x^3", r" - 7\,", " x ", " + 6")
        t1 = subtitle("..or this")
        self.add(t1)
        self.play(Transform(e1, e2))
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
        framebox1 = SurroundingRectangle(e1[1], buff=.1)
        framebox2 = SurroundingRectangle(e1[3], buff=.1)
        self.add(framebox1, framebox2)

        # merge to another curve
        E2 = EllipticCurve([-7, 6])
        curve2 = smanim(E2.plot(color="yellow", thickness=2, alpha=0.3, xmax=7, ymin=-5, ymax=5))
        curve2.set_z_index(3)
        self.play(
            Transform(curve, curve2),
            Transform(e1, e2),
            run_time=1
        )
        self.wait(1)

        # try to give lots of curves
        ABs = [(-7,6), (-4,1), (9,1), (0,2), (-3,-1)]
        for A,B in ABs:
            self.remove(e1, curve)
            E2 = EllipticCurve([A, B])
            curve = smanim(E2.plot(color="yellow", thickness=2, alpha=0.3, xmax=7, ymin=-5, ymax=5))
            curve.set_z_index(3)
            if A >= 0:
                Astr = fr"+{A}\,"
            else:
                Astr = fr"-{-A}\,"
            if B >= 0:
                Bstr = fr"+{B}"
            else:
                Bstr = fr"-{-B}"
            e1 = MathTex(r"y^2 = x^3 ", Astr, " x ", Bstr)
            e1.to_corner(UL)
            self.add(curve, e1)
            self.wait(1)

# https://github.com/3b1b/manim/issues/760
# cap = cv2.VideoCapture("repressilator_animate.mov")
#        flag = True
#        while flag:
#            flag, frame = cap.read()
#            if flag:
#                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#                frame_img = ImageMobject(frame)
#                self.add(frame_img)
#                self.wait(0.04)
#                self.remove(frame_img)
#        cap.release()

# now render it
if __name__ == "__main__":
    with tempconfig({"quality": "medium_quality", "preview": True}):
        scene = FirstScene()
        scene.render()
