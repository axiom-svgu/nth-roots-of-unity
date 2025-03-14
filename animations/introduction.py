from manim import *
from animations.equations import (
    ROOTS_OF_UNITY_TITLE,
    COMPLEX_PLANE_TITLE,
    PROPERTIES,
    EULER_FORMULA,
    DE_MOIVRE_FORMULA
)

class IntroductionScene(Scene):
    def construct(self):
        # Initial friendly explanation
        explanation = Text(
            "Let's explore something fascinating in mathematics:",
            font_size=36,
            color=BLUE
        ).to_edge(UP)
        
        question = Text(
            "What happens when we keep multiplying\n"
            "a number by itself?",
            font_size=32
        ).next_to(explanation, DOWN, buff=0.8)
        
        # Simple example with real numbers
        real_example = VGroup(
            MathTex("2 \\times 2 = 4"),
            MathTex("4 \\times 2 = 8"),
            MathTex("8 \\times 2 = 16"),
            Text("(keeps growing)", font_size=24)
        ).arrange(DOWN, buff=0.3)
        real_example.next_to(question, DOWN, buff=0.8)
        
        # Show initial concept
        self.play(Write(explanation))
        self.wait(2)
        self.play(Write(question))
        self.wait(2)
        self.play(Write(real_example))
        self.wait(3)
        
        # Clear screen for unity roots concept
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        
        # Setup main title and complex plane
        title = MathTex(ROOTS_OF_UNITY_TITLE)
        title.scale(1.2)
        title.to_edge(UP)

        # Create a larger complex plane as the central focus
        plane = ComplexPlane(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            background_line_style={
                "stroke_opacity": 0.6,
                "stroke_width": 1,
            }
        ).scale(1.2)  # Slightly smaller scale
        
        # Position plane on the right side
        plane.shift(RIGHT * 3 + DOWN * 0.5)
        
        # Add clear axis labels with adjusted positions
        x_label = Text("r", font_size=24)
        x_label.next_to(plane.x_axis.get_end(), DOWN + RIGHT, buff=0.2)
        
        y_label = Text("i", font_size=24)
        y_label.next_to(plane.y_axis.get_end(), UP + LEFT, buff=0.2)
        y_label.rotate(90 * DEGREES)
        
        # Create unit circle with clear radius indicator - adjusted for new plane position
        circle = Circle(radius=1.2, color=BLUE)  # Matches plane scale
        circle.move_to(plane.get_center())
        radius_line = Line(
            circle.get_center(),
            circle.get_center() + RIGHT * 1.2,
            color=YELLOW
        )
        radius_label = Text("r=1", font_size=24, color=YELLOW)
        radius_label.next_to(radius_line.get_center(), DOWN, buff=0.1)

        # Show plane and basic elements with animations
        self.play(Write(title))
        self.play(Create(plane))
        self.play(
            Write(x_label),
            Write(y_label)
        )
        self.wait(1)
        
        self.play(
            Create(circle),
            Create(radius_line),
            Write(radius_label)
        )
        self.wait(2)

        # First two properties with visual demonstrations - positioned on the left
        # Property 1: Unit distance
        prop1 = MathTex(PROPERTIES[0])
        prop1.scale(0.8)
        prop1.to_edge(LEFT, buff=1).shift(UP * 1)  # Increased left buffer
        
        # Animate multiple points at unit distance
        points = VGroup(*[
            Dot(circle.point_from_proportion(i/8), color=GREEN)
            for i in range(8)
        ])
        
        self.play(Write(prop1))
        self.play(AnimationGroup(*[Create(p) for p in points], lag_ratio=0.1))
        self.wait(1)
        self.play(FadeOut(points))
        
        # Property 2: Even spacing
        prop2 = MathTex(PROPERTIES[1])
        prop2.scale(0.8)
        prop2.next_to(prop1, DOWN, buff=1)
        prop2.align_to(prop1, LEFT)
        
        # Show angle markers for even spacing - adjusted for new plane position
        angles = VGroup(*[
            Arc(radius=0.4, angle=2*PI/4 * i, color=RED)
            for i in range(1, 4)
        ])
        angles.move_to(plane.get_center())
        
        self.play(Write(prop2))
        self.play(Create(angles))
        self.wait(2)
        
        # Clear for next page
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        self.wait(1)

        # Second page - recreate plane and circle with same positioning
        title.to_edge(UP)
        self.play(
            Write(title),
            Create(plane),
            Create(circle)
        )
        
        # Property 3 and 4 with dynamic demonstrations - positioned on the left
        prop3 = MathTex(PROPERTIES[2])
        prop3.scale(0.8)
        prop3.to_edge(LEFT, buff=1).shift(UP * 1)  # Increased left buffer
        
        # Show starting point at (1,0)
        start_point = Dot(circle.point_at_angle(0), color=GREEN)
        start_label = MathTex("1").next_to(start_point, RIGHT)
        
        self.play(Write(prop3))
        self.play(
            Create(start_point),
            Write(start_label)
        )
        
        # Property 4 with rotation demonstration
        prop4 = MathTex(PROPERTIES[3])
        prop4.scale(0.8)
        prop4.next_to(prop3, DOWN, buff=1)
        prop4.align_to(prop3, LEFT)
        
        # Demonstrate rotation for different k values
        rotating_point = Dot(circle.point_at_angle(0), color=YELLOW)
        self.play(Write(prop4))
        
        for angle in [PI/2, PI, 3*PI/2]:
            self.play(
                rotating_point.animate.move_to(circle.point_at_angle(angle)),
                run_time=0.5
            )
        
        self.wait(2)
        
        # Final fadeout
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        self.wait(2)

    def get_property_explanation(self, index):
        explanations = [
            "All points are exactly 1 unit\nfrom the center",
            "Points are evenly spaced\naround the circle",
            "We start counting from\nthis position",
            "Multiply the angle by k\nto find each root"
        ]
        return explanations[index]

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