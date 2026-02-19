r"""
split scene
3.13 - 14

3-D

"""

from manim import *
import sage.all as sagemath
from tools import vec, shz, dot_on_curve
from msage import smanim


def dot_on_3dcurve(centre=ORIGIN, colour=YELLOW, radius=0.1, z_index=10):
    """
    version of dot_on_curve but for the fake 3d curve
    """
    v = Dot3D(centre, color=colour, radius=radius, z_index=z_index)
    return v

def fake_numberplane():
    """
    Projective version of number plane for 3D view at infinity
    The point (0:1:0) is at (0,100),
    The points (1:0:0), (0,0) and (0,4) are fixed
    """
    colour = TEAL
    colour2 = TEAL_A
    thickness = 0.001
    v = VGroup()
    ymin = -10  # don't draw behind the camera.

    # filled rectangle at the horizon
    nu2 = 100
    yy = 100 * nu2 / (nu2 + 96)
    p = Polygon(
        vec(-50, yy), vec(50, yy), vec(100, 100), vec(-100, 100),
        stroke_width=0,
        fill_color=colour,
        fill_opacity=.8,
        color=colour)
    shz(p, -1)
    v.add(p)

    # horizontal lines y=const
    for yy in range(ymin, nu2):
        y2 = 100*yy/(yy+96)
        v.add(Line3D(
            vec(-30, y2),
            vec(30, y2),
            thickness=thickness,
            color=colour2 if yy != 0 else WHITE))

    # lines x=const meeting at O
    nu1 = 100
    for xx in range(-nu1, nu1):
        v.add(Line3D(
            vec(xx * (1 - ymin / 100), ymin),
            vec(0, 100),
            thickness=thickness,
            color=colour if xx != 0 else WHITE))

    # horizont line
    v.add(Line3D(
        vec(-100, 100),
        vec(100, 100),
        color=WHITE,
        thickness=thickness))

    # redraw axes
    v.add(Line3D(
            vec(-30, 0),
            vec(30, 0),
            thickness=thickness,
            color=WHITE))
    v.add(Line3D(
            vec(0, ymin),
            vec(0, 100),
            thickness=thickness,
            color=WHITE))

    return v


def fake_curve():
    """
    Create a version of the elliptic curve y^2 = x^3-4x+1
    in the fake number plane where (0:1:0) is at (0,100)
    Calculations done in notebook
    """
    def f(x, y):
        return 2500*x**3 - x*y**2 + 1843/80*y**3 + 200*x*y - 9213/4*y**2 - 10000*x - 75*y + 2500

    v = ImplicitFunction(f, x_range=[-15, 15], y_range=[-10, 99], color=YELLOW, stroke_width=6)
    # v.add_points_as_corners(vec(0,100))
    # v.append_points([v.points[-1], v.points[-1], vec(0,100), vec(0,100)])
    # print(v.points[-1], len(v.points))
    v.add_line_to(vec(0, 100))
    # print(v.points[-20:])

    # w = VGroup([v])
    # w.add(Line3D(v.points[-100],vec(0,100), color=RED, stroke_width=6))
    return v



class Horizon3cWithoutText(ThreeDScene):

    def construct(self):
        numberplane_for_3d = fake_numberplane()
        shz(numberplane_for_3d, 1)
        self.add(numberplane_for_3d)
        projective_curve = fake_curve()
        shz(projective_curve, +2)
        self.add(projective_curve)

        point_colour = BLUE_B
        point_radius = .08
        point_z_index = 3
        P01 = dot_on_curve(vec(0, -1))
        P02 = dot_on_curve(vec(0, 1))
        P11 = dot_on_curve(vec(2, 1, .1))
        P12 = dot_on_curve(vec(2, -1, .1))
        P21 = dot_on_curve(vec(-1, 2, .05))
        P22 = dot_on_curve(vec(-1, -2, .1))
        P31 = dot_on_curve(vec(-2, 1, .1))
        P32 = dot_on_curve(vec(-2, -1, .1))
        P41 = dot_on_curve(vec(.25, .125, .1))
        P42 = dot_on_curve(vec(.25, -.125, .1))
        P51 = dot_on_curve(vec(-7. / 4, 13. / 8, .1))
        P52 = dot_on_curve(vec(-7. / 4, -13 / 8., .1))

        x_numerator = 6250080
        x_denominator = 33884041
        y_numerator = 102194916251
        y_denominator = 197239002661
        P61 = dot_on_curve(vec(x_numerator * 1. / x_denominator, y_numerator * 1. / y_denominator, .1))
        P62 = dot_on_curve(vec(x_numerator * 1. / x_denominator, -y_numerator * 1. / y_denominator, .1))

        # transform points to the 3d picture in fake coordinates
        for P in [P01, P02, P11, P12, P21, P22, P31, P32, P41, P42, P51, P52, P61, P62]:
            xP = P.get_center()[0]
            yP = P.get_center()[1]
            this_pt = dot_on_3dcurve(vec(96 * xP / (96 + yP), 100 * yP / (96 + yP), 0.03),
                                     point_colour,
                                     point_radius)
            #shz(this_pt, point_z_index)
            self.add(this_pt)

        # point at infinity
        pt_at_inf = dot_on_3dcurve(vec(0, 95, .1), radius=.45, colour=YELLOW)
        #shz(pt_at_inf, point_z_index)

        #text_at_inf = MathTex(r"(X=0,\,Y=1,\,Z=0)")
        #text_at_inf.rotate(PI / 2, axis=RIGHT)
        #text_at_inf.move_to(vec(1, 1, 6))

        #arrow_at_inf = Arrow3D(vec(1, 1, 5.5), vec(.1, 1, 4.1), color=WHITE)
        #pointing_at_inf = VGroup(text_at_inf, arrow_at_inf)

        # timings for the 3d move
        total_time_of_camera_move = 16.
        time_it_stands_still = 4.
        time_to_increase = 0.5

        t = ValueTracker(0)

        def onf(tt):
            if tt < (total_time_of_camera_move - time_it_stands_still) / 2:
                return 0
            elif tt < (total_time_of_camera_move - time_it_stands_still) / 2 + time_to_increase:
                ss = tt - (total_time_of_camera_move - time_it_stands_still) / 2
                ss *= 1 / time_to_increase
                return ss ** 2 * (2 - ss)
            elif tt < (time_it_stands_still + total_time_of_camera_move) / 2 - time_to_increase:
                return 1
            elif tt < (time_it_stands_still + total_time_of_camera_move) / 2:
                ss = (time_it_stands_still + total_time_of_camera_move) / 2 - tt
                ss *= 1 / time_to_increase
                return ss ** 2 * (2 - ss)
            else:
                return 0

        #pointing_at_inf.add_updater(lambda m: m.set_opacity(onf(t.get_value())))
        #self.add(pointing_at_inf)

        my_there_and_back_with_pause = lambda tt: rate_functions.there_and_back_with_pause(tt,
                                                                                           pause_ratio=time_it_stands_still / total_time_of_camera_move)

        frame_centre = vec(0, -10, 5)

        self.play(t.animate.set_value(total_time_of_camera_move),
                  self.camera.phi_tracker.animate(rate_func=my_there_and_back_with_pause).set_value(PI / 2),
                  self.camera._frame_center.animate(rate_func=my_there_and_back_with_pause).move_to(frame_centre),
                  run_time=total_time_of_camera_move)
        # this is copied from ThreeDScene.move_camera. See there.
        self.remove(self.camera._frame_center)

        self.wait(1)

# now render it
if __name__ == "__main__":
    config.renderer = "cairo"
    config.format = "mp4"
    #config.transparent = True
    #config.write_to_movie = False
    config.preview = True

    # Optional but recommended
    config.background_color = BLACK

    scene = Horizon3cWithoutText()
    scene.render()
