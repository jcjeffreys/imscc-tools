#!/usr/bin/env python3
"""
Create a template folder structure for working on Canvas course content locally.

Copies the comprehensive canvas-course-template with CSS styling system and modern features.

The template includes:
- Comprehensive CSS styling system (info boxes, task accordions, tabs, tables, etc.)
- Example pages demonstrating all styling features
- Quiz and assignment examples
- Proper folder structure for Canvas IMSCC export

Pages use HTML comments for metadata:
  <!-- CANVAS_META
  title: Page Title
  home: true
  -->

Links work locally and are converted to Canvas format during IMSCC export.
"""

import os
import json
import argparse
import shutil
from pathlib import Path


def create_template(output_dir):
    """Create a template folder structure by copying canvas-course-template."""
    output_path = Path(output_dir)
    
    if output_path.exists():
        print(f"❌ Error: Directory '{output_dir}' already exists!")
        print(f"   Please choose a different name or remove the existing directory.")
        return False
    
    # Find the template directory
    script_dir = Path(__file__).parent
    template_source = script_dir / "canvas-course-template"
    
    if not template_source.exists():
        print(f"❌ Error: Template directory not found at {template_source}")
        print(f"   Please ensure canvas-course-template exists in the imscc-tools directory.")
        return False
    
    print("\n" + "=" * 70)
    print(f"Creating Course Template: {output_dir}")
    print("=" * 70)
    print(f"\n📋 Copying from: {template_source}")
    
    # Copy the entire template directory
    print("\n📁 Copying template files...")
    try:
        shutil.copytree(template_source, output_path)
    except Exception as e:
        print(f"❌ Error copying template: {e}")
        return False
    
    # List what was copied
    print("\n✅ Copied structure:")
    for item in sorted(output_path.iterdir()):
        if item.is_dir():
            file_count = len(list(item.rglob('*.*')))
            print(f"   ✓ {item.name}/ ({file_count} files)")
        else:
            print(f"   ✓ {item.name}")
    
    # Update course.json with the new directory name
    course_json_path = output_path / "course.json"
    if course_json_path.exists():
        print("\n⚙️  Updating course.json...")
        try:
            with open(course_json_path, 'r', encoding='utf-8') as f:
                course_data = json.load(f)
            
            # Update title to match directory name
            course_data['title'] = output_dir.replace('-', ' ').replace('_', ' ').title()
            course_data['course_code'] = output_dir.upper()
            
            with open(course_json_path, 'w', encoding='utf-8') as f:
                json.dump(course_data, f, indent=2)
            
            print(f"   ✓ Updated title to: {course_data['title']}")
            print(f"   ✓ Updated course code to: {course_data['course_code']}")
        except Exception as e:
            print(f"   ⚠️  Could not update course.json: {e}")
    
    # Update README
    print("\n📖 Updating README...")
    readme_content = f"""# {output_dir.replace('-', ' ').replace('_', ' ').title()}

This Canvas course was created from the **canvas-course-template** with comprehensive CSS styling system.

## 🎨 CSS Styling System

This template includes a complete styling system for creating professional, visually appealing course content. All styles are defined in `css/canvas-course.css` and work seamlessly with Canvas LMS.

### Available Components:

**Info Boxes:**
- `info-learning-goals` - Cyan box for learning objectives
- `info-key-concept` - Indigo box for key concepts
- `info-tip` - Yellow box for helpful tips
- `info-note` - Orange box for important notes
- `info-summary` - Gray box for summaries

**Task Accordions:**
- `task-practice` - Blue accordion for practice exercises
- `task-portfolio` - Purple accordion for portfolio tasks
- `task-quiz` - Teal/mint accordion for quiz tasks

**Other Features:**
- Canvas native tabs with color themes
- Priority badges (MUST/SHOULD/COULD with MoSCoW method)
- Good/bad example boxes with dashed borders
- Styled tables and general accordions

See the styling guide pages for complete examples and usage.

## 📁 Folder Structure

```
{output_dir}/
├── wiki_content/                # HTML pages for your course
│   ├── welcome_TEMPLATE.html    # Home page with customizable banner
│   ├── styling-guide-*_TEMPLATE.html  # Documentation pages
│   └── ...
├── css/
│   └── canvas-course.css        # Complete styling system
├── web_resources/               # Files (PDFs, images, documents)
├── quizzes/                     # Quiz definitions (JSON)
├── assignments/                 # Assignment definitions (JSON)
├── rubrics/                     # Rubrics (JSON format)
├── course.json                  # Course metadata
├── modules.json                 # Module organization
└── README.md                    # This file
```

## 🚀 Working Locally

1. **Edit pages**: Open HTML files in `wiki_content/` with your favorite editor
2. **Preview**: Open HTML files directly in your browser - all links and styles work locally!
3. **Add files**: Place PDFs, images, etc. in `web_resources/`
4. **Create content**: Add quizzes, assignments, and rubrics as JSON files
5. **Organize**: Update `modules.json` to organize all content into modules

## 📄 Page Metadata

Each page can have metadata in HTML comments at the top:

```html
<!-- CANVAS_META
title: My Page Title
home: true
-->
```

Supported metadata:
- `title`: Page title (defaults to filename)
- `home`: Set to `true` to make this the course home page

## 🔗 Linking

### Link to files:
```html
<a href="../web_resources/syllabus.pdf">Syllabus</a>
```

### Link to other pages:
```html
<a href="lesson-1.html">Go to Lesson 1</a>
```

These links work locally for preview. When you export to IMSCC, they're automatically
converted to Canvas format.

## 📦 Export to IMSCC

When ready to upload to Canvas:

```bash
python build_from_template.py {output_dir}
```

This will create an `.imscc` file that you can import into Canvas.

## 🏷️ Template Files

All example files are tagged with `_TEMPLATE` in their filenames for easy identification:

- **Pages:** `welcome_TEMPLATE.html`, `styling-guide-*_TEMPLATE.html`
- **Quizzes:** `*_TEMPLATE.json`
- **Assignments:** `*_TEMPLATE.json` and `*_TEMPLATE.html`
- **Rubrics:** `*_TEMPLATE.json`

**To remove templates:** Delete all files containing `_TEMPLATE` when you're ready to add your own content.

## 📚 Next Steps

1. Open `wiki_content/welcome_TEMPLATE.html` in your browser to see the template
2. Review the styling guide pages to see all available CSS components
3. Customize the welcome page banner with your course colors
4. Replace template content with your own course materials
5. Delete `_TEMPLATE` files when ready
6. Build and import to Canvas

For complete documentation, see the styling guide pages in `wiki_content/`.
"""
    readme_path = output_path / "README.md"
    readme_path.write_text(readme_content, encoding='utf-8')
    print(f"   ✓ README.md")
    
    # Success message
    print("\n" + "=" * 70)
    print("✅ Template Created Successfully!")
    print("=" * 70)
    print(f"\n📂 Location: {output_path.absolute()}")
    print("\n✨ What's Included:")
    print("   • Comprehensive CSS styling system (canvas-course.css)")
    print("   • Welcome page with customizable banner (home page)")
    print("   • 3 styling guide pages demonstrating all features")
    print("   • Example quiz and assignment")
    print("   • Detailed rubric example")
    print("   • Configuration files (course.json, modules.json)")
    print("\n🎨 CSS Features:")
    print("   • Info boxes (learning-goals, key-concept, tip, note, summary)")
    print("   • Task accordions (practice, portfolio, quiz)")
    print("   • Canvas native tabs with color themes")
    print("   • Priority badges (MUST/SHOULD/COULD)")
    print("   • Good/bad example boxes")
    print("   • Styled tables and accordions")
    print("\n🏷️  All template files tagged with '_TEMPLATE' for easy identification")
    print("\n🚀 Next Steps:")
    print(f"   1. cd {output_dir}")
    print(f"   2. Open wiki_content/welcome_TEMPLATE.html in your browser")
    print(f"   3. Review the styling guides and examples")
    print(f"   4. Customize the welcome page banner and content")
    print(f"   5. Delete _TEMPLATE files and add your content")
    print(f"   6. Run: python build_from_template.py {output_dir}")
    print(f"   7. Import the generated IMSCC file into Canvas")
    print("\n💡 Tip: Check the styling guides for complete CSS component reference!\n")
    
    return True


def main():
    parser = argparse.ArgumentParser(
        description='Create a Canvas course template by copying canvas-course-template',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python create_template.py my-course
  python create_template.py biology-101
  python create_template.py year9-programming

The template includes:
  - Comprehensive CSS styling system (info boxes, task accordions, tabs)
  - Welcome page with customizable banner (set as home page)
  - 3 styling guide pages demonstrating all features
  - Example quiz, assignment, and rubric
  - Configuration files (course.json, modules.json)
  - Complete documentation
  
All example files are tagged with _TEMPLATE for easy identification and removal.
        """
    )
    
    parser.add_argument(
        'directory',
        help='Name of the directory to create'
    )
    
    args = parser.parse_args()
    
    create_template(args.directory)


if __name__ == '__main__':
    main()
