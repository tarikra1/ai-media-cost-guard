import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import unittest

from ai_media_cost_guard.core import simulate_generation_cost


class TestAiMediaCostGuard(unittest.TestCase):
    def test_quote_calculation_and_budget_pass(self) -> None:
        q = simulate_generation_cost("video_5s_1080p", units=2, current_credits=5000, max_usd_per_call=1.0)
        self.assertEqual(q.credits_required, 240.0)
        self.assertAlmostEqual(q.usd_annual_rate, 0.18, places=4)
        self.assertAlmostEqual(q.usd_monthly_rate, 0.24, places=4)
        self.assertEqual(q.projected_remaining_credits, 4760.0)
        self.assertTrue(q.within_budget)
        self.assertTrue(q.requires_explicit_approval)

    def test_exceeding_max_usd_flags_over_budget(self) -> None:
        q = simulate_generation_cost("video_10s_1080p", units=15, current_credits=5000, max_usd_per_call=1.0)
        self.assertFalse(q.within_budget)


if __name__ == "__main__":
    unittest.main()
