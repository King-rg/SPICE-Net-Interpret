# SPICE-Net-Interpret

This repository provides a simple Python script to parse a SPICE `.cir` netlist and generate a Graphviz flowchart of the circuit connections.

## Usage

```bash
pip install graphviz
python3 cir_to_flowchart.py example.cir output.dot
```

If no output path is given, the DOT representation is printed to standard output. Use Graphviz to render the DOT file to an image, e.g. `dot -Tpng output.dot -o output.png`.
