# -*- coding: utf-8 -*-
from client import GenParkQuantOrderbookL2MicrostructureImbalance

def main():
    engine = GenParkQuantOrderbookL2MicrostructureImbalance()
    print("=== GenPark Quant L2 Orderbook Microstructure Imbalance ===")

    # Simulated orderbook snapshot for SOL/USDC
    bids = [(145.20, 150.0), (145.15, 300.0), (145.10, 500.0)]
    asks = [(145.25, 40.0), (145.30, 80.0), (145.35, 120.0)]

    metrics = engine.evaluate_l2_snapshot(bids, asks)
    print(f"Mid-Price: ${metrics['mid_price']}, Micro-Price: ${metrics['micro_price']}")
    print(f"Spread: {metrics['spread_bps']} bps, Weighted OBI: {metrics['weighted_obi']}")
    print(f"Order Flow Signal: {metrics['order_flow_pressure']}")

    # Simulate $10,000 buy market order (approx 68.8 SOL)
    sim = engine.simulate_market_order_vwap("buy", order_size=68.8, bids=bids, asks=asks)
    print()
    print(f"Simulated Buy Fill: VWAP=${sim['vwap_execution_price']}, Slippage={sim['slippage_bps']} bps")

if __name__ == "__main__":
    main()
