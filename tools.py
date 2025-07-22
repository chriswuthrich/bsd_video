r"""
Part of the bsd_video

Common commands
useful for all parts

"""

from manim import *
from msage import smanim
import sage.all as sagemath


def vec(x, y, z=0):
    """
    short cur for numpy's array for 2-dimensional vectors
    """
    return np.array([x, y, z])


def shz(m, z: float):
    r"""
    To arrange objects in z-levels
    (since in opengl the set_z_level doesn't work).
    We expect z to be integers between -100 and 100,
    this shifts by z/100
    Typically the background will be -10 and the most forefront +10
    """
    # This is the version for opengl
    # return m.shift(np.array([0, 0, z/100]))
    return m.set_z_index(z)


# not used
def subtitle(said):
    r"""
    This prints a text in small white at the bottom of the screen.
    """
    vt = Text(said, font_size=15, color="white", font="sans-serif")

    # Create a black rectangle with size matching the text
    background_box = Rectangle(
        width=vt.width + 0.1,  # Add some padding around the text
        height=vt.height + 0.1,  # Add some padding around the text
        color=BLACK
    )
    background_box.set_fill(BLACK, opacity=1)  # Set the fill colour to black

    # add them together and shift to bottom of screen
    v = VGroup()
    v.add(background_box)
    v.add(vt)
    v.to_edge(DOWN)
    shz(v, 10)
    return v


def natural_initial_background():
    r"""
    Background picture for the opening scene.

    This is a placeholder.
    """
    bg_image = ImageMobject("pics/path.jpg")
    bg_image.scale_to_fit_height(config.frame_height)
    bg_image.scale_to_fit_width(config.frame_width)
    bg_image.move_to(ORIGIN)
    shz(bg_image, -10)
    return bg_image


# TODO decide if BLACK on right or left
def thought_bubble(centre, size=1.):
    r"""
    A cloud shape together with little dots below.
    Text is given to MathTex so its raw TeX.
    """
    bubble = SVGMobject("pics/cloud.svg",
                        color=WHITE,
                        stroke_width=8
                        )
    bubble.scale(1.5*size)
    bubble.set_fill([rgb_to_color([0.0, 0.0, 0.5]), BLACK], opacity=1)
    bubble.shift(centre)

    c = Circle(radius=0.08,
               color=WHITE,
               stroke_width=8,
               fill_opacity=1,
               fill_color=BLACK
               )
    small_bubbles = VGroup(c.copy().scale(2), c.copy().scale(1.5), c)
    small_bubbles.arrange(DOWN).next_to(bubble, DOWN, buff=0.3)
    v = VGroup(bubble, small_bubbles)
    return v


def cloud_background():
    r"""
    This creates the bubble as it is at the end of its
    scaling in # 1.1
    """
    return thought_bubble(ORIGIN, size=7.48)


# can be deleted
def my_old_background():
    r"""
    A gradient background
    """
    gradient_rect = Rectangle(
        width=config.frame_height,
        height=config.frame_width,
        fill_opacity=1,
    )
    gradient_rect.set_fill(
        color=[rgb_to_color([0.0, 0.0, 0.3]), BLACK],
        opacity=1
    )
    gradient_rect.rotate(PI/2)
    shz(gradient_rect, -10)
    return gradient_rect


def fading_line(y, stroke_width=4, **kwargs):
    """
    helper for my_fading_number_plane
    """
    # eps = vec(0.005, 0) # to avoid overlap
    v = VGroup()
    start = vec(-7.112, y)
    end = vec(7.112, y)
    number_of_segments = 100
    length_of_segments = (end - start)/number_of_segments

    for i in range(number_of_segments):
        if i < number_of_segments/2:
            opacity = 2*i/number_of_segments  # Fade out to the left
        else:
            opacity = 1
        segment = Line(i * length_of_segments + start,
                       (i+1) * length_of_segments + start,
                       stroke_opacity=opacity,
                       stroke_width=stroke_width,
                       **kwargs)
        v.add(segment)
    return v


def fading_numberplane(x_tip=True,
                       y_tip=True,
                       x_label=False,
                       y_label=False,
                       axes_fading=True,
                       stroke_width=2):
    r"""
    A version of NumberPlane, where the lines fade out to the left.

    x_tip includes an arrow tip on the x-axis,
    y_tip for the y_axis

    x_label and y_label add "x" and "y" on it

    axes_fading = False means that the x and y axis
    are redrawn in white.
    """
    v = VGroup()

    # full line for x=i with i positive.
    for i in [1, 2, 3, 4, 5, 6, 7]:
        li = Line(vec(i, -4),
                  vec(i, 4),
                  stroke_width=stroke_width,
                  color=GRAY)
        v.add(li)

    # y-axis
    y_axis_colour = GRAY if axes_fading else WHITE
    y_axis = Line(vec(0, -4),
                  vec(0, 4),
                  color = y_axis_colour,
                  stroke_width=stroke_width)
    v.add(y_axis)

    if y_tip:
        y_arrow_tip = CurvyPointyTip(length=.35,
                                     stroke_width=stroke_width,
                                     color=y_axis_colour)
        y_arrow_tip.rotate(PI/2)
        y_arrow_tip.move_to(vec(0, 3.4))
        v.add(y_arrow_tip)

    if y_label:
        label_y = MathTex(r"y", color=y_axis_colour)
        label_y.scale(.8)
        label_y.move_to(vec(0.4, 3.5))
        v.add(label_y)

    # lines with less opacity for x=i with negative i
    for i in [1, 2, 3, 4, 5, 6, 7]:
        li = Line(vec(-i, -4),
                  vec(-i, 4),
                  stroke_opacity=(7 - i) / 7,
                  stroke_width=stroke_width,
                  color=GRAY)
        v.add(li)

    # lines y=i for non-zero i
    for i in [-3, -2, -1, 1, 2, 3]:
        li = fading_line(i, stroke_width=stroke_width, color=GRAY)
        v.add(li)

    # x-axis
    if axes_fading:
        x_axis = fading_line(0, stroke_width=stroke_width, color=WHITE)
    else:
        x_axis = Line(vec(-7, 0, .1),
                      vec(7, 0, .1),
                      color=WHITE,
                      stroke_width=2)
    v.add(x_axis)

    if x_tip:
        x_arrow_tip = CurvyPointyTip(length=.35,
                                     stroke_width=stroke_width,
                                     color=WHITE)
        x_arrow_tip.move_to(vec(6.4, 0))
        v.add(x_arrow_tip)

    if x_label:
        label_x = MathTex(r"x")
        label_x.scale(.8)
        label_x.move_to(vec(6.5, -0.4))
        v.add(label_x)

    shz(v,1)
    return v

# not used
def glow_dot(centre, radius=0.035, glow_radius=0.2, glow_opacity=0.3, colour=YELLOW, **kwargs):
    v = VGroup()
    dot = Dot(point=centre, radius=radius, color=colour, **kwargs)
    v.add(dot)
    nu = 10
    for i in range(nu):
        glow = Circle(radius=i*glow_radius/nu,
                      color=colour,
                      fill_opacity=(nu-i)*glow_opacity/nu,
                      stroke_opacity=0
                      )
        glow.move_to(centre)
        v.add(glow)
    return v


class MySurroundingRectangle(RoundedRectangle):
    r"""
    untyped version
    """

    def __init__(
        self,
        *mobjects,
        color,
        buff,
        corner_radius = 0.0,
        **kwargs
    ) -> None:
        from manim.mobject.mobject import Group

        # this is the text commented out to avoid opengl problems
        # if not all(isinstance(mob, Mobject) or for mob in mobjects):
        #     raise TypeError("Expected all inputs for parameter mobjects to be a Mobjects")

        group = Group(*mobjects)
        super().__init__(
            color=color,
            width=group.width + 2 * buff,
            height=group.height + 2 * buff,
            corner_radius=corner_radius,
            **kwargs,
        )
        self.buff = buff
        self.move_to(group)

# to be deleted
class OldCurvyPointyTip(ArrowTip):
    r"""
    My class for a tip that has inwards curved sides

    It is not very neat and produces random errors

    side_angle : Is the angle between the base and the tangent of the curve to the tip
    pointiness>0 : determines how pointy the tip is
                   The higher the value the pointier.
    """

    def __init__(
        self,
        fill_opacity: float = 1,
        stroke_width: float = 3,
        length: float = DEFAULT_ARROW_TIP_LENGTH,
        width: float = DEFAULT_ARROW_TIP_LENGTH*.8,
        start_angle: float = PI,
        side_angle: float = PI/4,
        pointiness: float = 2,
        **kwargs
    ):
        self.start_angle = start_angle  # doesn't seem to change anything

        tip = vec(length,0)
        upper_corner = vec(0, width/2)
        lower_corner = vec(0, -width/2)

        # Control points to curve the left and right sides inwards
        cp1 = vec(length/pointiness,0)
        cp2 = upper_corner + length/3 * vec(np.sin(side_angle), -np.cos(side_angle))
        cp3 = lower_corner + length/3 * vec(np.sin(side_angle), np.cos(side_angle))
        cp4 = vec(length/pointiness, 0)

        # OpenGLVMobject.__init__(
        #     self, fill_opacity=fill_opacity, stroke_width=stroke_width, **kwargs
        # )
        VMobject.__init__(
            self, fill_opacity=fill_opacity, stroke_width=stroke_width, **kwargs
        )

        self.start_new_path(tip)
        self.add_cubic_bezier_curve_to(cp1, cp2, upper_corner)
        self.add_cubic_bezier_curve_to(upper_corner, lower_corner, lower_corner)
        self.add_cubic_bezier_curve_to(cp3, cp4, tip)
        self.scale(length / self.length)


def standard_curve():
    """
    Draws the standard example of an elliptic curve
    It has rank 2
    """
    E = sagemath.EllipticCurve([-4, 1])
    curve = smanim(E.plot(color="yellow", thickness=2, alpha=0.3, xmax=7, ymin=-5, ymax=5))
    shz(curve, 5)
    return curve


class CurvyPointyTip(ArrowTip):
    r"""
    My class for a tip that has inwards curved sides

    It is not very neat and produces random errors
    """

    def __init__(
        self,
        fill_opacity: float = 1,
        stroke_width: float = 3,
        length: float = DEFAULT_ARROW_TIP_LENGTH,
        width: float = DEFAULT_ARROW_TIP_LENGTH*.8,
        start_angle: float = PI,
        side_angle: float = PI/4,
        **kwargs
    ):
        self.start_angle = start_angle  # doesn't seem to change anything

        tip = vec(length,0)
        upper_corner = vec(0, width/2)
        lower_corner = vec(0, -width/2)

        # Control points to curve the left and right sides inwards
        cp1 = vec(length,0)
        cp2 = upper_corner + length/3 * vec(np.sin(side_angle), -np.cos(side_angle))
        cp3 = lower_corner + length/3 * vec(np.sin(side_angle), np.cos(side_angle))
        cp4 = vec(length, 0)

        # OpenGLVMobject.__init__(
        #     self, fill_opacity=fill_opacity, stroke_width=stroke_width, **kwargs
        # )
        VMobject.__init__(
            self, fill_opacity=fill_opacity, stroke_width=stroke_width, **kwargs
        )
        self.start_new_path(tip)
        self.add_cubic_bezier_curve_to(cp1, cp2, upper_corner)
        self.add_cubic_bezier_curve_to(cp2, cp3, lower_corner)
        self.add_cubic_bezier_curve_to(cp3, cp4, tip)
        self.scale(length / self.length)


class TestSome(Scene):
    """
    A placeholder character for the student

    Example how to use the above class
    """
    def construct(self):

        self.add(fading_numberplane(y_tip=True, x_label=True))
        self.wait(.2)
        dot = glow_dot(centre=vec(.3, .5))
        self.add(dot)
        self.wait(.2)
        t = ValueTracker(0)
        dot.add_updater(lambda m: m.move_to(vec(t.get_value(), t.get_value() ** 3)))
        self.play(t.animate.set_value(1), run_time=1)
        self.wait(2)

        w = Arrow(start=vec(1,1), end=vec(2,3), tip_shape=OldCurvyPointyTip, buff =0)
        w2 = Arrow(start=vec(-5, 0), end=vec(-3, 0), tip_shape=CurvyPointyTip)
        w3 = Arrow(start=vec(-4, -3), end=vec(-4, 3))
        w5 = Arrow(start=vec(-1, -1.3), end=vec(-5, -1.3), tip_shape=OldCurvyPointyTip)
        w6 = Arrow(start=vec(-1, -1), end=vec(0, 0), tip_shape=CurvyPointyTip)
        self.add(w, w2, w3, w5, w6)
        self.wait()
        self.clear()
        for j in range(-12,12):
            i = j/4
            self.play(FadeIn(Arrow(vec(-5, i), vec(i,4*i/3), tip_shape=CurvyPointyTip, buff =0)))
        self.wait(1)
        self.clear()
        self.add(cloud_background())
        self.wait()


        self.add(thought_bubble(ORIGIN, 1.3))
        # self.add(Arrow(tip_shape=CurvyPointyTip))
        self.wait()

if __name__ == "__main__":
    with tempconfig({"renderer": "cairo",  "quality": "medium_quality", "preview": True}):
        scene = TestSome()
        scene.render()
