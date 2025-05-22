from manim import *
from sage.all import *
from character import StudentChar
from msage import smanim
from first_scene import subtitle


class SecondScene(ThreeDScene):

    def calc_curve(self):

        # Do the sage calculations to
        # get the curve and its rational points EQ
        E = EllipticCurve([-4, 1])

        P, Q = E.gens()
        EQ = []
        for n in [-3, -2, -1, 0, 1, 2, 3]:
            for m in range(-13, 13):
                R = n * P + m * Q
                if R != 0:
                    EQ.append(R)
        EQ.sort(key=lambda R: R.height())

        return E, EQ

    def my_latex(self, R):
        """
        Return the latexed version of a
        rational point
        """
        xx = R[0]
        yy = R[1]
        return r"\bigl(" + xx._latex_() + "," + yy._latex_() + r"\bigr)"

    def pt_with_label(self, R, dir=UR):
        """
        plot a point at R and label it with the rational coordinates
        dir is the direction in which the label is off the dot
        """
        sc = 0.3  # how much distance between them
        v = Sphere(center = np.array([R[0],R[1],0]), radius=0.05, color=WHITE)
        lastr = self.my_latex(R)
        print(lastr)
        la = MathTex(lastr, color=YELLOW_A)
        la.scale(.5)
        la.move_to(np.array([R[0],R[1],0.])+sc*dir)
        return v, la

    def my_numberplane(self,
                       x_range=np.array([-50, 50, 1]),
                       y_range=np.array([-10, 100, 1]),
                       colour=TEAL):
        """
        Version of NumberPlane used in 3D
        """
        v = VGroup()
        xx = x_range[0]
        yy = y_range[0]
        while xx < x_range[1]:
            v.add(Line3D(
                np.array([xx, y_range[0], 0]),
                np.array([xx, y_range[1], 0]),
                thickness=.002,
                color=colour))
            xx += x_range[2]
        while yy < y_range[1]:
            v.add(Line3D(
                np.array([x_range[0],yy,0]),
                np.array([x_range[1],yy,0]),
                thickness=.001,
                color=colour))
            yy += y_range[2]
        return v

    def construct(self):

        E, EQ = self.calc_curve()
        # phi = 0 from above theta = -90 gives 2d view
        # self.camera.frame.move_to((0,0,5))
        self.set_camera_orientation(phi=0, theta=-PI/2, frame_center=(0,0,5), distance=5)

        nu = self.my_numberplane()
        self.add(nu)
        self.add(smanim(E.plot(xmin=-3, xmax=100, ymin=-100, ymax=100, color="yellow")))

        for R in EQ[:5]:
            v, la = self.pt_with_label(R)
            self.add(v, la)
            self.wait(1)
            self.remove(la)

        pts_in_pic = []
        vpts = VGroup()
        for R in EQ[:30]:  ## do more but restrict better later
                rr = np.array([R[0],R[1],0.])
                pts_in_pic.append(rr)
                vpts.add(Dot(rr))  #Sphere(center=rr, radius=0.1, color=YELLOW_A))

        self.add(vpts)
        self.wait(2)

        self.move_camera(phi=0.45*PI/2, frame_center=(0, -5, 5))
        # self.remove(nu)
        # nu = NumberPlane(x_range=[-100,100,2],y_range=[-10,100,2])
        # self.add(nu)
        self.move_camera(phi=PI/2, frame_center=(0, -10, 5))

        self.wait(1)
        self.play(Uncreate(vpts))
        self.wait(2)


# now render it
if __name__ == "__main__":
    with tempconfig({"quality": "medium_quality", "preview": True}):
        scene = SecondScene()
        scene.render()
