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
        
        # Transition to unity roots concept
        unity_intro = Text(
            "But what if we want numbers that come back to 1\n"
            "after multiplying by themselves a certain number of times?",
            font_size=32
        ).to_edge(UP)
        
        equation = MathTex("z^n = 1")
        equation.scale(1.5)
        equation.next_to(unity_intro, DOWN, buff=1)
        
        # Example with square roots of unity
        square_root_example = VGroup(
            Text("For example, when n=2:", font_size=28),
            MathTex("1 \\times 1 = 1"),
            MathTex("-1 \\times -1 = 1"),
            Text("These are the square roots of unity!", font_size=28, color=GREEN)
        ).arrange(DOWN, buff=0.4)
        square_root_example.next_to(equation, DOWN, buff=1)
        
        # Transition to main concept
        self.play(
            FadeOut(explanation),
            FadeOut(question),
            FadeOut(real_example),
        )
        self.play(Write(unity_intro))
        self.wait(2)
        self.play(Write(equation))
        self.wait(2)
        self.play(Write(square_root_example))
        self.wait(4)
        
        # Clear for next section
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        self.wait(1)

        # Main title with adjusted position
        title = MathTex(ROOTS_OF_UNITY_TITLE)
        title.scale(1.5)
        title.to_edge(UP).shift(LEFT * 3)  # Moved more to the left

        # Create and setup complex plane - moved right and made slightly smaller
        plane = ComplexPlane(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            background_line_style={
                "stroke_opacity": 0.6,
                "stroke_width": 1,
            }
        ).scale(1)  # Reduced scale
        plane.shift(RIGHT * 4)  # Moved further right
        
        # Add axis labels with better positioning
        x_label = Text("Real", font_size=20)
        x_label.next_to(plane.x_axis.get_end(), DOWN + RIGHT, buff=0.1)
        
        y_label = Text("Imaginary", font_size=20)
        y_label.next_to(plane.y_axis.get_end(), UP + LEFT, buff=0.1)
        y_label.rotate(90 * DEGREES)  # Rotate for better fit
        
        plane_title = MathTex(COMPLEX_PLANE_TITLE)
        plane_title.scale(0.8)  # Made smaller
        plane_title.next_to(plane, UP, buff=0.2)

        # Create unit circle with radius indicator - adjusted for new plane size
        circle = Circle(radius=1, color=BLUE)  # Adjusted radius
        circle.shift(RIGHT * 4)  # Match plane position
        radius_line = Line(
            circle.get_center(),
            circle.get_center() + RIGHT * 1,
            color=YELLOW
        )
        radius_label = Text("r=1", font_size=20, color=YELLOW)  # Simplified label
        radius_label.next_to(radius_line.get_center(), DOWN, buff=0.1)

        plane_explanation = Text(
            "We need complex numbers\nto find all roots",
            font_size=24,
            line_spacing=1.5
        )
        
        circle_explanation = Text(
            "All roots lie on the\nunit circle",
            font_size=24,
            line_spacing=1.5
        )
        
        # Organize explanations on the left
        explanations = VGroup(plane_explanation, circle_explanation)
        explanations.arrange(DOWN, buff=0.8)
        explanations.next_to(title, DOWN, buff=1)
        
        # Animation sequence with better timing
        self.play(Write(title))
        self.wait(2)
        
        # Show plane with labels
        self.play(
            Create(plane),
            Write(plane_title),
        )
        self.wait(1)
        self.play(
            Write(x_label),
            Write(y_label)
        )
        self.wait(2)
        
        # Show first explanation and circle
        self.play(Write(plane_explanation))
        self.wait(2)
        
        self.play(
            Create(circle),
            Create(radius_line),
            Write(radius_label),
        )
        self.play(Write(circle_explanation))
        self.wait(3)

        # Clear explanations for properties
        self.play(
            FadeOut(plane_explanation),
            FadeOut(circle_explanation),
            FadeOut(radius_line),
            FadeOut(radius_label)
        )
        self.wait(1)

        # Display properties with better spacing
        properties = VGroup()
        property_explanations = VGroup()
        
        for i, prop in enumerate(PROPERTIES):
            property_group = VGroup()
            
            property_tex = MathTex(prop)
            property_tex.scale(0.6)  # Made smaller
            
            explanation = Text(
                self.get_property_explanation(i),
                font_size=20,  # Smaller font
                color=BLUE_B
            )
            
            property_group.add(property_tex, explanation)
            property_group.arrange(DOWN, buff=0.2)
            
            if i == 0:
                property_group.next_to(title, DOWN, buff=1)
            else:
                property_group.next_to(properties[i-1], DOWN, buff=0.6)
            
            property_group.align_to(title, LEFT)
            properties.add(property_group)
            
            self.play(Write(property_tex))
            self.play(Write(explanation))
            self.wait(2)

        self.wait(2)

        # Clear for formulas
        self.play(FadeOut(properties))
        self.wait(1)

        # Show Euler's formula with better positioning
        euler_group = VGroup()
        
        euler_explanation = Text(
            "Euler's formula connects complex\nnumbers with circles:",
            font_size=24,
            line_spacing=1.5
        )
        
        euler = MathTex(EULER_FORMULA)
        euler.scale(0.8)
        
        euler_group.add(euler_explanation, euler)
        euler_group.arrange(DOWN, buff=0.5)
        euler_group.next_to(title, DOWN, buff=1)
        euler_group.align_to(title, LEFT)
        
        self.play(Write(euler_explanation))
        self.wait(1)
        self.play(Write(euler))
        self.wait(2)

        # Show De Moivre's formula with better positioning
        demoivre_group = VGroup()
        
        demoivre_explanation = Text(
            "De Moivre's formula helps us\nfind powers:",
            font_size=24,
            line_spacing=1.5
        )
        
        demoivre = MathTex(DE_MOIVRE_FORMULA)
        demoivre.scale(0.8)
        
        demoivre_group.add(demoivre_explanation, demoivre)
        demoivre_group.arrange(DOWN, buff=0.5)
        demoivre_group.next_to(euler_group, DOWN, buff=1)
        demoivre_group.align_to(euler_group, LEFT)
        
        self.play(Write(demoivre_explanation))
        self.wait(1)
        self.play(Write(demoivre))
        self.wait(3)

        # Final summary with better positioning
        summary = Text(
            "These formulas help us find all\n"
            "nth roots of unity and understand\n"
            "their beautiful patterns",
            font_size=24,
            line_spacing=1.5,
            color=GREEN
        )
        summary.next_to(demoivre_group, DOWN, buff=1)
        summary.align_to(title, LEFT)
        
        self.play(Write(summary))
        self.wait(3)

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