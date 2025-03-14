import sys
from manim import Scene
from animations.introduction import IntroductionScene, ComplexRootVisualization
from animations.specific_roots import SpecificRootsScene, RootPatternScene
from slides.slide_generator import SlideGenerator

def render_manim_scene(scene_class: type[Scene]) -> None:
    """Render a specific Manim scene."""
    scene = scene_class()
    
    scene.render()

def list_available_scenes() -> list[tuple[int, str, type[Scene]]]:
    """List all available Manim scenes."""
    scenes = [
        (1, "Introduction to Roots of Unity", IntroductionScene),
        (2, "Complex Root Visualization", ComplexRootVisualization),
        (3, "Specific Roots of Unity", SpecificRootsScene),
        (4, "Root Pattern Visualization", RootPatternScene),
    ]
    return scenes

def render_slides() -> None:
    """Render the presentation slides."""
    print("\nGenerating presentation slides...")
    try:
        generator = SlideGenerator()
        generator.generate_slides()
        print("\nSlides generated successfully!")
        print("You can open the presentation in your browser at: slides/output/presentation.html")
    except Exception as e:
        print(f"\nError generating slides: {str(e)}")

def main():
    while True:
        print("\n=== Nth Roots of Unity Interactive Runner ===")
        print("\nWhat would you like to do?")
        print("1. Render Manim Scenes")
        print("2. Generate Slides")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            print("\nAvailable Manim Scenes:")
            scenes = list_available_scenes()
            for num, name, _ in scenes:
                print(f"{num}. {name}")
            
            scene_choice = input("\nEnter scene number to render (or 'b' to go back): ").strip()
            if scene_choice.lower() == 'b':
                continue
                
            try:
                scene_num = int(scene_choice)
                selected_scene = next((scene for num, _, scene in scenes if num == scene_num), None)
                if selected_scene:
                    print(f"\nRendering scene {scene_num}...")
                    render_manim_scene(selected_scene)
                else:
                    print("\nInvalid scene number!")
            except ValueError:
                print("\nInvalid input! Please enter a number.")
                
        elif choice == "2":
            render_slides()
            
        elif choice == "3":
            print("\nGoodbye!")
            sys.exit(0)
            
        else:
            print("\nInvalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
