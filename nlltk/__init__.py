# nlltk/__init__.py

import os, shutil, pkg_resources
from IPython.display import IFrame

# === Path Utilities ===
def get_install_path():
    """Return the installation path of nlltk package."""
    import nlltk
    return os.path.dirname(nlltk.__file__)

# === PDF Access Utilities ===
def get_pdf(filename, destination="."):
    """Copy a packaged PDF to the specified destination."""
    src = pkg_resources.resource_filename("nlltk", f"data/{filename}")
    shutil.copy(src, os.path.join(destination, filename))
    print(f"✅ '{filename}' copied to {destination}")
    print(f"📁 Source: {src}")

def show_pdf(filename):
    """Display a packaged PDF inline in Jupyter Notebook."""
    path = pkg_resources.resource_filename("nlltk", f"data/{filename}")
    return IFrame(path, width=800, height=600)
