from manim import *
from manim.equations import (
    ROOTS_OF_UNITY_TITLE,
    COMPLEX_PLANE_TITLE,
    PROPERTIES,
    EULER_FORMULA,
    DE_MOIVRE_FORMULA
)

class IntroductionScene(Scene):
    def construct(self):
        # Create title
        title = MathTex(ROOTS_OF_UNITY_TITLE)
        title.scale(1.5)
        title.to_edge(UP)

        # Create a complex plane
        plane = ComplexPlane(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            background_line_style={
                "stroke_opacity": 0.6,
                "stroke_width": 1,
            }
        ).scale(1.5)
        
        plane_title = MathTex(COMPLEX_PLANE_TITLE)
        plane_title.next_to(plane, UP)

        # Create unit circle
        circle = Circle(radius=1.5, color=BLUE)

        # Animation sequence
        self.play(Write(title))
        self.wait()
        
        self.play(
            Create(plane),
            Write(plane_title)
        )
        self.wait()
        
        self.play(Create(circle))
        self.wait()

        # Display properties one by one
        properties = VGroup()
        for i, prop in enumerate(PROPERTIES):
            property_tex = MathTex(prop)
            property_tex.scale(0.8)
            property_tex.to_edge(LEFT)
            property_tex.shift(DOWN * (i * 0.7 + 1))
            properties.add(property_tex)

        for prop in properties:
            self.play(Write(prop))
            self.wait(0.5)
        
        self.wait()

        # Clear properties and show important formulas
        self.play(FadeOut(properties))
        
        # Show Euler's formula
        euler = MathTex(EULER_FORMULA)
        euler.next_to(plane, DOWN, buff=0.5)
        
        self.play(Write(euler))
        self.wait()
        
        # Show De Moivre's formula
        demoivre = MathTex(DE_MOIVRE_FORMULA)
        demoivre.next_to(euler, DOWN, buff=0.5)
        
        self.play(Write(demoivre))
        self.wait(2)

        # Final fadeout
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class ComplexRootVisualization(Scene):
    def construct(self):
        # Create complex plane with unit circle
        plane = ComplexPlane().scale(2)
        circle = Circle(radius=2, color=YELLOW)
        
        # Setup initial scene
        self.play(
            Create(plane),
            Create(circle)
        )
        self.wait()

        # Demonstrate different roots of unity
        for n in [2, 3, 4]:
            # Create dots for nth roots
            roots = VGroup(*[
                Dot(2 * complex_to_R3(np.exp(2 * PI * i * 1j / n)))
                for i in range(n)
            ])
            
            # Create labels for angles
            angles = VGroup(*[
                MathTex(f"\\frac{{{2}\\pi {i}}}{{{n}}}")
                for i in range(n)
            ])
            
            # Position labels near their respective points
            for angle, root in zip(angles, roots):
                angle.next_to(root, UR, buff=0.1)
                angle.scale(0.7)
            
            # Show roots and angles
            self.play(
                AnimationGroup(*[Create(root) for root in roots]),
                AnimationGroup(*[Write(angle) for angle in angles])
            )
            self.wait()
            
            # Clear for next demonstration
            self.play(
                FadeOut(roots),
                FadeOut(angles)
            )
            self.wait(0.5)

        self.wait() 