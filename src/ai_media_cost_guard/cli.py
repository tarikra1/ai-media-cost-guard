"""CLI for ai-media-cost-guard."""

from __future__ import annotations

import argparse
import json

from .core import DEFAULT_RATES_CREDITS, simulate_generation_cost


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="cost-guard", description="Simulate generative media credits and USD cost before execution.")
    parser.add_argument("operation", choices=sorted(DEFAULT_RATES_CREDITS.keys()))
    parser.add_argument("--units", type=float, default=1.0, help="Quantity/batches to generate.")
    parser.add_argument("--balance", type=float, default=10000.0, help="Current available credit balance.")
    parser.add_argument("--max-usd", type=float, default=2.0, help="Maximum allowed USD per call.")
    args = parser.parse_args(argv)

    quote = simulate_generation_cost(
        operation=args.operation,
        units=args.units,
        current_credits=args.balance,
        max_usd_per_call=args.max_usd,
    )
    print(json.dumps(quote.to_dict(), indent=2))
    return 0 if quote.within_budget else 2


if __name__ == "__main__":
    raise SystemExit(main())
