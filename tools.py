r"""
Part of the bsd_video

Common commands for useful for all parts

"""

from manim import *


def vec(x,y):
    return np.array([x, y, 0])


def subtitle(said):
    r"""
    This prints a text in small white at the bottom of the screen.
    """
    vt = Text(said, font_size=15, color="white", font="sans-serif")

    # Create a black rectangle with size matching the text
    background_box = Rectangle(
        width = vt.width + 0.1,  # Add some padding around the text
        height = vt.height + 0.1,  # Add some padding around the text
        color = BLACK
    )
    background_box.set_fill(BLACK, opacity=1)  # Set the fill color to black

    # add them together and shift to bottom of screen
    v = VGroup()
    v.add(background_box)
    v.add(vt)
    v.to_edge(DOWN)
    v.set_z_index(1)  # a bit in the foreground
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
    gradient_rect.set_z_index(0)
    return gradient_rect


def nature_background():
    r"""
    Background picture for opening scene.

    This is a placeholder
    """
    bg_image = ImageMobject("pics/path.jpg")
    bg_image.scale_to_fit_height(config.frame_height)
    bg_image.scale_to_fit_width(config.frame_width)
    bg_image.move_to(ORIGIN)
    bg_image.set_z_index(-10)
    return bg_image


def thought_bubble(text):
    r"""
    A cloud shape together with little dots below.
    """
    bubble = SVGMobject("pics/cloud.svg",
                        color=WHITE,
                        stroke_width=8
                        )
    bubble.scale(1.5)
    bubble.set_fill([rgb_to_color([0.0, 0.0, 0.3]), BLACK], opacity=1)
    bubble.shift(UP)

    c = Circle(radius=0.1,
               color=WHITE,
               stroke_width=8,
               fill_opacity=1,
               fill_color=BLACK
               )
    trail = VGroup(c.copy().scale(2), c.copy().scale(1.5), c)
    trail.arrange(DOWN).next_to(bubble, DOWN, buff=0.5)

    # Add text inside the bubble
    thought_text = MathTex(text, font_size=36)
    thought_text.move_to(bubble.get_center())

    # Combine all parts
    return VGroup(bubble, trail, thought_text)


def fading_line(y, stroke_width=4, **kwargs):
    """
    helper for my_fading_number_plane
    """
    v = VGroup()
    start = vec(-7.112, y)
    end = vec(7.112, y)
    num_segments = 50  # More segments = smoother fade
    le = (end - start)/num_segments

    for i in range(num_segments):
        if i < num_segments/2:
            opacity = 2*i/num_segments  # Fade out to the right
        else:
            opacity = 1
        segment = Line(i*le+start, (i+1)*le+start, stroke_opacity=opacity, stroke_width=stroke_width, **kwargs)
        v.add(segment)
    return v


def my_fading_numberplane():
    r"""
    A version of NumberPlane, where the lines fade out to the left
    currently not much can be configured as it is used in one form only
    """
    v = VGroup()
    for i in [-3,-2,-1,1,2,3]:
        li = fading_line(i, stroke_width=2, color=GRAY)
        v.add(li)
    ax = fading_line(0, stroke_width=2, color=WHITE)
    v.add(ax)
    for i in [1,2,3,4,5,6,7]:
        li = Line(vec(i,-4), vec(i,4), stroke_width=2, color=GRAY)
        v.add(li)
    for i in [1, 2, 3, 4, 5, 6, 7]:
        li = Line(vec(-i, -4), vec(-i, 4), stroke_opacity=(7-i)/7, stroke_width=2, color=GRAY)
        v.add(li)
    ay = Line(vec(0, -4), vec(0,4), stroke_width=2, color=WHITE)
    v.add(ay)
    return v


class TestSome(Scene):
    """
    A placeholder character for the student

    Example how to use the above class
    """
    def construct(self):

        self.add(my_fading_numberplane())
        self.wait(2)


if __name__ == "__main__":
    with tempconfig({"quality": "medium_quality", "preview": True}):
        scene = TestSome()
        scene.render()