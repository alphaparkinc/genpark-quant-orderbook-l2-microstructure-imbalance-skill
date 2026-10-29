# -*- coding: utf-8 -*-
import sys, json
from client import GenParkQuantOrderbookL2MicrostructureImbalance

engine = GenParkQuantOrderbookL2MicrostructureImbalance()

def run_tool(name, args):
    if name == "evaluate_l2_snapshot":
        bids = [tuple(x) for x in args.get("bids", [])]
        asks = [tuple(x) for x in args.get("asks", [])]
        levels = int(args.get("eval_levels", 5))
        return engine.evaluate_l2_snapshot(bids, asks, levels)
    elif name == "simulate_market_order_vwap":
        otype = args.get("order_type", "buy")
        size = float(args.get("order_size", 1.0))
        bids = [tuple(x) for x in args.get("bids", [])]
        asks = [tuple(x) for x in args.get("asks", [])]
        return engine.simulate_market_order_vwap(otype, size, bids, asks)
    else:
        raise ValueError(f"Unknown tool: {name}")

def main():
    if "--test" in sys.argv:
        print("[TEST] Running GenPark L2 Microstructure Imbalance Self-Test...")
        bids = [(100.0, 5.0), (99.5, 10.0), (99.0, 20.0)]
        asks = [(100.5, 2.0), (101.0, 4.0), (101.5, 8.0)]
        res = engine.evaluate_l2_snapshot(bids, asks)
        assert res["mid_price"] == 100.25
        assert res["weighted_obi"] > 0.0 # Bids heavier
        sim = engine.simulate_market_order_vwap("buy", 3.0, bids, asks)
        assert sim["filled"] is True
        print("[TEST] All tests passed successfully!")
        return

    for line in sys.stdin:
        if not line.strip(): continue
        try:
            req = json.loads(line)
            res = run_tool(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"jsonrpc": "2.0", "id": req.get("id"), "result": res}))
        except Exception as e:
            print(json.dumps({"jsonrpc": "2.0", "id": None, "error": {"code": -32603, "message": str(e)}}))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
