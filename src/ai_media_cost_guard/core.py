"""Pre-flight credit & USD cost simulator and budget gate for generative media agents."""

from __future__ import annotations

from dataclasses import asdict, dataclass

DEFAULT_RATES_CREDITS: dict[str, float] = {
    "image_standard": 10.0,
    "image_upscale_4k": 25.0,
    "video_5s_1080p": 120.0,
    "video_10s_1080p": 240.0,
    "tts_per_1k_chars": 15.0,
    "model_3d_mesh": 80.0,
}


@dataclass(frozen=True)
class CostQuote:
    operation: str
    units: float
    credits_required: float
    usd_annual_rate: float
    usd_monthly_rate: float
    current_credits: float
    projected_remaining_credits: float
    within_budget: bool
    requires_explicit_approval: bool

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def simulate_generation_cost(
    operation: str,
    units: float = 1.0,
    current_credits: float = 10_000.0,
    max_usd_per_call: float = 2.00,
    usd_per_credit_annual: float = 0.00075,
    usd_per_credit_monthly: float = 0.00100,
) -> CostQuote:
    if operation not in DEFAULT_RATES_CREDITS:
        raise ValueError(f"Unknown operation '{operation}'. Supported: {', '.join(DEFAULT_RATES_CREDITS)}")
    if units <= 0:
        raise ValueError("units must be positive.")

    credits = round(DEFAULT_RATES_CREDITS[operation] * units, 2)
    usd_ann = round(credits * usd_per_credit_annual, 4)
    usd_mon = round(credits * usd_per_credit_monthly, 4)
    remaining = round(current_credits - credits, 2)
    within = remaining >= 0 and usd_mon <= max_usd_per_call
    return CostQuote(
        operation=operation,
        units=units,
        credits_required=credits,
        usd_annual_rate=usd_ann,
        usd_monthly_rate=usd_mon,
        current_credits=current_credits,
        projected_remaining_credits=remaining,
        within_budget=within,
        requires_explicit_approval=True,
    )
