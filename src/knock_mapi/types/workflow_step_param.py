# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from typing_extensions import TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .workflow_sms_step_param import WorkflowSMSStepParam
from .workflow_chat_step_param import WorkflowChatStepParam
from .workflow_push_step_param import WorkflowPushStepParam
from .workflow_batch_step_param import WorkflowBatchStepParam
from .workflow_delay_step_param import WorkflowDelayStepParam
from .workflow_email_step_param import WorkflowEmailStepParam
from .workflow_fetch_step_param import WorkflowFetchStepParam
from .workflow_webhook_step_param import WorkflowWebhookStepParam
from .workflow_ai_agent_step_param import WorkflowAIAgentStepParam
from .workflow_throttle_step_param import WorkflowThrottleStepParam
from .workflow_in_app_feed_step_param import WorkflowInAppFeedStepParam
from .workflow_update_data_step_param import WorkflowUpdateDataStepParam
from .workflow_update_user_step_param import WorkflowUpdateUserStepParam
from .workflow_random_cohort_step_param import WorkflowRandomCohortStepParam
from .workflow_update_object_step_param import WorkflowUpdateObjectStepParam
from .workflow_update_tenant_step_param import WorkflowUpdateTenantStepParam
from .workflow_trigger_workflow_step_param import WorkflowTriggerWorkflowStepParam

__all__ = ["WorkflowStepParam"]

if TYPE_CHECKING or not PYDANTIC_V1:
    WorkflowStepParam = TypeAliasType(
        "WorkflowStepParam",
        Union[
            WorkflowWebhookStepParam,
            WorkflowInAppFeedStepParam,
            WorkflowChatStepParam,
            WorkflowSMSStepParam,
            WorkflowPushStepParam,
            WorkflowEmailStepParam,
            WorkflowAIAgentStepParam,
            WorkflowDelayStepParam,
            WorkflowBatchStepParam,
            WorkflowFetchStepParam,
            WorkflowUpdateDataStepParam,
            WorkflowUpdateObjectStepParam,
            WorkflowUpdateTenantStepParam,
            WorkflowUpdateUserStepParam,
            WorkflowThrottleStepParam,
            "WorkflowBranchStepParam",
            WorkflowRandomCohortStepParam,
            WorkflowTriggerWorkflowStepParam,
        ],
    )
else:
    WorkflowStepParam: TypeAlias = Union[
        WorkflowWebhookStepParam,
        WorkflowInAppFeedStepParam,
        WorkflowChatStepParam,
        WorkflowSMSStepParam,
        WorkflowPushStepParam,
        WorkflowEmailStepParam,
        WorkflowAIAgentStepParam,
        WorkflowDelayStepParam,
        WorkflowBatchStepParam,
        WorkflowFetchStepParam,
        WorkflowUpdateDataStepParam,
        WorkflowUpdateObjectStepParam,
        WorkflowUpdateTenantStepParam,
        WorkflowUpdateUserStepParam,
        WorkflowThrottleStepParam,
        "WorkflowBranchStepParam",
        WorkflowRandomCohortStepParam,
        WorkflowTriggerWorkflowStepParam,
    ]

from .workflow_branch_step_param import WorkflowBranchStepParam
