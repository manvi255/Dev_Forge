from manim import *

class AutoScene(Scene):
    def construct(self):
        # Step 1: Draw a circle on the screen
        circle = Circle(radius=2, color=BLUE)
        self.play(Create(circle))

        # Step 2: Highlight and draw a line from the center of the circle to its edge (radius)
        radius_line = Line(start=[0, 0, 0], end=[2, 0, 0], color=YELLOW)
        self.play(Create(radius_line))

        # Step 3: Label the radius
        radius_label = MathTex("r", color=YELLOW).next_to(radius_line, RIGHT)
        self.play(Write(radius_label))

        # Step 4: Draw a line from one edge of the circle to the opposite edge (diameter)
        diameter_line = Line(start=[-2, 0, 0], end=[2, 0, 0], color=GREEN)
        self.play(Create(diameter_line))

        # Step 5: Label the diameter
        diameter_label = MathTex("2r", color=GREEN).next_to(diameter_line, RIGHT)
        self.play(Write(diameter_label))

        # Step 6: Highlight the difference between the radius and diameter
        radius_circle = Circle(radius=0.15, color=YELLOW).move_to([2, 0, 0])
        diameter_circle = Circle(radius=0.15, color=GREEN).move_to([-2, 0, 0])
        self.play(Create(radius_circle), Create(diameter_circle))

        # Emphasizing the relationship
        self.play(radius_circle.animate.set_fill(opacity=0.5), diameter_circle.animate.set_fill(opacity=0.5))
        self.wait(2)