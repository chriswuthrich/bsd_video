r"""
Part of the bsd_video

Version for split up

File to implement conversion of sage plots to
manim objects

This is implemented in the function
smanim( some Graphics )

Remember to give sage objects colours that are visible on a dark background.

Problems:
implement more 2d objects
3d objects
"""


from manim import *
import sage.all as sagemath
#from sage.schemes.elliptic_curves.constructor import EllipticCurve
from sage.plot.line import Line as sagemathLine


def smanim(gr):
    """
    If the Graphics gr is a primitive, we return a VMobject
    otherwise a VGroup
    """
    if isinstance(gr, sagemath.Graphics):
        v = VGroup()
        components = list(gr)
        if len(components) == 1:
            return sage_to_vmobject(gr[0])
        else:
            for g in list(gr):
                v.add(sage_to_vmobject(g))
            return v
    else:
        raise NotImplementedError("Not yet done")


def sage_to_vmobject(g):
    """
    Turn a single Graphics primitive to a VMoject
    """
    if isinstance(g, sagemathLine):
        return sline_to_vmobject(g)
    else:
        raise NotImplementedError("Not yet done")


def sline_to_vmobject(g):
    r"""
    Turn a sage line into a VMObject
    thickness, colour and opacity is copied over, the line style not.
    """
    colour = ManimColor.from_rgb(g.options()['rgbcolor'])
    alpha = float(g.options()["alpha"])
    thickness = float(g.options()["thickness"])
    P0, *pts = list(g)
    first_vertex = np.array([P0[0], P0[1], 0.])
    if len(pts) == 1:
        v = Line(first_vertex, np.array([pts[0][0], pts[0][1], 0.]), stroke_width=4*thickness)
        print(first_vertex, pts, np.array([pts[0][0], pts[0][1], 0.]))
        v.set_stroke(colour, opacity=alpha)
        return v
    else:
        v = VMobject(stroke_color=colour, stroke_width=4*thickness)
        v.start_new_path(first_vertex)
        v.add_points_as_corners([np.array([P[0], P[1], 0]) for P in pts])
        v.make_smooth()
        return v


class Test_smanim(Scene):
    def construct(self):
        # a manim line
        li0 = Line(ORIGIN, UL)
        self.play(Create(li0))
        # self.add(Text(f" Hello {li0.width}, {li0.depth}, {li0.height}")) gives 1, 0, 1
        self.wait(1)

        # test line
        sli1 = sagemath.line([(-7., 0.), (1., 3.9)], color="white")
        li1 = smanim(sli1)
        sli2 = sagemath.line([(0, 0), (1.3, 0.8)], color="yellow")
        li2 = smanim(sli2)
        self.play(Create(li1))
        self.play(Transform(li1, li2))
        self.wait(1)

        sli3 = sagemath.line([(sagemath.cos(n*PI/7), sagemath.sin(n*PI/7+0.1)-0.5) for n in sagemath.srange(6)], color="red")
        li3 = smanim(sli3)
        self.play(Create(li3))
        self.play(Wiggle(li3))

        # test plot of an elliptic curve
        E = sagemath.EllipticCurve([sagemath.RR(-.25), sagemath.RR(0.01)])
        gr = E.plot(color="yellow", xmin=-7.1, xmax=7.1, ymin=-3.8, ymax=3.8)
        curve = smanim(gr)
        self.add(curve)
        self.wait(.5)

        # test a function plot
        gr = sagemath.plot(sagemath.sin, (-7, 7), color="white", alpha=0.5, thickness=3)
        self.add(smanim(gr))
        self.wait(2)


if __name__ == "__main__":
    with tempconfig({"renderer": "cairo",
                     "quality": "medium_quality",
                     "disable_caching": True,
                     "preview": True}):
        scene = Test_smanim()
        scene.render()
