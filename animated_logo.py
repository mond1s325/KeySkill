from manim import *
import numpy as np

class Logo(Scene):
    def construct(self):
        text = Text("KeySkill", font_size=72, color=WHITE)
        self.play(
                Write(text,run_time=3)
            ) 
        