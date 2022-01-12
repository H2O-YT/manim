from h2o.logo import H2OLogo
from manimlib.animation.creation import ShowCreation, Write
from manimlib.animation.transform import ReplacementTransform
from manimlib.constants import GREEN, ORANGE, PURPLE, RED
from manimlib.mobject.coordinate_systems import NumberPlane
from manimlib.mobject.mobject_update_utils import always_redraw
from manimlib.mobject.types.vectorized_mobject import VGroup
from manimlib.mobject.value_tracker import ValueTracker
from manimlib.scene.scene import Scene


class CalculusIntro(Scene):
    
    def construct(self):
        self.setup_axes_and_graph()
        self.setup_derivative_stuff()
        self.setup_integral_stuff()
        self.setup_logo()
        
    def setup_axes_and_graph(self):
        def function(x):
            return x*(x+1)*(x+2)*(x+3)
        self.ax = NumberPlane()
        self.graph = self.ax.get_graph(function, color = RED)
        self.play(Write(self.ax), run_time = 0.5)
        self.play(ShowCreation(self.graph), run_time = 0.5)
    
    def setup_derivative_stuff(self):
        dx_tracker = ValueTracker(2)
        secant_line = always_redraw(lambda: self.ax.get_tangent_line(
            x = -3.4, graph = self.graph, dx = dx_tracker.get_value(), color = GREEN
        ))
        self.play(ShowCreation(secant_line), run_time=0.5)
        self.play(dx_tracker.animate(run_time = 0.5).set_value(0.1))
    
    def setup_integral_stuff(self):
        areas = VGroup(*[self.ax.get_riemann_rectangles(
            self.graph, x_range=[-3, 0], dx=dx, colors=(PURPLE, ORANGE)
        ) for dx in [1, 0.5, 0.2, 0.1]])
        for index in range(len(areas)):
            if index == 0:
                self.play(Write(areas[index]), run_time=0.5)
            else:
                self.play(ReplacementTransform(areas[index-1], areas[index]), run_time=0.5)
    
    def setup_logo(self):
        logo = H2OLogo()
        self.play(Write(logo))
        self.wait()