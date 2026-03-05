import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app


def test_header_present():
    layout = app.layout

    headers = [component for component in layout.children if component.__class__.__name__ == "H1"]

    assert len(headers) > 0


def test_graph_present():
    layout = app.layout

    graphs = [component for component in layout.children if component.__class__.__name__ == "Graph"]

    assert len(graphs) > 0


def test_region_picker_present():
    layout = app.layout

    radio = [component for component in layout.children if component.__class__.__name__ == "RadioItems"]

    assert len(radio) > 0