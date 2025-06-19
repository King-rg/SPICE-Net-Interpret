import argparse
import re
from graphviz import Digraph


def parse_netlist(text):
    components = {}
    nets = set()
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith('*') or line.startswith(';'):
            continue
        if line.lower().startswith('.end'):
            break
        if line.startswith('.'):  # directive
            continue
        tokens = re.split(r'\s+', line)
        if len(tokens) < 3:
            continue
        name = tokens[0]
        node_tokens = tokens[1:3]
        nets.update(node_tokens)
        components[name] = node_tokens
    return components, nets


def build_graph(components):
    dot = Digraph()
    dot.attr('node', shape='box')
    for comp, nodes in components.items():
        dot.node(comp)
        for node in nodes:
            net_node = f"net_{node}"
            dot.node(net_node, label=node, shape='ellipse')
            dot.edge(comp, net_node)
    return dot


def main():
    parser = argparse.ArgumentParser(description='Convert SPICE .cir netlist to flowchart (graphviz dot).')
    parser.add_argument('input', help='Path to .cir netlist file')
    parser.add_argument('output', nargs='?', help='Output dot file path (optional)')
    args = parser.parse_args()
    with open(args.input) as f:
        text = f.read()
    components, nets = parse_netlist(text)
    dot = build_graph(components)
    if args.output:
        dot.save(args.output)
    else:
        print(dot.source)

if __name__ == '__main__':
    main()
