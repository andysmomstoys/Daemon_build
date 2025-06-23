
SPECIALTIES = {
    "software": "Trained in Python, Rust, and Julia development.",
    "mechanical_engineering": "CAD integration, design, and AI control logic.",
    "philosophy": "Symbolic logic, ethical evaluation, and debate.",
    "video_editing": "Script-based video pipelines.",
    "3d_animation": "Scene generation with Blender hooks.",
    "3d_modeling": "Procedural model generation tools.",
    "storytelling": "Narrative engine for mythic and symbolic arc development."
}

def describe_specialty(name):
    return SPECIALTIES.get(name, "Unknown specialty")
