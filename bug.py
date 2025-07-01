from manim import *

class IsItABug(ThreeDScene):

    def construct(self):
        self.set_camera_orientation(phi=0, theta=-PI/2, frame_center=(0,0,5))
        L = Line([1,-10,0],[2,100,0])
        C = Circle()
        N = NumberPlane(x_range=[-100,100,1], y_range=[-100,100,1])
        self.add(L, C, N)
        self.wait(1)
        self.move_camera(phi=0.9*PI/2, frame_center=(0, -10, 5), run_time=3)
        self.wait(1)

class AnotherScene(ThreeDScene):

    def construct(self):
        self.set_camera_orientation(phi=0, theta=-PI/2, frame_center=(0,0,5))
        L = Line3D([0,-10,0],[0,10000,0], color=WHITE)
        L2 = Line3D([-100,0,0], [100,0,0], color=WHITE)
        L3 = Line3D([1,-10,0],[1,10000,0], color=TEAL)
        L4 = Line3D([-100,1,0], [100,1,0], color=TEAL)
        f = lambda t : np.array([t**2,t**3,0])
        C = ParametricFunction(f,[0,100])
        self.add(L, L2, L3, L4, C)
        self.wait(1)
        self.move_camera(phi=0.9*PI/2, frame_center=(0, -10, 5), run_time=3)
        self.wait(1)


# no bug, it does cache Flash
class IsThisNotCaching(Scene):
    def construct(self):
        self.add(Circle())
        self.wait()
        d = Dot()
        self.add(d)
        self.play(Flash(ORIGIN))
        self.wait()


if __name__ == "__main__":
    with tempconfig({"quality": "medium_quality", "preview": True}):
        scene = IsThisNotCaching()
        scene.render()