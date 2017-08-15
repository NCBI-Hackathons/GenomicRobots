import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

if __package__ is None:
    import genomicrobots
    __package__ = "genomicrobots"

from .config import development as conf
from .webapp import create_app
from .manage import get_command_manager

app = create_app(conf)
manager = get_command_manager(app)
print("APP", manager)

if __name__ == '__main__':
    manager.run()
