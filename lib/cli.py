import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from helpers import EventPlanner
import fire

if __name__ == "__main__":
    fire.Fire(EventPlanner)
