# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from typing_extensions import TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .workflow_batch_step_param import WorkflowBatchStepParam
from .workflow_delay_step_param import WorkflowDelayStepParam
from .workflow_fetch_step_param import WorkflowFetchStepParam
from .workflow_channel_step_param import WorkflowChannelStepParam
from .workflow_throttle_step_param import WorkflowThrottleStepParam
from .workflow_trigger_workflow_step_param import WorkflowTriggerWorkflowStepParam

__all__ = ["WorkflowStepParam"]

if TYPE_CHECKING or not PYDANTIC_V1:
    WorkflowStepParam = TypeAliasType(
        "WorkflowStepParam",
        Union[
            WorkflowChannelStepParam,
            WorkflowDelayStepParam,
            WorkflowBatchStepParam,
            WorkflowFetchStepParam,
            WorkflowThrottleStepParam,
            "WorkflowBranchStepParam",
            WorkflowTriggerWorkflowStepParam,
        ],
    )
else:
    WorkflowStepParam: TypeAlias = Union[
        WorkflowChannelStepParam,
        WorkflowDelayStepParam,
        WorkflowBatchStepParam,
        WorkflowFetchStepParam,
        WorkflowThrottleStepParam,
        "WorkflowBranchStepParam",
        WorkflowTriggerWorkflowStepParam,
    ]

from .workflow_branch_step_param import WorkflowBranchStepParam
