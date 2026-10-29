# genpark-quant-orderbook-l2-microstructure-imbalance-skill

[![Organization](https://img.shields.io/badge/AlphaPark-OpenSource-blue.svg)](https://github.com/alphaparkinc)
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard-orange.svg)](https://modelcontextprotocol.io)
[![Zero-Dependency](https://img.shields.io/badge/Dependencies-Zero_External-brightgreen.svg)](#)
[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](#)
[![Domain](https://img.shields.io/badge/Domain-AI_Quant_%26_DeFi-gold.svg)](#)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Production-grade Quantitative Finance & DeFi Microstructure skill engineered strictly with Python standard library. Provides real-time concentrated liquidity optimization, L2 orderbook imbalance metrics, negative-cycle triangular arbitrage detection, and Bayesian Black-Litterman portfolio rebalancing via the Model Context Protocol (MCP).

---

## Architecture & Data Flow

```mermaid
flowchart TD
    MarketFeed[L2 Tick / Orderbook / Exchange Rate Matrix / Covariance] --> Normalizer[Data Normalizer]
    Normalizer --> Core["GenParkQuantOrderbookL2MicrostructureImbalance"]
    Core --> Analytics[Microstructure & Optimization Engine]
    Analytics --> RiskGuard[Slippage & Drawdown Constraints]
    RiskGuard --> MCPOutput[Standard MCP Tool Result / Execution Vector]
```

---

## Quickstart & Usage

### 1. Direct Python Client Execution
```bash
python example_usage.py
```

### 2. Standalone MCP Server Launch
Run the native STDIO MCP server:
```bash
python mcp_server.py
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
