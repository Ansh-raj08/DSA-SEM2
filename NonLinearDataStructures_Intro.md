# Non-Linear Data Structures: Introduction

## What Are Non-Linear Data Structures?
Non-linear data structures are structures where data elements are not arranged in a single sequence.
Each element can be connected to one or many other elements.

In a linear structure, each item usually has one predecessor and one successor.
In a non-linear structure, relationships can be hierarchical or network-based.

## Common Non-Linear Data Structures
1. Trees
2. Graphs
3. Heaps
4. Hash Tables

## Why They Are Important
- Trees are used for hierarchical data like folders and organization charts.
- Graphs are used for networks like maps and social media connections.
- Heaps are used for priority-based processing.
- Hash tables are used for fast lookup operations.

## Introductory Questions and Solutions

### Question 1
What is the main difference between a linear and a non-linear data structure?

Solution:
In a linear data structure, elements are arranged in a sequence, one after another.
In a non-linear data structure, elements are connected in multiple possible paths, such as parent-child or network links.

### Question 2
How many edges are there in a tree with `n` nodes?

Solution:
A tree with `n` nodes has `n - 1` edges.

### Question 3
Which traversal of a tree visits nodes level by level?

Solution:
Level Order Traversal (Breadth-First Search, BFS) visits nodes level by level.

### Question 4
Which data structure is most suitable for representing a road map with cities and roads?

Solution:
A graph is most suitable.
Cities can be represented as vertices, and roads as edges.

### Question 5
Write a simple Python function for preorder traversal of a binary tree.

Solution:
```python
def preorder(node):
    if node is None:
        return
    print(node.data, end=" ")
    preorder(node.left)
    preorder(node.right)
```

Preorder traversal order is:
1. Root
2. Left subtree
3. Right subtree

## Quick Recap
- Non-linear structures model complex relationships.
- Trees and graphs are the most common types.
- BFS, DFS, and tree traversals are key concepts to practice.