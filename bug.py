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


if __name__ == "__main__":
    with tempconfig({"quality": "medium_quality", "preview": True}):
        scene = IsItABug()
        scene.render()