from manim import *
import numpy as np

class NthRootsOfUnityScene(Scene):
    def construct(self):
        # Title with larger font
        title = Text("nth Roots of Unity", font_size=64)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait()

        # Definition with more detailed explanation
        definition = MathTex(
            r"\text{The }n\text{th roots of unity are the solutions to: }",
            r"z^n = 1",
            font_size=48
        )
        definition.next_to(title, DOWN, buff=1)
        self.play(Write(definition))
        self.wait()

        # General formula with explanation
        formula = MathTex(
            r"z_k = e^{\frac{2\pi i k}{n}}",
            r"\text{ where } k = 0, 1, 2, ..., n-1",
            font_size=48
        )
        formula.next_to(definition, DOWN, buff=1)
        self.play(Write(formula))
        
        # Add explanation text
        explanation = Text(
            "Each root represents a point on the unit circle\n"
            "equally spaced at angles of 2π/n",
            font_size=36,
            color=YELLOW
        )
        explanation.next_to(formula, DOWN, buff=1)
        self.play(Write(explanation))
        self.wait(2)
        self.play(FadeOut(definition), FadeOut(formula), FadeOut(explanation))

        # Complex plane setup with larger size
        plane = ComplexPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": BLUE, "include_tip": True}
        )
        plane.scale(1.2)
        plane.next_to(title, DOWN, buff=1)
        self.play(Create(plane))
        self.wait()

        # Unit circle with label
        circle = Circle(radius=1, color=YELLOW)
        circle.move_to(plane.get_center())
        circle_label = Text("Unit Circle", font_size=36, color=YELLOW)
        circle_label.next_to(circle, UP, buff=0.5)
        self.play(Create(circle), Write(circle_label))
        self.wait()

        # Show roots for n=4 with more detailed labels
        n = 4
        roots = []
        labels = []
        angles = []
        
        for k in range(n):
            angle = 2 * PI * k / n
            point = Dot(plane.c2p(np.cos(angle), np.sin(angle)), color=RED, radius=0.1)
            label = MathTex(f"z_{k}", font_size=36)
            label.next_to(point, direction=UP)
            
            # Add angle label
            angle_label = MathTex(
                f"\\frac{{{k}}}{{{n}}} \\cdot 2\\pi",
                font_size=32,
                color=GREEN
            )
            angle_label.next_to(point, direction=RIGHT)
            
            roots.append(point)
            labels.append(label)
            angles.append(angle_label)
            
            self.play(
                Create(point),
                Write(label),
                Write(angle_label)
            )
            self.wait(0.5)

        # Show rotation animation
        self.play(
            *[Rotate(label, angle=2*PI/n) for label in labels],
            *[Rotate(angle_label, angle=2*PI/n) for angle_label in angles],
            run_time=2
        )
        self.wait()

        # Add final summary
        summary = Text(
            "The nth roots of unity form a regular n-gon\n"
            "on the unit circle in the complex plane",
            font_size=36,
            color=WHITE
        )
        summary.next_to(plane, DOWN, buff=1)
        self.play(Write(summary))
        self.wait(2)

        # Cleanup
        self.play(
            *[FadeOut(mob) for mob in [plane, circle, circle_label] + roots + labels + angles + [summary]],
            FadeOut(title)
        )

class PolarFormScene(Scene):
    def construct(self):
        # Title
        title = Text("Polar Form Representation", font_size=64)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait()

        # Complex plane with larger size
        plane = ComplexPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": BLUE, "include_tip": True}
        )
        plane.scale(1.2)
        plane.next_to(title, DOWN, buff=1)
        self.play(Create(plane))
        self.wait()

        # Show a point and its polar form with more detail
        point = Dot(plane.c2p(1, 1), color=RED, radius=0.1)
        self.play(Create(point))
        
        # Draw radius and angle with labels
        radius = Line(plane.get_center(), point.get_center(), color=YELLOW)
        angle = Angle(Line(plane.get_center(), plane.c2p(1, 0)), radius, radius=0.8)
        radius_label = MathTex("r", font_size=36, color=YELLOW)
        radius_label.next_to(radius.get_center(), direction=UP)
        angle_label = MathTex("\\theta", font_size=36, color=GREEN)
        angle_label.next_to(angle, direction=RIGHT)
        
        self.play(
            Create(radius),
            Create(angle),
            Write(radius_label),
            Write(angle_label)
        )
        self.wait()
        
        # Show polar form equation with explanation
        polar_form = MathTex(
            r"z = r(\cos\theta + i\sin\theta)",
            font_size=48
        )
        polar_form.next_to(plane, DOWN, buff=1)
        self.play(Write(polar_form))
        
        # Add explanation
        explanation = Text(
            "r: distance from origin (modulus)\n"
            "θ: angle from positive real axis (argument)",
            font_size=36,
            color=YELLOW
        )
        explanation.next_to(polar_form, DOWN, buff=0.5)
        self.play(Write(explanation))
        self.wait()
        
        # Show Euler's form with transition
        euler_form = MathTex(
            r"z = re^{i\theta}",
            font_size=48
        )
        euler_form.next_to(explanation, DOWN, buff=0.5)
        self.play(Write(euler_form))
        
        # Add Euler's formula explanation
        euler_explanation = MathTex(
            r"e^{i\theta} = \cos\theta + i\sin\theta",
            font_size=36,
            color=GREEN
        )
        euler_explanation.next_to(euler_form, DOWN, buff=0.5)
        self.play(Write(euler_explanation))
        self.wait(2)
        
        # Cleanup
        self.play(
            *[FadeOut(mob) for mob in [plane, point, radius, angle, radius_label, angle_label,
                                     polar_form, explanation, euler_form, euler_explanation]],
            FadeOut(title)
        )

class UnityPropertiesScene(Scene):
    def construct(self):
        # Title
        title = Text("Unity Properties & Sum and Product of Roots", font_size=64)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait()

        # Show sum property with explanation
        sum_property = MathTex(
            r"\sum_{k=0}^{n-1} z_k = 0",
            font_size=48
        )
        sum_property.next_to(title, DOWN, buff=1)
        self.play(Write(sum_property))
        
        sum_explanation = Text(
            "The sum of all nth roots of unity is zero",
            font_size=36,
            color=YELLOW
        )
        sum_explanation.next_to(sum_property, DOWN, buff=0.5)
        self.play(Write(sum_explanation))
        self.wait()

        # Show product property with explanation
        product_property = MathTex(
            r"\prod_{k=0}^{n-1} z_k = (-1)^{n-1}",
            font_size=48
        )
        product_property.next_to(sum_explanation, DOWN, buff=1)
        self.play(Write(product_property))
        
        product_explanation = Text(
            "The product of all nth roots of unity is (-1)^(n-1)",
            font_size=36,
            color=YELLOW
        )
        product_explanation.next_to(product_property, DOWN, buff=0.5)
        self.play(Write(product_explanation))
        self.wait()

        # Complex plane visualization with larger size
        plane = ComplexPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": BLUE, "include_tip": True}
        )
        plane.scale(1.2)
        plane.next_to(product_explanation, DOWN, buff=1)
        self.play(Create(plane))
        self.wait()

        # Show roots for n=3 with detailed labels
        n = 3
        roots = []
        labels = []
        for k in range(n):
            angle = 2 * PI * k / n
            point = Dot(plane.c2p(np.cos(angle), np.sin(angle)), color=RED, radius=0.1)
            label = MathTex(f"z_{k}", font_size=36)
            label.next_to(point, direction=UP)
            roots.append(point)
            labels.append(label)
            self.play(Create(point), Write(label))
            self.wait(0.5)

        # Show sum vector with animation
        sum_vector = Vector(plane.c2p(0, 0), color=GREEN)
        sum_label = Text("Sum = 0", font_size=36, color=GREEN)
        sum_label.next_to(sum_vector, DOWN, buff=0.5)
        self.play(Create(sum_vector), Write(sum_label))
        self.wait()

        # Add final summary
        summary = Text(
            "These properties are fundamental to understanding\n"
            "the geometric and algebraic nature of roots of unity",
            font_size=36,
            color=WHITE
        )
        summary.next_to(plane, DOWN, buff=1)
        self.play(Write(summary))
        self.wait(2)

        # Cleanup
        self.play(
            *[FadeOut(mob) for mob in [plane] + roots + labels + [sum_vector, sum_label,
                                     sum_property, sum_explanation, product_property,
                                     product_explanation, summary]],
            FadeOut(title)
        )

class PrimitiveRootScene(Scene):
    def construct(self):
        # Title
        title = Text("Primitive Root and Principal Root", font_size=64)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait()

        # Complex plane with larger size
        plane = ComplexPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": BLUE, "include_tip": True}
        )
        plane.scale(1.2)
        plane.next_to(title, DOWN, buff=1)
        self.play(Create(plane))
        self.wait()

        # Show primitive root definition with more detail
        primitive_def = MathTex(
            r"\text{A primitive root is a root that generates all other roots}",
            font_size=48
        )
        primitive_def.next_to(plane, DOWN, buff=1)
        self.play(Write(primitive_def))
        
        # Add explanation
        explanation = Text(
            "When raised to powers, it cycles through all other roots",
            font_size=36,
            color=YELLOW
        )
        explanation.next_to(primitive_def, DOWN, buff=0.5)
        self.play(Write(explanation))
        self.wait()

        # Show roots for n=4 with detailed labels
        n = 4
        roots = []
        labels = []
        for k in range(n):
            angle = 2 * PI * k / n
            point = Dot(plane.c2p(np.cos(angle), np.sin(angle)), color=RED, radius=0.1)
            label = MathTex(f"z_{k}", font_size=36)
            label.next_to(point, direction=UP)
            roots.append(point)
            labels.append(label)
            self.play(Create(point), Write(label))
            self.wait(0.5)

        # Highlight primitive root with animation
        primitive_root = roots[1]
        primitive_root.set_color(YELLOW)
        primitive_label = Text("Primitive Root", font_size=36, color=YELLOW)
        primitive_label.next_to(primitive_root, DOWN, buff=0.5)
        self.play(
            primitive_root.animate.set_color(YELLOW),
            Write(primitive_label)
        )
        self.wait()

        # Show principal root
        principal_def = MathTex(
            r"\text{Principal root: } z_0 = 1",
            font_size=48
        )
        principal_def.next_to(explanation, DOWN, buff=1)
        self.play(Write(principal_def))
        
        # Add final summary
        summary = Text(
            "The primitive root is crucial for understanding\n"
            "the multiplicative structure of roots of unity",
            font_size=36,
            color=WHITE
        )
        summary.next_to(principal_def, DOWN, buff=0.5)
        self.play(Write(summary))
        self.wait(2)

        # Cleanup
        self.play(
            *[FadeOut(mob) for mob in [plane] + roots + labels + [primitive_label,
                                     primitive_def, explanation, principal_def, summary]],
            FadeOut(title)
        ) 