r"""
Part of the bsd_video

This will contain the intro
of projective coordinates
by going to a 3D scene.

Due to bugs this is not done
and renders slowly.

"""

from manim import *
from manim.opengl import *
import sage.all as sagemath
from character import StudentChar
from msage import smanim
from tools import *


def calc_curve():
    # Do the sage calculations to
    # get the curve and its rational points EQ
    E = sagemath.EllipticCurve([-4, 1])

    P, Q = E.gens()
    EQ = []
    for n in [-3, -2, -1, 0, 1, 2, 3]:
        for m in range(-13, 13):
            R = n * P + m * Q
            if R != 0:
                EQ.append(R)
    EQ.sort(key=lambda R: R.height())

    return E, EQ


def my_latex(R):
    """
    Return the latexed version of a
    rational point
    """
    xx = R[0]
    yy = R[1]
    return r"\bigl(" + xx._latex_() + "," + yy._latex_() + r"\bigr)"


def pt_with_label(R, dir=UR):
    """
    plot a point at R and label it with the rational coordinates
    dir is the direction in which the label is off the dot
    """
    sc = 0.3  # how much distance between them
    v = Sphere(center=np.array([R[0], R[1], 0]), radius=0.05, color=WHITE)
    lastr = my_latex(R)
    la = MathTex(lastr, color=YELLOW_A)
    la.move_to(np.array([R[0], R[1], 0.])+sc*dir)
    return v, la

def path(pts, colour=WHITE, **kwargs):
    v = VMobject(stroke_color=colour, **kwargs)
    v.start_new_path(pts[0])
    v.add_points_as_corners(pts[1:])
    v.make_smooth()
    return v

def dummy_curve():
    """ Curve to display with few points only no precalculation """
    li = [(29.4069687323273, 159.102579768869),
             (18.5558451565427, 79.4727242193263),
             (14.1839020946821, 52.8944749670282),
             (11.7262277758544, 39.5790754415291),
             (10.1187887022127, 31.5687575733752),
             (8.97066530771083, 26.2109179055659),
             (8.10165070958815, 22.3687141460578),
             (7.41619491447776, 19.4737142746493),
             (6.85853538093578, 17.2101128833461),
             (6.39376390014999, 15.3884176858763),
             (5.99882183547338, 13.8880342695749),
             (5.65781679020570, 12.6285584472365),
             (5.35941122265808, 11.5543182694121),
             (5.09528270060630, 10.6255408657860),
             (4.85917339148022, 9.81305252752575),
             (4.64628032827383, 9.09496623640533),
             (4.45285130986880, 8.45453827892505),
             (4.27590946907810, 7.87873929984326),
             (4.11306091336658, 7.35727657909984),
             (3.96235749116391, 6.88190960235587),
             (3.82219703585803, 6.44596115892533),
             (3.69124964709792, 6.04396175204804),
             (3.56840241904170, 5.67138674627703),
             (3.45271747499337, 5.32445920162396),
             (3.4695648421091643, 5.374750833741052),
             (3.066992086080393, 4.193031134234696),
             (2.660875126026444, 3.032520030131728),
             (2.255573830329872, 1.8582766495268068),
             (1.9409259929060723, 0.7403649237419704),
             (1.8638334808854342, 0.13925180616285376),
             (1.8812097842720061, -0.36423715331547174),
             (2.0825905509946057, -1.304689606470304),
             (2.410536193850231, -2.316186759721809),
             (2.792956787977554, -3.4080687858887733),
             (3.1999194600953365, -4.578847893959676)]
    lip = [vec(a[0], a[1]) for a in li]
    return path(lip)



def my_numberplane(x_range=np.array([-50, 50, 1]),
                   y_range=np.array([-10, 100, 1]),
                   colour=TEAL,
                   thickness=0.001):
    """
    Version of NumberPlane used in 3D
    """
    v = VGroup()
    xx = x_range[0]
    yy = y_range[0]
    while yy < y_range[1]:
        v.add(Line3D(
            np.array([x_range[0], yy, 0]),
            np.array([x_range[1], yy, 0]),
            thickness=thickness,
            color=colour if xx!=0 else WHITE))
        yy += y_range[2]
    while xx < x_range[1]:
        v.add(Line3D(
            np.array([xx, y_range[0], 0]),
            np.array([xx, y_range[1], 0]),
            thickness=thickness,
            color=colour if xx != 0 else WHITE))
        xx += x_range[2]
    return v


# try creating curve with parametric plot
# doesn't work
def curve_again():
    E = sagemath.EllipticCurve([-4, 1])
    wp = E.weierstrass_p().truncate(20)
    wp2 = wp.derivative()
    om1, om2 = E.period_lattice().basis()

    def func(t):
        return np.array([wp(t), wp2(t), 0])

    v = ParametricFunction(func, t_range=(-om1 / 2, om1 / 2)).set_color(RED_A)
    return v


class SecondScene(ThreeDScene):

    def construct(self):

        # copied from first scene:
        bgr = my_background()
        shz(bgr, -1)
        st = StudentChar()
        te = StudentChar(height=1.2, width=0.8, colour=GREEN, lid_colour=DARK_GRAY)
        st.scale(1)
        te.scale(1)
        stte = VGroup(st, te)
        stte.arrange()
        stte.to_corner(DL)
        grid = VGroup()
        grid.add(my_fading_numberplane())
        grid.add(Line(vec(0, -4), vec(0, 4), color=WHITE, stroke_width=2))
        xline = Line(vec(-7, 0, .1), vec(7, 0, .1), color=WHITE, stroke_width=2)
        grid.add(xline)
        shz(grid, 1)
        axex = Arrow(start=vec(0,0),
                     end=vec(6.5,0),
                     buff=0,
                     stroke_width=2,
                     tip_length=0.2,
                     tip_shape=BetterCurvyPointyTip,
                     color=WHITE)
        axey = Arrow(start=vec(0, 0),
                     end=vec(0, 3.7),
                     buff=0,
                     stroke_width=2,
                     tip_length=0.2,
                     tip_shape=BetterCurvyPointyTip,
                     color=WHITE)
        label_x = MathTex(r"x")
        label_x.scale(.8)
        label_x.move_to(vec(6.5, -0.4))
        label_y = MathTex(r"y")
        label_y.scale(.8)
        label_y.move_to(vec(0.4, 3.5))
        labelled_axes = VGroup(axex, axey, label_x, label_y)
        shz(labelled_axes,1)
        E = sagemath.EllipticCurve([-4, 1])
        curve = smanim(E.plot(color="yellow", thickness=2, alpha=0.3, xmax=7, ymin=-5, ymax=5))
        shz(curve, 5)
        e1 = MathTex(r"y^2 = x^3", r"- 4\,", " x ", "+ 1")
        e1.to_corner(UL)
        shz(e1, 5)

        self.add(bgr, grid, labelled_axes, stte)
        self.add(e1, curve)




    def not_used_right_now(self):
        E, EQ = calc_curve()
        # phi = 0 from above theta = -90 gives 2d view
        # self.camera.frame.move_to((0,0,5))
        # self.renderer.camera.set_camera_orientation(
        #     phi=0,
        #     theta=-PI/2,
        #     frame_center=[0, 0, 5],
        #     distance=5
        # )  # self.set_camera_orientation(phi=0, theta=-PI/2, frame_center=(0,0,5), distance=5)
        self.renderer.camera.phi = 0
        self.renderer.camera.theta = -PI / 2
        self.renderer.camera.distance = 5
        self.renderer.camera.frame_center = [0, 0, 5]

        nu = my_numberplane()
        self.add(nu)
        # self.add(smanim(E.plot(xmin=-3, xmax=1000, ymin=-1000, ymax=1000, color="yellow")))
        # cu = curve_again()
        cu = dummy_curve()
        self.add(cu)

        for R in EQ[:5]:
            v, la = pt_with_label(R)
            self.add(v, la)
            self.wait(1)
            self.remove(la)

        pts_in_pic = []
        vpts = VGroup()
        for R in EQ[:10]:  # do more but restrict better later
            rr = vec(R[0], R[1])
            pts_in_pic.append(rr)
            vpts.add(Dot3D(rr))

        self.add(vpts)
        self.wait(2)
        #
        # number_of_grid_changes = 5
        # y_grid_steps = [1, 2, 4, 8, 8]
        # x_grid_steps = [1, 2, 2, 4, 4]
        # for i in range(number_of_grid_changes):
        #     self.remove(nu)
        #     if i == 0:
        #         rf = rate_functions.ease_in_sine
        #     elif i == number_of_grid_changes - 1:
        #         rf = rate_functions.ease_out_sine
        #     else:
        #         rf = rate_functions.linear
        #     # nu = my_numberplane(
        #     #            x_range=np.array([-50, 50, x_grid_steps[i]]),
        #     #            y_range=np.array([-10, 100, y_grid_steps[i]]),
        #     #            colour=TEAL,
        #     #            thickness=0.01)
        #     # self.add(nu)
        #     phi_end = PI/2 * i/number_of_grid_changes
        #     frame_centre = -10*i/number_of_grid_changes
        #     self.move_camera(phi=phi_end, frame_center=(0, frame_centre, 5), rate_func=rf)

        self.move_camera(phi=PI/2, frame_center=(0, -10, 5))
        self.wait(1)
        self.play(Uncreate(vpts))
        self.wait(2)


# now render it
if __name__ == "__main__":
    with tempconfig({"renderer": "cairo", "quality": "medium_quality", "preview": True}):
        scene = SecondScene()
        scene.render()
