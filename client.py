# -*- coding: utf-8 -*-
"""
GenPark Quant Orderbook L2 Microstructure Imbalance Engine
Standard Library only: math, typing.
Calculates Level-2 order book depth metrics: Order Book Imbalance (OBI),
micro-price, VWAP execution slippage, and price impact estimation.
"""

import math
from typing import Dict, List, Tuple, Any

class GenParkQuantOrderbookL2MicrostructureImbalance:
    def evaluate_l2_snapshot(self, bids: List[Tuple[float, float]],
                             asks: List[Tuple[float, float]],
                             eval_levels: int = 5) -> Dict[str, Any]:
        """
        bids: list of (price, size) sorted desc by price
        asks: list of (price, size) sorted asc by price
        """
        if not bids or not asks:
            raise ValueError("Bids and asks must not be empty")

        best_bid, best_bid_sz = bids[0]
        best_ask, best_ask_sz = asks[0]

        if best_bid >= best_ask:
            raise ValueError("Crossed or locked book detected")

        mid_price = (best_bid + best_ask) / 2.0
        spread_bps = round(((best_ask - best_bid) / mid_price) * 10000, 2)

        # Micro-price: volume-weighted top-of-book price
        tot_top_sz = best_bid_sz + best_ask_sz
        micro_price = round(((best_bid_sz * best_ask) + (best_ask_sz * best_bid)) / tot_top_sz, 4)

        # Multi-level weighted OBI
        k = min(eval_levels, len(bids), len(asks))
        w_bid_vol = 0.0
        w_ask_vol = 0.0

        for i in range(k):
            weight = 1.0 / (i + 1)
            w_bid_vol += bids[i][1] * weight
            w_ask_vol += asks[i][1] * weight

        obi = (w_bid_vol - w_ask_vol) / max(1e-6, (w_bid_vol + w_ask_vol))

        # Order flow pressure classification
        pressure = "NEUTRAL"
        if obi >= 0.25: pressure = "BULLISH_BUY_PRESSURE"
        elif obi <= -0.25: pressure = "BEARISH_SELL_PRESSURE"

        return {
            "mid_price": round(mid_price, 4),
            "micro_price": micro_price,
            "spread_bps": spread_bps,
            "weighted_obi": round(obi, 4),
            "order_flow_pressure": pressure,
            "top_bid": {"price": best_bid, "size": best_bid_sz},
            "top_ask": {"price": best_ask, "size": best_ask_sz},
            "depth_levels_evaluated": k
        }

    def simulate_market_order_vwap(self, order_type: str, order_size: float,
                                    bids: List[Tuple[float, float]],
                                    asks: List[Tuple[float, float]]) -> Dict[str, Any]:
        """
        Simulates filling a market order through the L2 book and calculates VWAP slippage.
        """
        book = asks if order_type.lower() == "buy" else bids
        remaining = order_size
        cost = 0.0

        for price, size in book:
            fill_sz = min(remaining, size)
            cost += fill_sz * price
            remaining -= fill_sz
            if remaining <= 1e-6:
                break

        if remaining > 1e-6:
            return {"filled": False, "remaining_size": round(remaining, 4), "reason": "Insufficient liquidity"}

        vwap = cost / order_size
        best_price = book[0][0]
        slippage_bps = round((abs(vwap - best_price) / best_price) * 10000, 2)

        return {
            "filled": True,
            "order_type": order_type.upper(),
            "order_size": order_size,
            "vwap_execution_price": round(vwap, 4),
            "initial_best_price": best_price,
            "slippage_bps": slippage_bps,
            "total_notional": round(cost, 2)
        }
