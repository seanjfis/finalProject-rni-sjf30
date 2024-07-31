# finalProject-rni-sjf30
Final Project for Math 260 - Ryan Iki, Sean Fiscus

## Overview

This project aims to detect potential arbitrage opportunities in currency exchange rates using the Bellman-Ford algorithm. It contains Python code for detecting negative cost cycles in currency exchange rates, which can indicate profitable arbitrage opportunities.

## Files

1. **p3currencies.py** - Contains the `Currencies` class, which handles currency exchange rates, adjacency lists, and matrices. It also includes methods to print information and detect arbitrage opportunities.

2. **p3vertex.py** - Defines the `Vertex` class used for representing vertices in the graph of currencies.

3. **project3.py** - Includes the functions `detectArbitrage` and `rates2mat`. `detectArbitrage` detects negative cost cycles in the graph, and `rates2mat` converts exchange rates to an adjacency matrix with correctly weighted edges.

4. **p2tests.py** - Contains test cases for checking the correctness of exchange rate implementations and arbitrage detection.

## Getting Started

### Requirements

- Python 3.x

### Running the Code

1. Ensure all the files (`p3currencies.py`, `p3vertex.py`, `project3.py`, `p2tests.py`) are in the same directory.

2. Run the test script to verify the implementation:

   ```bash
   python p2tests.py
