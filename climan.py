from manim import *
import matplotlib
from manim import *

class EarthScene(ThreeDScene):
    def construct(self):
        earth = Sphere(radius=2, resolution=(50, 50))
        earth.set_fill(color=BLUE, opacity=1)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.play(ShowCreation(earth))
        self.wait()

earth_scene = EarthScene()
earth_scene.render()