import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.gui import run_app

if __name__ == "__main__":
    run_app()
