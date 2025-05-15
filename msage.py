from manim import *
from sage.all import *

from sage.schemes.elliptic_curves.constructor import EllipticCurve
# from sage.plot.line import Line as SageLine

def sage_graphics_to_vmobject(gr):
    if isinstance(gr, sage.plot.graphics.Graphics):
        v = VGroup()
        for g in gr._objects:
            v.add( sage_graphics_to_vmobject(g) )
        return v
    elif isinstance(gr, sage.plot.line.Line):
        colour = ManimColor.from_rgb(gr.options()['rgbcolor'])
        P0, *pts = list(gr)
        v = VMobject(stroke_color=colour)
        first_vertex = np.array([P0[0],P0[1],0.])
        v.start_new_path(first_vertex)
        # print(first_vertex)
        v.add_points_as_corners( [np.array([P[0], P[1], 0]) for P in pts] )
        return v
    else:
        raise NotImplementedError("Not yet done")


class MySc(Scene):
    def construct(self):
        # E = EllipticCurve([RR(-.25), RR(0.01)])
        # gr = E.plot()
        # curve = sage_graphics_to_vmobject(gr)
        # self.add(curve)
        # li = line([(-1.,0.),(1.,0.3)])
        # self.wait(1)
        # self.add(sage_graphics_to_vmobject(li))
        # self.wait(1)
        d = Dot(color=RED, radius=0.2)
        d.move_to([-3, 2, 0])

        self.play(Write(d))
        self.play(d.animate.move_to([5, -1, 0]))
        self.play(d.animate.move_to(ORIGIN))
        self.play(Unwrite(d))
        corners = (
                        # create square
                        UR, UL,
                        DL, DR,
                        UR,
                        # create crosses
                        DL, UL,
                        DR
                    )
        vmob = VMobject(stroke_color=RED)
        vmob.set_points_as_corners(corners).scale(2)
        self.add(vmob)

with tempconfig({"quality": "medium_quality", "preview": True}):
    scene = MySc()
    scene.render()