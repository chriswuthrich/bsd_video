from manim import *

class ManimLogo(Scene):
    def construct(self):
        banner = ManimBanner()
        self.play(banner.create())
        self.play(banner.expand())
        self.wait()
        self.play(Unwrite(banner))

# now render it
if __name__ == "__main__":
    config.renderer = "cairo"
    config.format = "png"
    config.transparent = True
    config.write_to_movie = False
    # config.preview = True

    # Optional but recommended
    config.background_color = None

    scene = ManimLogo()
    scene.render()
