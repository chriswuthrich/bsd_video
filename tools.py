r"""
Part of the bsd_video

Common commands for useful for all parts

"""

from manim import *
from manim.opengl import *

def vec(x: float, y: float, z=0):
    return np.array([x, y, z])


def shz(m, z: float):
    r"""
    To arrange object in z-levels
    (since in opengl the set_z_level doesn't work)
    We expect z to be integers between -100 and 100,
    this shifts by z/100
    Typically the background will be -10 and the most forefront +10
    """
    return m.shift(np.array([0, 0, z/100]))


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
    background_box.set_fill(BLACK, opacity=1)  # Set the fill color to black

    # add them together and shift to bottom of screen
    v = VGroup()
    v.add(background_box)
    v.add(vt)
    v.to_edge(DOWN)
    shz(v, 10)
    return v


def my_background():
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


def nature_background():
    r"""
    Background picture for opening scene.

    This is a placeholder
    """
    bg_image = OpenGLImageMobject("pics/path.jpg")
    bg_image.scale_to_fit_height(config.frame_height)
    bg_image.scale_to_fit_width(config.frame_width)
    bg_image.move_to(ORIGIN)
    shz(bg_image, -10)
    return bg_image


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
    bubble.set_fill([rgb_to_color([0.0, 0.0, 0.3]), BLACK], opacity=1)
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


def fading_line(y, stroke_width=4, **kwargs):
    """
    helper for my_fading_number_plane
    """
    eps = vec(0.005, 0) # to avoid overlap
    v = VGroup()
    start = vec(-7.112, y)
    end = vec(7.112, y)
    num_segments = 100  # More segments = smoother fade
    le = (end - start)/num_segments

    for i in range(num_segments):
        if i < num_segments/2:
            opacity = 2*i/num_segments  # Fade out to the left
        else:
            opacity = 1
        segment = Line(i*le+start,
                       (i+1)*le+start-eps,
                       stroke_opacity=opacity,
                       stroke_width=stroke_width,
                       **kwargs)
        v.add(segment)
    return v


def my_fading_numberplane(stroke_width=2):
    r"""
    A version of NumberPlane, where the lines fade out to the left
    currently not much can be configured as it is used in one form only
    """
    v = VGroup()
    for i in [1, 2, 3, 4, 5, 6, 7]:
        li = Line(vec(i, -4), vec(i, 4), stroke_width=stroke_width, color=GRAY)
        v.add(li)
    ax = fading_line(0, stroke_width=stroke_width, color=WHITE)
    v.add(ax)
    for i in [1, 2, 3, 4, 5, 6, 7]:
        li = Line(vec(-i, -4), vec(-i, 4), stroke_opacity=(7 - i) / 7, stroke_width=stroke_width, color=GRAY)
        v.add(li)
    ay = Line(vec(0, -4), vec(0, 4), stroke_width=stroke_width, color=WHITE)
    v.add(ay)


    for i in [-3, -2, -1, 1, 2, 3]:
        li = fading_line(i, stroke_width=stroke_width, color=GRAY)
        v.add(li)
    return v


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

        # if not all(isinstance(mob, Mobject) or for mob in mobjects):
        #     raise TypeError(
        #         "Expected all inputs for parameter mobjects to be a Mobjects"
        #     )

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

#
#
# class CurvyPointyTip(ArrowTip):
#     def __init__(
#         self,
#         fill_opacity: float = 1,
#         stroke_width: float = 3,
#         length: float = DEFAULT_ARROW_TIP_LENGTH / 2,
#         start_angle: float = PI,
#         **kwargs: Any,
#     ):
#         self.start_angle = start_angle
#         VMobject.__init__(
#             self, fill_opacity=fill_opacity, stroke_width=stroke_width, **kwargs
#         )
#
#         self.set_points_as_corners(
#             np.array(
#                 [
#                     [2, 0, 0],  # tip
#                     [-1.2, 1.6, 0],
#                     [0, 0, 0],  # base
#                     [-1.2, -1.6, 0],
#                     [2, 0, 0],  # close path, back to tip
#                 ]
#             )
#         )
#         self.scale(length / self.length)
#     self.width = length
#         path = [
#           UP * length,
#           ORIGIN,
#           DOWN * length,
#         ]
#         self.set_points_smoothly(path)



class TestSome(Scene):
    """
    A placeholder character for the student

    Example how to use the above class
    """
    def construct(self):

        self.clear()
        self.add(my_background())
        self.wait()

        self.add(my_fading_numberplane())
        self.wait(.2)
        dot = glow_dot(centre=vec(.3, .5))
        self.add(dot)
        self.wait(.2)
        t = ValueTracker(0)
        dot.add_updater(lambda m: m.move_to(vec(t.get_value(), t.get_value()**3)))
        self.play(t.animate.set_value(1), run_time=1)
        self.wait(2)

        self.add(thought_bubble(ORIGIN, 1.3))
        # self.add(Arrow(tip_shape=CurvyPointyTip))
        self.wait()

if __name__ == "__main__":
    with tempconfig({"renderer": "opengl",  "quality": "medium_quality", "preview": True}):
        scene = TestSome()
        scene.render()
