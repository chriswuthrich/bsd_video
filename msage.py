r"""
File to implement conversion of sage plots to
manim objects

This is implemented in the function
smanim( some Graphics )

Problems: How to convert the coordinate system,
implement more 2d ojects
3d objects
"""



from manim import *
from sage.all import *



def smanim(gr):
    """
    If the Graphics gr is a primitive, we return a VMobject
    otherwise a VGroup
    """
    if isinstance(gr, sage.plot.graphics.Graphics):
        v = VGroup()
        components = list(gr)
        if len(components)==1:
            return sage_to_vmobject(gr[0])
        else:
            for g in list(gr):
                v.add( sage_to_vmobject(g) )
            return v
    else:
        raise NotImplementedError("Not yet done")

def sage_to_vmobject(g):
    """
    Turn a single Graphics primitive to a VMoject
    """
    if isinstance(g, sage.plot.line.Line):
        return sline_to_vmobject(g)
    else:
        raise NotImplementedError("Not yet done")

def sline_to_vmobject(g):
    r"""
    Turn a sage line into a VMObject
    """
    colour = ManimColor.from_rgb(g.options()['rgbcolor'])
    P0, *pts = list(g)
    first_vertex = np.array([P0[0], P0[1], 0.])

    if len(pts) == 1:
        v = Line(first_vertex,np.array([pts[0][0],pts[0][1],0.]))
        v.set_stroke(colour)
        return v
    else:
        v = VMobject(stroke_color=colour)
        v.start_new_path(first_vertex)
        v.add_points_as_corners( [np.array([P[0], P[1], 0]) for P in pts] )
        v.scale_to_fit_width()
        return v


class MySc(Scene):
    def construct(self):
        # test line
        sli1 = line([(-1., 0.), (1., 0.3)])
        li1 = smanim(sli1)
        sli2 = line([(0,0), (1.3,0.8)])
        li2 = smanim(sli2)
        print(li1,li2)
        print(config["frame_x_radius"], config["frame_y_radius"])
        print(li1.is_off_screen())
        self.play(Create(li1))
        self.play(Transform(li1,li2))
        self.wait(1)

        # E = EllipticCurve([RR(-.25), RR(0.01)])
        # gr = E.plot(xmin=-1,xmax=1,ymin=-1,ymax=+1)
        # curve = svgroup(gr)
        # self.add(curve)


with tempconfig({"quality": "medium_quality", "preview": True}):
    scene = MySc()
    scene.render()