from manimlib.constants import WHITE
from manimlib.mobject.geometry import Circle
from manimlib.mobject.svg.tex_mobject import Tex
from manimlib.mobject.types.vectorized_mobject import VMobject


MY_GREEN = "#419425"


class H2OLogo(VMobject):
    
    def __init__(self, surround_class=Circle, stroke_opacity=1.0):
        super().__init__()
        name = Tex("\\mathrm{H_2O}")
        surround = surround_class().set_stroke(WHITE, opacity=stroke_opacity).set_fill(MY_GREEN, opacity=1.0)
        self.add(surround, name)