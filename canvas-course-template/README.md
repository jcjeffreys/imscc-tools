# Canvas Course Template with CSS Styling System

This is a **comprehensive Canvas course template** featuring a complete CSS styling system with extensive documentation. Perfect for creating professional, consistently-styled Canvas courses.

## ✨ What's Included

### 🎨 Complete CSS Styling System
- **Comprehensive Stylesheet** (`css/canvas-course.css`) with 40+ styled components
- **Three Complete Styling Guides** demonstrating all available CSS classes:
  - **Guide 1:** General & Specific Styles (typography, boxes, tables, buttons, badges)
  - **Guide 2:** Interactive Elements (accordions and tabs)
  - **Guide 3:** Complete Lesson Example (production-ready Python lesson)

### 📚 Template Content
- **Welcome Page** - Customizable course home page with banner
- **Example Lesson** - Demonstration of course content structure
- **Assignment Template** - With priority badges and styled components
- **Comprehensive Quiz** - All 12 Canvas question types
- **Detailed Rubric** - 5 criteria with 5 rating levels

### 🎯 Key Features
- Full HTML document support for local preview
- Automatic CSS inlining on export
- File and page link conversion
- Priority badge system (MoSCoW method)
- Contextual emoji integration
- Canvas native tabs support

**To remove templates:** Delete all files containing `_TEMPLATE` when you're ready to add your own content.

## 📁 Folder Structure

```
canvas-course-template/
├── css/
│   └── canvas-course.css                    # Complete styling system (698 lines)
├── wiki_content/                            # HTML pages for your course
│   ├── welcome_TEMPLATE.html                # Home page with customizable banner
│   ├── styling-guide-1-styles_TEMPLATE.html          # Guide: General & Specific Styles
│   ├── styling-guide-2-interactive_TEMPLATE.html     # Guide: Interactive Elements
│   ├── styling-guide-3-example_TEMPLATE.html         # Guide: Complete Lesson Example
├── web_resources/                           # Files (PDFs, images, documents)
│   ├── syllabus_TEMPLATE.txt                # Example syllabus
│   ├── week1-reading_TEMPLATE.txt           # Example reading material
│   └── resources_TEMPLATE.txt               # Example resources
├── quizzes/                                 # Quiz definitions (JSON)
│   └── comprehensive-quiz_TEMPLATE.json     # All 12 question types
├── assignments/                             # Assignment definitions (JSON)
│   ├── comprehensive-assignment_TEMPLATE.html    # Assignment description
│   └── comprehensive-assignment_TEMPLATE.json    # Assignment settings
├── rubrics/                                 # Rubrics (JSON format)
│   └── comprehensive-rubric_TEMPLATE.json   # 5 criteria, 5 ratings each
├── course.json                              # Course metadata
├── modules.json                             # Module organization
└── README.md                                # This file
```

## 🚀 Working Locally

1. **Edit pages**: Open HTML files in `wiki_content/` with your favorite editor
2. **Preview**: Open HTML files directly in your browser - all links work locally!
3. **Add files**: Place PDFs, images, etc. in `web_resources/`
4. **Create content**: Add quizzes, assignments, and rubrics as JSON files
5. **Organize**: Update `modules.json` to organize all content into modules

## 🎨 CSS Styling System

The template includes a comprehensive CSS framework with 40+ styled components:

### Component Categories
- **Task Boxes:** Practice (blue), Portfolio (purple), Quiz (teal/mint)
- **Info Boxes:** Learning Goals, Key Concepts, Tips, Notes, Summaries
- **Example Boxes:** Good (green dashed), Bad (red dashed)
- **Priority Badges:** MUST (⭐ yellow), SHOULD (➕ orange), COULD (💎 red)
- **Interactive:** Accordions (default + styled), Canvas native tabs
- **Standard Elements:** Tables, blockquotes, buttons, typography

### How to Use Styles

Write your pages as **full HTML documents** for local preview:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="../css/canvas-course.css">
</head>
<body>
    <!-- Your content with CSS classes -->
    <div class="info-tip">
        <h3>💡 Tip</h3>
        <p>Your content here</p>
    </div>
</body>
</html>
```

**On export**, the build script automatically:
1. Inlines all CSS as style attributes
2. Removes `<link>` tags and document structure (DOCTYPE, html, head, body tags)
3. Converts file and page links to Canvas format
4. Keeps only the styled content for Canvas

### Page Metadata

Add optional metadata in HTML comments at the top:

```html
<!-- CANVAS_META
title: My Page Title
home: true
-->
```

**Supported Options:**
- `title`: Page title (defaults to filename)
- `home`: Set to `true` to make this the course home page

## 🔗 Linking

### Link to files:
```html
<a href="../web_resources/syllabus.txt">Syllabus</a>
```

### Link to other pages:
```html
<a href="lesson-1.html">Go to Lesson 1</a>
```

These links work locally for preview. When you export to IMSCC, they're automatically
converted to Canvas format.

## Export to IMSCC

When ready to upload to Canvas:

```bash
python3 build_from_template.py canvas-course-template
```

This will create `COURSE101.imscc` that you can import into Canvas.

## 📊 Quizzes

Create quiz files in `quizzes/` using JSON format. The template includes a comprehensive example with **all 12 question types**:

### Question Types Supported:
1. **`multiple_choice`** - One correct answer from multiple options
2. **`true_false`** - Simple true or false question
3. **`fill_in_blank`** - Short text answer (exact match)
4. **`fill_in_multiple_blanks`** - Multiple blanks with different answers
5. **`multiple_answers`** - Select all correct answers (checkboxes)
6. **`multiple_dropdowns`** - Multiple dropdown menus in text
7. **`matching`** - Match items between two columns
8. **`numerical_answer`** - Numeric answer with tolerance/range
9. **`formula_question`** - Calculated question with variables
10. **`essay_question`** - Long-form text response (manual grading)
11. **`file_upload_question`** - File submission (manual grading)
12. **`text_only_question`** - Informational text (0 points)

See `comprehensive-quiz_TEMPLATE.json` for examples of each type!

### Quiz Settings:
```json
{
  "title": "My Quiz",
  "description": "<p>Quiz description</p>",
  "settings": {
    "quiz_type": "assignment",
    "allowed_attempts": 2,
    "time_limit": 30,
    "shuffle_questions": true,
    "shuffle_answers": true,
    "show_correct_answers": true,
    "one_question_at_a_time": false,
    "cant_go_back": false,
    "scoring_policy": "keep_highest"
  },
  "questions": [...]
}
```

## 📋 Assignments

Create assignment files in `assignments/` using JSON format:

```json
{
  "title": "Assignment Title",
  "description": "<p>Assignment instructions</p>",
  "points_possible": 100,
  "submission_types": ["online_upload", "online_text_entry"],
  "allowed_extensions": [".pdf", ".doc", ".docx"],
  "grading_type": "points",
  "assignment_group": "Assignments",
  "rubric": "rubric-filename"
}
```

**Submission Types:** `online_upload`, `online_text_entry`, `online_url`, `media_recording`

## 📏 Rubrics

Create rubrics in `rubrics/` as JSON files. The template includes a detailed example with 5 criteria and 5 rating levels each:

```json
{
  "title": "Rubric Title",
  "criteria": [
    {
      "description": "Criterion Name",
      "long_description": "Detailed description of what this criterion evaluates",
      "points": 25,
      "ratings": [
        {
          "description": "Exemplary",
          "long_description": "Detailed description of exemplary performance",
          "points": 25
        },
        {
          "description": "Proficient",
          "long_description": "Detailed description of proficient performance",
          "points": 20
        }
      ]
    }
  ]
}
```

**Note:** Both criteria and ratings support `long_description` for detailed feedback guidance.

## 📚 Module Organization

Edit `modules.json` to organize all content types into modules:

```json
{
  "modules": [
    {
      "title": "Week 1",
      "items": [
        {"type": "page", "id": "welcome"},
        {"type": "page", "id": "lesson-1"},
        {"type": "quiz", "id": "week-1-quiz"},
        {"type": "assignment", "id": "homework-1"}
      ]
    }
  ]
}
```

**Content Types:** `page`, `quiz`, `assignment`  
**IDs:** Match filenames without extensions (e.g., `welcome_TEMPLATE.html` → `"id": "welcome_TEMPLATE"`)

## 🔨 Export to IMSCC

When ready to upload to Canvas:

```bash
python3 build_from_template.py canvas-course-template
```

This will create `COURSE101.imscc` that you can import into Canvas.

## 🎓 Learning the Styling System

**Start with the Styling Guides** - they demonstrate every available CSS class:

1. **styling-guide-1-styles.html** - All basic components, boxes, tables, buttons, badges
2. **styling-guide-2-interactive.html** - Accordions and tabs with styling variations
3. **styling-guide-3-example.html** - Complete production lesson showing everything together

These guides work locally in your browser and include detailed explanations of each component.

## 💡 Tips

1. **Preview locally**: Write full HTML documents with `<link>` tags - preview in browser before exporting
2. **Study the guides**: Open the three styling guides to see all available CSS classes
3. **Copy examples**: The styling guides include copy-ready code for every component
4. **Customize banners**: Use inline styles for course-specific elements (like the welcome banner)
5. **Use priority badges**: Help students prioritize with MoSCoW method (MUST/SHOULD/COULD)
6. **Emoji integration**: Each component type has suggested contextual emojis
7. **Easy cleanup**: Delete all `_TEMPLATE` files when ready to add your content
8. **Comprehensive quiz**: Check the quiz file to see all 12 question types in action

## 🚀 Quick Start

1. Open `wiki_content/welcome_TEMPLATE.html` in your browser to see the welcome page
2. Explore the three styling guides to learn available components
3. Edit HTML files to create your course content
4. Run `python3 build_from_template.py canvas-course-template` to export to IMSCC
5. Import the `.imscc` file into Canvas
