import os

# ------------------------------
# 1. PROJECT STRUCTURE DEFINITION
# ------------------------------
structure = {
    "glearn": {
        "__init__.py": "",
        "core": {
            "__init__.py": "",
            "utils.py": ""
        },
        "models": {
            "__init__.py": "",
            "linear_regression.py": ""
        },
        "preprocessing": {
            "__init__.py": "",
            "standard_scaler.py": ""
        }
    },
    "tests": {},
    "examples": {},
    "README.md": ""
}

# ------------------------------
# 2. FUNCTION TO CREATE STRUCTURE
# ------------------------------
def create_structure(base_path, struct):
    for name, content in struct.items():
        path = os.path.join(base_path, name)

        if isinstance(content, dict):
            # Create folder
            os.makedirs(path, exist_ok=True)
            # Recursively build inside it
            create_structure(path, content)
        else:
            # Create file with content
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

# ------------------------------
# 3. GENERATE TREE FOR README
# ------------------------------
def generate_tree(path, prefix=""):
    tree_str = ""
    items = sorted(os.listdir(path))

    for i, item in enumerate(items):
        full_path = os.path.join(path, item)
        connector = "└── " if i == len(items) - 1 else "├── "
        tree_str += prefix + connector + item + "\n"

        if os.path.isdir(full_path):
            extension = "    " if i == len(items) - 1 else "│   "
            tree_str += generate_tree(full_path, prefix + extension)

    return tree_str


# ------------------------------
# 4. MAIN EXECUTION
# ------------------------------
if __name__ == "__main__":
    base_path = os.getcwd()

    print("\n🚀 Creating G-Learn project structure...\n")
    create_structure(base_path, structure)

    print("📁 Folder structure created. Updating README.md ...")

    # Generate folder tree
    tree = generate_tree(base_path)

    readme_path = os.path.join(base_path, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("# G-Learn\n")
        f.write("A lightweight machine learning library implemented from scratch.\n\n")
        f.write("## 📂 Project Structure\n")
        f.write("```\n" + tree + "\n```\n")

    print("\n✅ README.md updated automatically!")
    print("✅ Setup complete!\n")
