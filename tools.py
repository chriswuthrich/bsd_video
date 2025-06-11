r"""
Part of the bsd_video

Common commands for useful for all parts

"""


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

