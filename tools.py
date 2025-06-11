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
