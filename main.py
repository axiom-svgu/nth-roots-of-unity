import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from manim import Scene, config
from animations.introduction import IntroductionScene, ComplexRootVisualization
from animations.specific_roots import SpecificRootsScene, RootPatternScene
from animations.core_concepts import (
    NthRootsOfUnityScene,
    PolarFormScene,
    UnityPropertiesScene,
    PrimitiveRootScene
)
from animations.advanced_concepts import (
    GeometricPropertiesScene,
    SpecialCasesScene
)
from slides.slide_generator import SlideGenerator

def render_manim_scene(scene_class: type[Scene], scene_name: str = None) -> None:
    """Render a specific Manim scene.
    
    Args:
        scene_class: The Manim scene class to render
        scene_name: Optional name to use for the output file. If None, uses the class name.
    """
    if scene_name:
        # Convert the scene name to a valid filename
        filename = scene_name.lower().replace(" ", "_").replace("(", "").replace(")", "")
        # Set the output filename in Manim's config
        config.output_file = filename
    
    scene = scene_class()
    scene.render()

def render_scene_parallel(scene_info: tuple[int, str, type[Scene]]) -> tuple[int, bool, str]:
    """Render a single scene in parallel and return its status.
    
    Args:
        scene_info: Tuple containing (scene_number, scene_name, scene_class)
    
    Returns:
        Tuple containing (scene_number, success, message)
    """
    num, name, scene_class = scene_info
    try:
        render_manim_scene(scene_class, name)
        return num, True, f"✓ Completed scene {num}: {name}"
    except Exception as e:
        return num, False, f"✗ Error rendering scene {num}: {str(e)}"

def render_all_scenes(parallel: bool = True) -> None:
    """Render all available Manim scenes in sequence or parallel.
    
    Args:
        parallel: Whether to render scenes in parallel (default: True)
    """
    print("\nRendering all scenes...")
    scenes = list_available_scenes()
    total_scenes = len(scenes)

    
    if parallel:
        print("\nRendering scenes in parallel...")
        with ThreadPoolExecutor(max_workers=4) as executor:
            # Submit all scenes for parallel rendering
            future_to_scene = {
                executor.submit(render_scene_parallel, scene_info): scene_info
                for scene_info in scenes
            }
            
            # Process completed scenes as they finish
            completed = 0
            for future in as_completed(future_to_scene):
                num, success, message = future.result()
                print(f"\n{message}")
                completed += 1
                if success:
                    print(f"Progress: {completed}/{total_scenes} scenes completed")
    else:
        print("\nRendering scenes sequentially...")
        for i, (num, name, scene_class) in enumerate(scenes, 1):
            print(f"\nRendering scene {i}/{total_scenes}: {name}")
            try:
                render_manim_scene(scene_class, name)
                print(f"✓ Completed scene {i}/{total_scenes}")
            except Exception as e:
                print(f"✗ Error rendering scene {i}/{total_scenes}: {str(e)}")
    
    print("\nAll scenes have been rendered!")
        
    # Print scene order information
    print("\nScene Order:")
    print("=" * 50)
    for num, name, _ in scenes:
        print(f"{num:2d}. {name}")
    print("=" * 50)

def list_available_scenes() -> list[tuple[int, str, type[Scene]]]:
    """List all available Manim scenes."""
    scenes = [
        # Core Concepts
        (1, "Introduction to Roots of Unity", IntroductionScene),
        (2, "Complex Root Visualization", ComplexRootVisualization),
        (3, "Nth Roots of Unity", NthRootsOfUnityScene),
        (4, "Polar Form Representation", PolarFormScene),
        (5, "Unity Properties & Sum/Product", UnityPropertiesScene),
        (6, "Primitive Root and Principal Root", PrimitiveRootScene),
        
        # Advanced Concepts
        (7, "Geometric Properties", GeometricPropertiesScene),
        (8, "Special Cases (Square, Cube, Fourth Roots)", SpecialCasesScene),
        
        # Additional Visualizations
        (9, "Specific Roots of Unity", SpecificRootsScene),
        (10, "Root Pattern Visualization", RootPatternScene),
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
        print("3. Render All Scenes (Parallel)")
        print("4. Render All Scenes (Sequential)")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
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
                selected_scene = next((scene for num, name, scene in scenes if num == scene_num), None)
                if selected_scene:
                    print(f"\nRendering scene {scene_num}...")
                    render_manim_scene(selected_scene, scenes[scene_num-1][1])
                else:
                    print("\nInvalid scene number!")
            except ValueError:
                print("\nInvalid input! Please enter a number.")
                
        elif choice == "2":
            render_slides()
            
        elif choice == "3":
            render_all_scenes(parallel=True)
            
        elif choice == "4":
            render_all_scenes(parallel=False)
            
        elif choice == "5":
            print("\nGoodbye!")
            sys.exit(0)
            
        else:
            print("\nInvalid choice! Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
