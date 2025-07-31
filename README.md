# RiskRadarSystem Architecture Diagram

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://python.org)
[![Graphviz Required](https://img.shields.io/badge/requires-Graphviz-orange)](https://graphviz.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

![RiskRadarSystem Architecture](RiskRadarSystem_Architecture.png)

## Description

This repository contains a Python script that generates a detailed architecture diagram for a RiskRadarSystem using Graphviz. The diagram illustrates the data flow and modular components of a computer vision-based risk assessment system.

## Key Components

- **Perception Module**: Handles frame processing, object detection (using YOLO), tracking (CSRT), and distance mapping (MiDaS)
- **Risk Analysis Module**: Processes detections to calculate risk levels using heatmaps
- **Output Module**: Visualizes results and generates reports

## Features

- Detailed flow diagram with decision points
- Modular architecture with clear separation of concerns
- Persistent state components (distance map and heatmap)
- Conditional execution paths

## Requirements

- Python 3.6+
- Graphviz (must be installed and in system PATH)
- `graphviz` Python package

## Installation

```bash
pip install graphviz
```

## Usage

Simply run the script to generate the diagram:

```bash
python RiskRadarSystem_architecture.py
```

The script will generate:
- `RiskRadarSystem_Architecture.png` - The visualization
- `RiskRadarSystem_Architecture` - Graphviz source file

## Technical Details

- Uses orthogonal edges for clean layout
- Color-coded nodes for different component types
- Subgraphs to represent system modules
- Diamond nodes for decision points
- Cylinder nodes for persistent data stores

## Troubleshooting

If you encounter errors:
1. Verify Graphviz is installed (`dot -V` in terminal)
2. Ensure Graphviz binaries are in your system PATH
3. Check Python graphviz package is installed

## License

MIT License - See [LICENSE](LICENSE) file for details.

---

*Diagram automatically generated using Python Graphviz*

