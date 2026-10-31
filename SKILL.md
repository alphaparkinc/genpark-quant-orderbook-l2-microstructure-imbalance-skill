---
name: genpark-quant-orderbook-l2-microstructure-imbalance-skill
description: Quant orderbook L2 microstructure imbalance engine computing weighted OBI, micro-price, and market order VWAP execution slippage.
category: Service
version: 1.0.0
license: MIT
tools:
  - {'name': 'evaluate_l2_snapshot', 'description': 'Calculate order book imbalance and micro-price metrics from L2 snapshot.'}
  - {'name': 'simulate_market_order_vwap', 'description': 'Simulate multi-level market order walk and compute VWAP slippage.'}
---

# Genpark Quant Orderbook L2 Microstructure Imbalance Skill

## Overview & Agent Behavioral Directives
You are an autonomous agent specialized in **Genpark Quant Orderbook L2 Microstructure Imbalance Skill**.
Your primary directive is to execute: Quant orderbook L2 microstructure imbalance engine computing weighted OBI, micro-price, and market order VWAP execution slippage.
Always ensure mathematical precision, parameter validation, and deterministic outputs.

## When to Activate This Skill
- Activate when an agent workflow or user instruction requires:
- `{'name': 'evaluate_l2_snapshot', 'description': 'Calculate order book imbalance and micro-price metrics from L2 snapshot.'}`
- `{'name': 'simulate_market_order_vwap', 'description': 'Simulate multi-level market order walk and compute VWAP slippage.'}`
- Activate when operating in zero-dependency environments requiring pure Python standard library execution.

## How to Execute

### Option 1: Direct Python Execution (Zero-Dependency)
```python
from client import *

# Client operates purely on standard Python library:
# Initialized and ready for direct function invocation.
```

### Option 2: FastMCP Tool Calling
Tools registered in `mcp_server.py`:
- `{'name': 'evaluate_l2_snapshot', 'description': 'Calculate order book imbalance and micro-price metrics from L2 snapshot.'}`
- `{'name': 'simulate_market_order_vwap', 'description': 'Simulate multi-level market order walk and compute VWAP slippage.'}`

## Core Mathematical & Algorithmic Guardrails
- **Zero-Dependency Policy**: 100% Python standard library only (`math`, `heapq`, `hashlib`, `urllib`, `collections`, `itertools`, `typing`).
- **Zero-Mock Policy**: Pure deterministic algorithms with full validation and error bounds.
