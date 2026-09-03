# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BillingSummary", "Credit", "Plan", "Usage"]


class Credit(BaseModel):
    """An unexpired Orb credit block, including scheduled and depleted allotments."""

    id: str
    """The Orb credit block id."""

    currency: str
    """The Orb custom pricing-unit identifier, such as mnr_credits or ai_credits."""

    effective_at: Optional[datetime] = None
    """When the block becomes effective."""

    expires_at: Optional[datetime] = None
    """When the block expires."""

    name: str
    """The display name for the credit currency."""

    quantity: float
    """The block's original allocation."""

    remaining: float
    """The block's remaining balance."""

    status: Literal["active", "depleted", "scheduled"]
    """
    Derived block status: scheduled when not yet effective, depleted when remaining
    is zero or less, otherwise active.
    """


class Plan(BaseModel):
    """The Knock plan currently assigned to the account."""

    id: str
    """The unique identifier of the plan."""

    display_name: str
    """The human-readable plan name."""

    type: Literal["free", "starter", "growth", "enterprise"]
    """The plan type."""


class Usage(BaseModel):
    """Usage for a single Orb billable metric on the current draft invoice."""

    amount: str
    """The billed dollar amount for this metric after credits and adjustments."""

    credits_applied: int
    """Prepaid credits applied to this metric during the current service period."""

    metric_id: str
    """The Orb billable metric id."""

    name: str
    """The Orb billable metric name."""

    pricing_currency: Optional[str] = None
    """
    The Orb price currency for this line item, used to correlate usage with credit
    blocks.
    """

    quantity: int
    """Orb line-item usage quantity for this period.

    This is not replaced by credits_applied.
    """

    quantity_type: Literal["usage", "credits"]
    """Whether the GraphQL usage quantity is raw usage or credits applied.

    Prefer quantity and credits_applied for new clients.
    """


class BillingSummary(BaseModel):
    """
    A snapshot of the current draft Orb invoice for the account, including plan, per-metric usage, and remaining credit blocks.
    """

    amount_due: str
    """The amount due on the draft invoice, as a decimal string."""

    credits: List[Credit]
    """
    Unexpired Orb credit blocks for custom pricing units on the draft invoice,
    including scheduled and depleted allotments.
    """

    currency: Optional[str] = None
    """The invoice currency code, such as USD."""

    invoice_id: Optional[str] = None
    """The Orb draft invoice id, if present."""

    period_end: Optional[datetime] = None
    """The end of the current usage period, hoisted from the first usage line item."""

    period_start: Optional[datetime] = None
    """The start of the current usage period, hoisted from the first usage line item."""

    plan: Plan
    """The Knock plan currently assigned to the account."""

    target_date: date
    """The date the draft invoice is scheduled to be issued."""

    usage: List[Usage]
    """Per-metric usage line items from the draft invoice."""
