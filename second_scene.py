from manim import *
from sage.all import *
from character import StudentChar
from msage import smanim
from first_scene import subtitle


class FirstScene(Scene):

    def construct(self):

        E = EllipticCurve([-4, 1])

        P, Q = E.gens()
        EQ = []
        for n in [-3,-2,-1,0,1,2,3]:
            for m in range(-13,13):
                R = n*P+m*Q
                if R != 0:
                    EQ.append(R)
        EQ.sort(key= lambda R : R.height())

        pts_in_pic = []
        vpts = VGroup()
        for R in EQ:
            if R[0].abs() < 7.111 and R[1].abs() < 4:
                rr = np.array([R[0],R[1],0.])
                pts_in_pic.append(rr)
                vpts.add(Dot(rr))

        self.add(NumberPlane())
        self.add(smanim(E.plot(xmin=-7, xmax=7, ymin=-4, ymax=4, color="yellow")))
        self.add(vpts)
        self.wait(2)


        #

# now render it
if __name__ == "__main__":
    with tempconfig({"quality": "medium_quality", "preview": True}):
        scene = FirstScene()
        scene.render()
