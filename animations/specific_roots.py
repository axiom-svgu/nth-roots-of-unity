from manim import *
from animations.equations import (
    SQUARE_ROOTS_OF_UNITY,
    CUBE_ROOTS_OF_UNITY,
    FOURTH_ROOTS_OF_UNITY,
    EULER_FORMULA,
    DE_MOIVRE_FORMULA,
    POLAR_FORM
)

class SpecificRootsScene(Scene):
    def construct(self):
        # Title
        title = Text("Exploring Specific Roots of Unity", font_size=36)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)

        # Create a reusable complex plane setup
        def create_plane_setup():
            plane = ComplexPlane(
                x_range=[-2, 2, 1],
                y_range=[-2, 2, 1],
                background_line_style={
                    "stroke_opacity": 0.6,
                    "stroke_width": 1,
                }
            ).scale(1)
            
            circle = Circle(radius=1, color=BLUE)
            circle.move_to(plane.get_center())
            
            # Add axis labels
            x_label = Text("Re", font_size=20)
            x_label.next_to(plane.x_axis.get_end(), DOWN + RIGHT, buff=0.1)
            
            y_label = Text("Im", font_size=20)
            y_label.next_to(plane.y_axis.get_end(), UP + LEFT, buff=0.1)
            
            return VGroup(plane, circle, x_label, y_label)

        # Function to create root dots and labels
        def create_root_points(n, radius=1):
            dots = VGroup()
            labels = VGroup()
            
            for k in range(n):
                angle = k * 2 * PI / n
                point = radius * complex_to_R3(np.exp(1j * angle))
                dot = Dot(point, color=YELLOW)
                dots.add(dot)
                
                # Create label based on the angle
                if k == 0:
                    label_text = "1"
                elif k == n//2 and n % 2 == 0:
                    label_text = "-1"
                elif k == n//4 and n % 4 == 0:
                    label_text = "i"
                elif k == 3*n//4 and n % 4 == 0:
                    label_text = "-i"
                else:
                    label_text = f"e^{{2\\pi i {k}/{n}}}"
                
                label = MathTex(label_text, font_size=20)
                offset = 0.3 * np.array([np.cos(angle), np.sin(angle), 0])
                label.next_to(dot, normalize(point) * 0.5, buff=0.1)
                labels.add(label)
            
            return dots, labels

        # Create main plane setup and shift it right
        setup = create_plane_setup()
        setup.shift(RIGHT * 3)
        self.play(Create(setup))

        # Create a box for equations on the left side
        eq_box = Rectangle(
            width=4.5,
            height=3,
            stroke_color=GREY,
            stroke_opacity=0.5
        ).shift(LEFT * 3)
        self.play(Create(eq_box))

        # Square roots of unity (n=2)
        square_title = Text("Square Roots of Unity (n=2)", font_size=24)
        square_title.next_to(title, DOWN, buff=0.3)
        
        self.play(Write(square_title))
        
        dots2, labels2 = create_root_points(2)
        dots2.shift(RIGHT * 3)
        labels2.shift(RIGHT * 3)
        self.play(
            Create(dots2),
            Write(labels2)
        )
        
        # Show equation for square roots
        square_eq = MathTex("z^2 = 1", font_size=32)
        square_eq.move_to(eq_box.get_center() + UP * 0.5)
        square_solutions = MathTex("z = \\pm 1", font_size=32)
        square_solutions.next_to(square_eq, DOWN, buff=0.5)
        
        self.play(
            Write(square_eq),
            Write(square_solutions)
        )
        self.wait(2)
        
        # Clear for cube roots
        self.play(
            *[FadeOut(mob) for mob in [square_title, dots2, labels2, square_eq, square_solutions]]
        )
        
        # Cube roots of unity (n=3)
        cube_title = Text("Cube Roots of Unity (n=3)", font_size=24)
        cube_title.next_to(title, DOWN, buff=0.3)
        
        self.play(Write(cube_title))
        
        dots3, labels3 = create_root_points(3)
        dots3.shift(RIGHT * 3)
        labels3.shift(RIGHT * 3)
        self.play(
            Create(dots3),
            Write(labels3)
        )
        
        # Show equation for cube roots
        cube_eq = MathTex("z^3 = 1", font_size=32)
        cube_eq.move_to(eq_box.get_center() + UP * 0.5)
        cube_solutions = MathTex(
            "z = 1, -\\frac{1}{2} \\pm i\\frac{\\sqrt{3}}{2}",
            font_size=28
        )
        cube_solutions.next_to(cube_eq, DOWN, buff=0.5)
        
        self.play(
            Write(cube_eq),
            Write(cube_solutions)
        )
        self.wait(2)
        
        # Clear for fourth roots
        self.play(
            *[FadeOut(mob) for mob in [cube_title, dots3, labels3, cube_eq, cube_solutions]]
        )
        
        # Fourth roots of unity (n=4)
        fourth_title = Text("Fourth Roots of Unity (n=4)", font_size=24)
        fourth_title.next_to(title, DOWN, buff=0.3)
        
        self.play(Write(fourth_title))
        
        dots4, labels4 = create_root_points(4)
        dots4.shift(RIGHT * 3)
        labels4.shift(RIGHT * 3)
        self.play(
            Create(dots4),
            Write(labels4)
        )
        
        # Show equation for fourth roots
        fourth_eq = MathTex("z^4 = 1", font_size=32)
        fourth_eq.move_to(eq_box.get_center() + UP * 0.5)
        fourth_solutions = MathTex("z = 1, i, -1, -i", font_size=32)
        fourth_solutions.next_to(fourth_eq, DOWN, buff=0.5)
        
        self.play(
            Write(fourth_eq),
            Write(fourth_solutions)
        )
        self.wait(2)
        
        # Show Euler's formula at the bottom
        euler = MathTex(EULER_FORMULA, font_size=28)
        euler.to_edge(DOWN, buff=0.5)
        self.play(Write(euler))
        self.wait(2)
        
        # Final cleanup
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        self.wait(1)

class RootPatternScene(Scene):
    def construct(self):
        # Title
        title = Text("Patterns in Roots of Unity", font_size=40)
        title.to_edge(UP)
        
        # Create plane and circle
        plane = ComplexPlane().scale(2)
        circle = Circle(radius=2, color=BLUE)
        
        self.play(
            Write(title),
            Create(plane),
            Create(circle)
        )
        self.wait(1)
        
        # Demonstrate pattern for increasing n
        for n in range(2, 9):
            # Create dots for nth roots
            angle = 2 * PI / n
            dots = VGroup(*[
                Dot(2 * complex_to_R3(np.exp(angle * i * 1j)), color=YELLOW)
                for i in range(n)
            ])
            
            # Create angle arcs to show spacing
            arcs = VGroup(*[
                Arc(radius=0.5, angle=angle * i, color=RED)
                for i in range(1, n)
            ])
            
            # Show number of roots
            count_text = Text(f"n = {n}", font_size=36)
            count_text.to_edge(LEFT)
            
            # Animate
            self.play(
                Write(count_text),
                AnimationGroup(*[Create(dot) for dot in dots], lag_ratio=0.1),
                Create(arcs)
            )
            self.wait(1)
            
            # Clear for next iteration
            self.play(
                FadeOut(dots),
                FadeOut(arcs),
                FadeOut(count_text)
            )
        
        # Final cleanup
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        self.wait(1) 