from manim import *
import numpy as np

class GeometricPropertiesScene(Scene):
    def construct(self):
        # Title
        title = Text("Geometric Properties", font_size=64)
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

        # Unit circle with label
        circle = Circle(radius=1, color=YELLOW)
        circle.move_to(plane.get_center())
        circle_label = Text("Unit Circle", font_size=36, color=YELLOW)
        circle_label.next_to(circle, UP, buff=0.5)
        self.play(Create(circle), Write(circle_label))
        self.wait()

        # Show roots for n=5 with detailed labels
        n = 5
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

        # Show regular polygon with animation
        polygon = RegularPolygon(n=n, color=GREEN)
        polygon.move_to(plane.get_center())
        polygon_label = Text("Regular Pentagon", font_size=36, color=GREEN)
        polygon_label.next_to(polygon, DOWN, buff=0.5)
        self.play(Create(polygon), Write(polygon_label))
        self.wait()

        # Show rotation property with detailed explanation
        rotation_text = MathTex(
            r"\text{Rotation by } \frac{2\pi}{n}",
            font_size=48
        )
        rotation_text.next_to(plane, DOWN, buff=1)
        self.play(Write(rotation_text))
        
        rotation_explanation = Text(
            "Each root can be obtained by rotating any other root\n"
            "by an angle of 2π/n",
            font_size=36,
            color=YELLOW
        )
        rotation_explanation.next_to(rotation_text, DOWN, buff=0.5)
        self.play(Write(rotation_explanation))
        
        # Animate rotation with multiple steps
        for i in range(3):
            self.play(
                Rotate(polygon, angle=2*PI/n),
                *[Rotate(label, angle=2*PI/n) for label in labels],
                *[Rotate(angle_label, angle=2*PI/n) for angle_label in angles],
                run_time=1
            )
            self.wait(0.5)

        # Add final summary
        summary = Text(
            "The geometric properties of roots of unity\n"
            "reveal their symmetric and cyclic nature",
            font_size=36,
            color=WHITE
        )
        summary.next_to(rotation_explanation, DOWN, buff=1)
        self.play(Write(summary))
        self.wait(2)

        # Cleanup
        self.play(
            *[FadeOut(mob) for mob in [plane, circle, circle_label, polygon, polygon_label] +
                                     roots + labels + angles + [rotation_text, rotation_explanation, summary]],
            FadeOut(title)
        )

class SpecialCasesScene(Scene):
    def construct(self):
        # Title
        title = Text("Special Cases", font_size=64)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait()

        # Create three sections for square, cube, and fourth roots
        cases = [
            ("Square Roots", 2),
            ("Cube Roots", 3),
            ("Fourth Roots", 4)
        ]

        for case_name, n in cases:
            case_title = Text(case_name, font_size=48)
            case_title.next_to(title, DOWN, buff=1)
            self.play(Write(case_title))
            self.wait()

            # Complex plane with larger size
            plane = ComplexPlane(
                x_range=[-3, 3, 1],
                y_range=[-3, 3, 1],
                axis_config={"color": BLUE, "include_tip": True}
            )
            plane.scale(1.2)
            plane.next_to(case_title, DOWN, buff=1)
            self.play(Create(plane))
            self.wait()

            # Unit circle
            circle = Circle(radius=1, color=YELLOW)
            circle.move_to(plane.get_center())
            self.play(Create(circle))
            self.wait()

            # Show roots with detailed labels
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

            # Show regular polygon
            polygon = RegularPolygon(n=n, color=GREEN)
            polygon.move_to(plane.get_center())
            self.play(Create(polygon))
            self.wait()

            # Show formula with explanation
            formula = MathTex(
                f"z_k = e^{{\\frac{{2\\pi i k}}{{{n}}}}}",
                font_size=48
            )
            formula.next_to(plane, DOWN, buff=1)
            self.play(Write(formula))
            
            # Add specific case explanation
            if n == 2:
                explanation = Text(
                    "Square roots: ±1",
                    font_size=36,
                    color=YELLOW
                )
            elif n == 3:
                explanation = Text(
                    "Cube roots: 1, ω, ω² where ω = e^(2πi/3)",
                    font_size=36,
                    color=YELLOW
                )
            else:  # n == 4
                explanation = Text(
                    "Fourth roots: ±1, ±i",
                    font_size=36,
                    color=YELLOW
                )
            
            explanation.next_to(formula, DOWN, buff=0.5)
            self.play(Write(explanation))
            self.wait()

            # Animate rotation
            self.play(
                Rotate(polygon, angle=2*PI/n),
                *[Rotate(label, angle=2*PI/n) for label in labels],
                *[Rotate(angle_label, angle=2*PI/n) for angle_label in angles],
                run_time=1
            )
            self.wait()

            # Fade out current case
            self.play(
                *[FadeOut(mob) for mob in [plane, circle, polygon] + roots + labels + angles +
                                     [formula, explanation, case_title]]
            )

        self.play(FadeOut(title))

class CyclotomicPolynomialScene(Scene):
    def construct(self):
        # Title
        title = Text("Cyclotomic Polynomial", font_size=64)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait()

        # Definition with explanation
        definition = MathTex(
            r"\Phi_n(x) = \prod_{\substack{1 \leq k \leq n \\ \gcd(k,n)=1}} (x - e^{\frac{2\pi i k}{n}})",
            font_size=48
        )
        definition.next_to(title, DOWN, buff=1)
        self.play(Write(definition))
        
        explanation = Text(
            "The cyclotomic polynomial is the minimal polynomial\n"
            "whose roots are the primitive nth roots of unity",
            font_size=36,
            color=YELLOW
        )
        explanation.next_to(definition, DOWN, buff=0.5)
        self.play(Write(explanation))
        self.wait()

        # Example for n=4
        example_title = Text("Example: n = 4", font_size=48)
        example_title.next_to(explanation, DOWN, buff=1)
        self.play(Write(example_title))
        self.wait()

        # Complex plane with larger size
        plane = ComplexPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": BLUE, "include_tip": True}
        )
        plane.scale(1.2)
        plane.next_to(example_title, DOWN, buff=1)
        self.play(Create(plane))
        self.wait()

        # Show primitive roots for n=4 with detailed labels
        n = 4
        roots = []
        labels = []
        angles = []
        for k in range(n):
            if np.gcd(k, n) == 1:  # Only show primitive roots
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

        # Show resulting polynomial with explanation
        polynomial = MathTex(
            r"\Phi_4(x) = x^2 + 1",
            font_size=48
        )
        polynomial.next_to(plane, DOWN, buff=1)
        self.play(Write(polynomial))
        
        polynomial_explanation = Text(
            "This polynomial is irreducible over the rationals\n"
            "and generates the field extension Q(i)",
            font_size=36,
            color=YELLOW
        )
        polynomial_explanation.next_to(polynomial, DOWN, buff=0.5)
        self.play(Write(polynomial_explanation))
        self.wait(2)

        # Cleanup
        self.play(
            *[FadeOut(mob) for mob in [plane] + roots + labels + angles +
                                     [definition, explanation, example_title,
                                      polynomial, polynomial_explanation]],
            FadeOut(title)
        )

class MinimalPolynomialScene(Scene):
    def construct(self):
        # Title
        title = Text("Minimal Polynomial", font_size=64)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait()

        # Definition with explanation
        definition = MathTex(
            r"\text{The minimal polynomial of a primitive root is the cyclotomic polynomial}",
            font_size=48
        )
        definition.next_to(title, DOWN, buff=1)
        self.play(Write(definition))
        
        explanation = Text(
            "It is the monic polynomial of least degree\n"
            "that has the primitive root as a root",
            font_size=36,
            color=YELLOW
        )
        explanation.next_to(definition, DOWN, buff=0.5)
        self.play(Write(explanation))
        self.wait()

        # Example for n=3
        example_title = Text("Example: n = 3", font_size=48)
        example_title.next_to(explanation, DOWN, buff=1)
        self.play(Write(example_title))
        self.wait()

        # Complex plane with larger size
        plane = ComplexPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": BLUE, "include_tip": True}
        )
        plane.scale(1.2)
        plane.next_to(example_title, DOWN, buff=1)
        self.play(Create(plane))
        self.wait()

        # Show primitive root with detailed labels
        n = 3
        angle = 2 * PI / n
        point = Dot(plane.c2p(np.cos(angle), np.sin(angle)), color=RED, radius=0.1)
        label = MathTex("\\zeta", font_size=36)
        label.next_to(point, direction=UP)
        
        # Add angle label
        angle_label = MathTex(
            f"\\frac{{2\\pi}}{{{n}}}",
            font_size=32,
            color=GREEN
        )
        angle_label.next_to(point, direction=RIGHT)
        
        self.play(
            Create(point),
            Write(label),
            Write(angle_label)
        )
        self.wait()

        # Show minimal polynomial with explanation
        polynomial = MathTex(
            r"x^2 + x + 1",
            font_size=48
        )
        polynomial.next_to(plane, DOWN, buff=1)
        self.play(Write(polynomial))
        
        polynomial_explanation = Text(
            "This is the minimal polynomial of ζ",
            font_size=36,
            color=YELLOW
        )
        polynomial_explanation.next_to(polynomial, DOWN, buff=0.5)
        self.play(Write(polynomial_explanation))
        self.wait()

        # Show property with animation
        property_text = MathTex(
            r"\zeta^2 + \zeta + 1 = 0",
            font_size=48
        )
        property_text.next_to(polynomial_explanation, DOWN, buff=0.5)
        self.play(Write(property_text))
        
        property_explanation = Text(
            "This equation characterizes the algebraic properties\n"
            "of the primitive cube root of unity",
            font_size=36,
            color=YELLOW
        )
        property_explanation.next_to(property_text, DOWN, buff=0.5)
        self.play(Write(property_explanation))
        self.wait(2)

        # Cleanup
        self.play(
            *[FadeOut(mob) for mob in [plane, point, label, angle_label,
                                     definition, explanation, example_title,
                                     polynomial, polynomial_explanation,
                                     property_text, property_explanation]],
            FadeOut(title)
        ) 