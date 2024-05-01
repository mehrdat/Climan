from manim import *
import matplotlib
from manim import *
from manim import Scene, Circle
from manim import *


from manim import *

class RotatingEarth3D(ThreeDScene):
    """ 
    creates an earth 3d rotating and some layers of atmospee around it
    """
    def construct(self):
        """ """
        # Set up the camera
        self.set_camera_orientation(phi=75 * DEGREES)#, theta=30 * DEGREES)

        # Create a textured sphere
        earth = Sphere(resolution=(101, 51))
        earth.set_texture("earth_texture.png")
        earth.scale(2)  # Adjust the size as needed

        # Create the animation
        self.add(earth)
        self.begin_ambient_camera_rotation(rate=0.8)  # Slowly rotate the camera around the scene

        # Play the rotation animation
        self.play(Rotate(earth, angle=2*PI, axis=UP, run_time=8, rate_func=linear))

        # Keep the scene
        self.wait(2)

# To render the video, use the following command in your terminal:
# manim -pql rotating_earth_3d.py RotatingEarth3D


# class RotatingEarth(Scene):
#     def construct(self):
#         # Load the image of Earth
#         earth = ImageMobject("earth.png")
#         earth.scale(1)  # Adjust size as needed

#         # Create the animation
#         self.add(earth)
#         self.play(Rotate(earth, angle=2*PI, run_time=8, rate_func=linear))

#         # Keep the image on screen after animation
#         self.wait(3)

# To render the video, use the following command in your terminal:
# manim -pql rotating_earth.py RotatingEarth
