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

    def pt_with_label(self, R, dir=UR):
        """
        plot a point at R and label it with the rational coordinates
        dir is the direction in which the label is off the dot
        """
        sc = 0.3  # how much distance between them
        v = Sphere(center = np.array([R[0],R[1],0]), radius=0.1, color=WHITE)
        # a = R[0].numerator()
        # b = R[0].denominator()
        # c = R[1].numerator()
        # d = R[1].denominator()
        # lastr = r"\bigl(\frac{" + str(a) + "}{" + str(b) + r"},\,\frac{" + str(c) + "}{" + str(d) + "}"
        lastr = r"\bigl(" + R[0]._latex_() + "," + R[1]._latex_() + r"\bigr)"
        print(lastr)
        la = MathTex(lastr, color=YELLOW_A)
        la.scale(.5)
        la.move_to(np.array([R[0],R[1],0.])+sc*dir)
        return v, la

    def construct(self):

        E, EQ = self.calc_curve()
        # phi = 0 from above theta = -90 gives 2d view
        # self.camera.frame.move_to((0,0,5))
        self.set_camera_orientation(phi=0, theta=-PI/2, frame_center=(0,0,5), distance=5)

        nu = NumberPlane(x_range=[-100,100,1],y_range=[-10,50,1])
        self.add(nu)
        self.add(smanim(E.plot(xmin=-3, xmax=100, ymin=-100, ymax=100, color="yellow")))

        for R in EQ[:5]:
            v, la = self.pt_with_label(R)
            self.add(v, la)
            self.wait(1)
            self.remove(la)

        pts_in_pic = []
        vpts = VGroup()
        for R in EQ:
        #    if R[0].abs() < 7.111 and R[1].abs() < 4:
                rr = np.array([R[0],R[1],0.])
                pts_in_pic.append(rr)
                vpts.add(Sphere(center=rr, radius=0.1, color=YELLOW_A))

        self.add(vpts)
        self.wait(2)

        self.move_camera(phi=0.45*PI/2, frame_center=(0, -5, 5))
        self.remove(nu)
        nu = NumberPlane(x_range=[-100,100,2],y_range=[-10,100,2])
        self.add(nu)
        self.move_camera(phi=0.9*PI/2, frame_center=(0, -10, 5))

        self.wait(1)
        self.play(Uncreate(vpts))
        self.wait(2)


        #

# now render it
if __name__ == "__main__":
    with tempconfig({"quality": "medium_quality", "preview": True}):
        scene = SecondScene()
        scene.render()
