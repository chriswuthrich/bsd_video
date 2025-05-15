from manim import *

class StudentChar(VGroup):
    """
        This creates a little character that is a placeholder for the student figure
        height and width measure the bottom rectangular body part
    """

    def __init__(self, height=1, width=1, centre=np.array([0.,0.,0.]), lid_colour=RED):

        super().__init__()

        h = height/2
        w = width/2
        self._lid_colour = lid_colour

        # body
        left_side = Line(UP*h+LEFT*w, DOWN*h+LEFT*w)
        bottom_side = Line(DOWN*h+LEFT*w, DOWN*h+RIGHT*w)
        right_side = Line(DOWN*h+RIGHT*w, UP*h+RIGHT*w)
        self.add(left_side, bottom_side, right_side)
        self.set_stroke(WHITE, width=2)

        body = Rectangle(height=2 * h, width=2 * w)
        body.set_fill(BLUE, opacity=1)
        body.set_stroke(width=0)  # No border
        body.set_fill(BLUE, opacity=0.7)
        self.add(body)

        # head
        head = Arc(radius=w, start_angle=0, angle=PI)
        head.shift(UP * h)
        head.set_fill(BLUE, opacity=0.7)
        head.set_stroke(WHITE, width=2)
        self.add(head)

        # eyes
        left_eye = Circle(w/3)
        left_eye.shift(h*UP+w/2*LEFT)
        left_eye.set_fill(WHITE, opacity=0.9)
        left_eye.set_stroke(WHITE, width=1)
        right_eye = Circle(w / 3)
        right_eye.shift(h * UP + w / 2 * RIGHT)
        right_eye.set_fill(WHITE, opacity=0.9)
        right_eye.set_stroke(WHITE, width=1)
        left_eye_centre = Dot(h*UP+w/2*LEFT, radius=w/10, color=BLACK)
        right_eye_centre = Dot(h*UP+w/2*RIGHT, radius=w/10, color=BLACK)
        self.add(left_eye)
        self.add(right_eye)
        self.add(left_eye_centre)
        self.add(right_eye_centre)

        # these should stay in order
        # smile -5
        smile = Arc(w/3,-PI/6,-2*PI/3)
        smile.shift(h*UP+w/3*DOWN)
        smile.set_stroke(WHITE, opacity=0.9)
        self.add(smile)

        # non smile mouth -4
        mouth = Line(h*UP+2*w/3*DOWN+w/3*LEFT, h*UP+2*w/3*DOWN+w/3*RIGHT)
        mouth.set_stroke(WHITE, opacity=0)  # invisible
        self.add(mouth)

        # sad face -3
        # sad = Arc(w/3, PI/6, 2*PI/3,color=BLACK)  # doesn't work fills arc??
        sad = Arc(w/3,-PI/6,-2*PI/3)
        sad.flip(RIGHT)
        sad.shift(h*UP+5*w/6*DOWN)
        sad.set_stroke(WHITE, opacity=0)
        sad.set_fill(WHITE, opacity=0)
        self.add(sad)

        # lids -1 right -2 left
        left_lid = Arc(w/3,0,PI)
        left_lid.shift(h*UP+w/2*LEFT)
        left_lid.set_fill(lid_colour, opacity=0)  # invisible at this stage
        left_lid.set_stroke(WHITE,0)
        right_lid = Arc(w/3,0,PI)
        right_lid.shift(h*UP+w/2*RIGHT)
        right_lid.set_fill(lid_colour, opacity=0)
        right_lid.set_stroke(WHITE,0)
        self.add(left_lid)
        self.add(right_lid)

        # place at the right spot
        self.shift(centre)


    def half_close_left_eye(self):
        self[-2].set_fill(self._lid_colour, opacity=0.95)

    def half_close_right_eye(self):
        self[-1].set_fill(self._lid_colour, opacity=0.95)

    def open_left_eye(self):
        self[-2].set_fill(self._lid_colour, opacity=0)

    def open_right_eye(self):
        self[-1].set_fill(self._lid_colour, opacity=0)

    def smile(self):
        self[-3].set_opacity(0)
        self[-4].set_opacity(0)
        self[-5].set_opacity(1)

    def sad(self):
        self[-3].set_opacity(1)
        self[-4].set_opacity(0)
        self[-5].set_opacity(0)

    def dull(self):
        self[-3].set_opacity(0)
        self[-4].set_opacity(1)
        self[-5].set_opacity(0)

    def no_mouth(self):
        self[-3].set_opacity(0)
        self[-4].set_opacity(0)
        self[-5].set_opacity(0)


class MyChar(Scene):
    """
    A placeholder character for the student

    Example how to use the above class
    """
    def construct(self):

        student = StudentChar()
        student.dull()
        # Show it
        self.play(Create(student))
        self.wait(.2)

        # blink left eye
        student.half_close_left_eye()
        self.wait(1)
        student.open_left_eye()
        self.wait(.2)

        # sad
        student.sad()
        self.wait(0.2)

        # more figures of different sizes
        st2 = StudentChar(.5,.5,2*UP, GREEN)
        st2.half_close_right_eye()
        st3 = StudentChar(1.5,.5,3*RIGHT)
        st3.dull()
        st4 = StudentChar(1,1, 2*LEFT)
        self.add(st2, st3, st4)
        self.wait(1)
        self.play(Rotate(st4,PI/4, run_time=1))


with tempconfig({"quality": "medium_quality", "preview": True}):
    scene = MyChar()
    scene.render()