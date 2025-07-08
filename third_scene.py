r"""
Part of the bsd_video

Here the actual conjecture is
explained and illustrated
with graphs.

TODO

"""

from manim import *
import sage.all as sagemath
from character import StudentChar
from msage import smanim
from tools import *
import json




class ThirdScene(Scene):

    def construct(self):

        # 3.1 Count global points
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

        # Title comes in
        tit = Text("Counting rational points", color=YELLOW)
        tit.shift(2*UP)
        self.play(GrowFromCenter(tit))
        self.wait(.5)
        ee = MathTex(r"Y^2 Z = X^3- 4\,XZ^2+ Z^3")
        ee.to_corner(UL)
        shz(ee, 5)
        self.add(ee)
        self.play(FadeOut(tit, shift=DOWN * 2, scale=1.5))
        self.wait(1)

        # recreate curve
        grid = VGroup()
        grid.add(my_fading_numberplane())
        grid.add(Line(vec(0, -4), vec(0, 4), color=WHITE, stroke_width=2))
        # xline = Line(vec(-7, 0, .1), vec(7, 0, .1), color=WHITE, stroke_width=2)
        # grid.add(xline)
        shz(grid, 1)
        # axex = Arrow(start=vec(0,0),
        #              end=vec(6.5,0),
        #              buff=0,
        #              stroke_width=2,
        #              tip_length=0.2,
        #              tip_shape=BetterCurvyPointyTip,
        #              color=WHITE)
        # axey = Arrow(start=vec(0, 0),
        #              end=vec(0, 3.7),
        #              buff=0,
        #              stroke_width=2,
        #              tip_length=0.2,
        #              tip_shape=BetterCurvyPointyTip,
        #              color=WHITE)
        # axes = VGroup(axex, axey)
        # shz(axes,1)
        E = sagemath.EllipticCurve([-4, 1])
        curve = smanim(E.plot(color="yellow", thickness=2, alpha=0.3, xmax=7, ymin=-5, ymax=5))
        shz(curve, 5)
        curvepic = VGroup(grid, curve)
        curvepic.shift(2*RIGHT)
        self.add(curvepic, stte)

        # points ordered by naive height
        pts = [ r"$(0$, & $1$, & $0)$",
                r"$(0$, & $\pm 1$, & $1)$",
                r"$(-1$, & $\pm 2$, & $1)$",
                r"$(-1$, & $\pm 2$, & $1)$",
                r"$(2$, & $\pm 1$, & $1)$",
                r"$(-2$, & $\pm 1$, & $1)$",
                r"$(3$, & $\pm 4$, & $1)$",
                r"$(4$, & $\pm 7$, & $1)$",
                r"$(2$, & $\pm 1$, & $8)$",
                r"$(-14$, & $\pm 13$, & $8)$",
                r"$(10$, & $\pm 31$, & $1)$",
                r"$(-6$, & $\pm 37$, & $27)$",
                r"$(12$, & $\pm 41$, & $1)$",
                r"$(-24$, & $\pm 53$, & $27)$",
                r"$(20$, & $\pm 89$, & $1)$",
                r"$(30$, & $\pm 29$, & $125)$",
                r"$(132$, & $\pm 79$, & $64)$",
                r"$(132$, & $\pm 79$, & $64)$",
                r"$(-80$, & $\pm 227$, & $125)$",
                r"$(-630$, & $\pm 503$, & $343)$",
                r"$(644$, & $\pm 113$, & $343)$",
                r"$(455$, & $\pm 736$, & $125)$",
                r"$(1160$, & $\pm 967$, & $512)$",
                r"$(114$, & $\pm 1217$, & $1)$",
                r"$(1386$, & $\pm 377$, & $729)$",
                r"$(-130$, & $\pm 2443$, & $2197)$",
                r"$(-1683$, & $\pm 2674$, & $1331)$",
                r"$(-2728$, & $\pm 1021$, & $1331)$",
                r"$(705$, & $\pm 3592$, & $27)$",
                r"$(1045$, & $\pm 4306$, & $6859)$"
               ]
        # lei[T] gives the number of items in
        # pts with height < T
        lei = {10:9, 30:10, 50:13, 100:15, 200:18, 1000:22, 5000:29}

        template = TexTemplate()
        template.add_to_preamble(r"\usepackage{booktabs}")

        def list_of_points(T):
            n = lei[T]
            tstr = r"\begin{tabular}{rcl} "
            for P in pts[:n-1]:
                tstr += P + r" \\ " + "\n"
            tstr += pts[n-1]
            tstr += r"\end{tabular}"
            v = Tex(tstr, tex_template=template)
            v.scale(.5)
            v.move_to(vec(-5,2))
            return v

        v1 = list_of_points(10)

        bdt = MathTex(r"\lvert X\rvert,\, \lvert Y \rvert\, \lvert Z\rvert < 10")
        bdt.to_edge(UP)
        self.play(FadeIn(v1),
                  FadeIn(bdt),
                  ee.animate.to_corner(DR),
                  run_time=1)
        self.wait(1)
        self.play(FadeOut(v1))
        self.wait(1)
        #
        # # box
        # mask_height = 6
        # mask_width = 6
        # mask = Rectangle(height=mask_height, width=mask_width, color=TEAL)
        # mask.set_stroke(WHITE, 2)
        # # mask.move_to(ORIGIN)
        #
        # # Only show items within the mask area
        # clipped_items = item_group.copy()
        # clipped_items.add(mask)
        # clipped_items = Group(clipped_items).set_z_index(1)
        #
        # # Add a simulated scrollbar
        # scrollbar = Rectangle(width=0.1, height=mask_height, color=GREY_B)
        # thumb_height = mask_height * (mask_height / item_group.height)
        # scrollbar_thumb = Rectangle(width=0.1, height=thumb_height, fill_color=WHITE, fill_opacity=1)
        # scrollbar.next_to(mask, RIGHT, buff=0.1)
        # scrollbar_thumb.move_to(scrollbar.get_top() - DOWN * thumb_height / 2)
        # scrollbar_thumb.set_z_index(2)
        #
        # # Masking is simulated using z-order — not true clipping
        # self.add(mask, clipped_items, scrollbar, scrollbar_thumb)
        #
        # # Animate scroll down
        # self.play(
        #     item_group.animate.shift(UP * 3),
        #     scrollbar_thumb.animate.shift(DOWN * 1.5),
        #     run_time=2
        # )

#  now render it
if __name__ == "__main__":
    with tempconfig({"renderer": "cairo", "quality": "medium_quality", "preview": True}):
        scene = ThirdScene()
        scene.render()
