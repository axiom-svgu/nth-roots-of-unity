import markdown
import os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

class SlideGenerator:
    def __init__(self, slides_dir="slides/content", template_dir="slides/templates", output_dir="slides/output"):
        self.slides_dir = Path(slides_dir)
        self.template_dir = Path(template_dir)
        self.output_dir = Path(output_dir)
        self.env = Environment(loader=FileSystemLoader(str(self.template_dir)))
        
        # Create necessary directories
        for directory in [self.slides_dir, self.template_dir, self.output_dir]:
            directory.mkdir(exist_ok=True, parents=True)
    
    def generate_slides(self):
        """Generate HTML slides from markdown files."""
        template = self.env.get_template("presentation.html")
        slides_content = []
        
        # Read all markdown files in order
        for md_file in sorted(self.slides_dir.glob("*.md")):
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                html = markdown.markdown(content, extensions=['extra', 'codehilite'])
                slides_content.append(html)
        
        # Generate the presentation
        presentation = template.render(slides=slides_content)
        
        # Write the output
        output_file = self.output_dir / "presentation.html"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(presentation)
        
        print(f"Presentation generated at {output_file}")

if __name__ == "__main__":
    generator = SlideGenerator()
    generator.generate_slides() 