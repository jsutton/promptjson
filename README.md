
# PromptJSON Documentation

## Overview
PromptJSON is a JSON-based language designed for crafting structured prompts for image generation models. It offers a standardized way to specify image details, enhancing compatibility and image quality.

NOTE: This is primarily intended as a thought experiment, but if it is useful to you feel free to use or submit PRs.

## Schema Details

### 1. Scene
- **Type**: String
- **Description**: Description of the image setting or environment.
- **Required**: Yes

### 2. Subjects
- **Type**: Object
- **Description**: Specifies main and secondary subjects in the image.
- **Properties**:
  - **Main**: Array of strings for primary subjects.
  - **Secondary**: Array of strings for secondary subjects.
- **Required**: Yes

### 3. Attributes
- **Type**: Object
- **Description**: Artistic attributes of the image.
- **Properties**:
  - **Style**: String for artistic style.
  - **Mood**: String for mood of the image.
  - **ColorScheme**: String for primary colors.

### 4. Constraints
- **Type**: Object
- **Description**: Specific requirements for the image.
- **Properties**:
  - **Dimensions**: String for size (e.g., "1024x768").
  - **AspectRatio**: String for aspect ratio (e.g., "16:9").

### 5. Options
- **Type**: Object
- **Description**: Additional optional settings for nuanced control.
- **Properties**: Flexible for any additional parameters.

## Examples

### Example 1: Simple Landscape
```json
{
  "Scene": "A tranquil mountain range at sunset",
  "Subjects": {
    "Main": ["mountains"],
    "Secondary": ["lake", "forest"]
  },
  "Attributes": {
    "Style": "realistic",
    "Mood": "peaceful",
    "ColorScheme": "warm colors"
  },
  "Constraints": {
    "Dimensions": "1920x1080"
  }
}
```

### Example 2: Portrait of a Person
```json
{
  "Scene": "Elegant portrait of a person in a Victorian setting",
  "Subjects": {
    "Main": ["person"],
    "Secondary": ["vintage armchair", "ornate wallpaper"]
  },
  "Attributes": {
    "Style": "classical painting",
    "Mood": "sophisticated",
    "ColorScheme": "rich, muted colors"
  },
  "Constraints": {
    "Dimensions": "800x1000",
    "AspectRatio": "4:5"
  },
  "Options": {
    "PersonDetails": {
      "Gender": "female",
      "Age": "early 30s",
      "Clothing": "Victorian dress",
      "Expression": "thoughtful"
    },
    "Lighting": "soft, from the left"
  }
}
```

## Usage
To validate a PromptJSON file, run the `promptscript_validator.py` script with the JSON file as an argument:
```bash
python promptscript_validator.py <file_to_validate.json>
```
Ensure that your PromptJSON file adheres to the schema and is correctly formatted before using it as input for your image generation model.

---