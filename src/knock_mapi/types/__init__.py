# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import (
    workflow,
    workflow_branch_step,
    workflow_upsert_response,
    workflow_activate_response,
    workflow_validate_response,
)
from .. import _compat
from .guide import Guide as Guide
from .commit import Commit as Commit
from .shared import PageInfo as PageInfo
from .channel import Channel as Channel
from .partial import Partial as Partial
from .duration import Duration as Duration
from .variable import Variable as Variable
from .workflow import Workflow as Workflow
from .condition import Condition as Condition
from .guide_step import GuideStep as GuideStep
from .environment import Environment as Environment
from .send_window import SendWindow as SendWindow
from .translation import Translation as Translation
from .email_layout import EmailLayout as EmailLayout
from .message_type import MessageType as MessageType
from .sms_template import SMSTemplate as SMSTemplate
from .channel_group import ChannelGroup as ChannelGroup
from .chat_template import ChatTemplate as ChatTemplate
from .push_template import PushTemplate as PushTemplate
from .workflow_step import WorkflowStep as WorkflowStep
from .duration_param import DurationParam as DurationParam
from .email_template import EmailTemplate as EmailTemplate
from .condition_group import ConditionGroup as ConditionGroup
from .condition_param import ConditionParam as ConditionParam
from .guide_step_param import GuideStepParam as GuideStepParam
from .request_template import RequestTemplate as RequestTemplate
from .webhook_template import WebhookTemplate as WebhookTemplate
from .guide_list_params import GuideListParams as GuideListParams
from .send_window_param import SendWindowParam as SendWindowParam
from .channel_group_rule import ChannelGroupRule as ChannelGroupRule
from .commit_list_params import CommitListParams as CommitListParams
from .sms_template_param import SMSTemplateParam as SMSTemplateParam
from .channel_list_params import ChannelListParams as ChannelListParams
from .chat_template_param import ChatTemplateParam as ChatTemplateParam
from .guide_upsert_params import GuideUpsertParams as GuideUpsertParams
from .partial_list_params import PartialListParams as PartialListParams
from .push_template_param import PushTemplateParam as PushTemplateParam
from .workflow_batch_step import WorkflowBatchStep as WorkflowBatchStep
from .workflow_delay_step import WorkflowDelayStep as WorkflowDelayStep
from .workflow_fetch_step import WorkflowFetchStep as WorkflowFetchStep
from .workflow_run_params import WorkflowRunParams as WorkflowRunParams
from .workflow_step_param import WorkflowStepParam as WorkflowStepParam
from .auth_verify_response import AuthVerifyResponse as AuthVerifyResponse
from .email_template_param import EmailTemplateParam as EmailTemplateParam
from .in_app_feed_template import InAppFeedTemplate as InAppFeedTemplate
from .message_type_variant import MessageTypeVariant as MessageTypeVariant
from .sms_channel_settings import SMSChannelSettings as SMSChannelSettings
from .variable_list_params import VariableListParams as VariableListParams
from .workflow_branch_step import WorkflowBranchStep as WorkflowBranchStep
from .workflow_list_params import WorkflowListParams as WorkflowListParams
from .chat_channel_settings import ChatChannelSettings as ChatChannelSettings
from .condition_group_param import ConditionGroupParam as ConditionGroupParam
from .guide_activate_params import GuideActivateParams as GuideActivateParams
from .guide_retrieve_params import GuideRetrieveParams as GuideRetrieveParams
from .guide_upsert_response import GuideUpsertResponse as GuideUpsertResponse
from .guide_validate_params import GuideValidateParams as GuideValidateParams
from .partial_upsert_params import PartialUpsertParams as PartialUpsertParams
from .push_channel_settings import PushChannelSettings as PushChannelSettings
from .workflow_channel_step import WorkflowChannelStep as WorkflowChannelStep
from .workflow_run_response import WorkflowRunResponse as WorkflowRunResponse
from .email_channel_settings import EmailChannelSettings as EmailChannelSettings
from .request_template_param import RequestTemplateParam as RequestTemplateParam
from .webhook_template_param import WebhookTemplateParam as WebhookTemplateParam
from .workflow_throttle_step import WorkflowThrottleStep as WorkflowThrottleStep
from .workflow_upsert_params import WorkflowUpsertParams as WorkflowUpsertParams
from .api_key_exchange_params import APIKeyExchangeParams as APIKeyExchangeParams
from .environment_list_params import EnvironmentListParams as EnvironmentListParams
from .guide_activate_response import GuideActivateResponse as GuideActivateResponse
from .guide_validate_response import GuideValidateResponse as GuideValidateResponse
from .message_type_text_field import MessageTypeTextField as MessageTypeTextField
from .partial_retrieve_params import PartialRetrieveParams as PartialRetrieveParams
from .partial_upsert_response import PartialUpsertResponse as PartialUpsertResponse
from .partial_validate_params import PartialValidateParams as PartialValidateParams
from .translation_list_params import TranslationListParams as TranslationListParams
from .commit_commit_all_params import CommitCommitAllParams as CommitCommitAllParams
from .email_layout_list_params import EmailLayoutListParams as EmailLayoutListParams
from .message_type_list_params import MessageTypeListParams as MessageTypeListParams
from .workflow_activate_params import WorkflowActivateParams as WorkflowActivateParams
from .workflow_retrieve_params import WorkflowRetrieveParams as WorkflowRetrieveParams
from .workflow_upsert_response import WorkflowUpsertResponse as WorkflowUpsertResponse
from .workflow_validate_params import WorkflowValidateParams as WorkflowValidateParams
from .api_key_exchange_response import APIKeyExchangeResponse as APIKeyExchangeResponse
from .channel_group_list_params import ChannelGroupListParams as ChannelGroupListParams
from .commit_promote_all_params import CommitPromoteAllParams as CommitPromoteAllParams
from .partial_validate_response import PartialValidateResponse as PartialValidateResponse
from .translation_upsert_params import TranslationUpsertParams as TranslationUpsertParams
from .workflow_batch_step_param import WorkflowBatchStepParam as WorkflowBatchStepParam
from .workflow_delay_step_param import WorkflowDelayStepParam as WorkflowDelayStepParam
from .workflow_fetch_step_param import WorkflowFetchStepParam as WorkflowFetchStepParam
from .commit_commit_all_response import CommitCommitAllResponse as CommitCommitAllResponse
from .email_layout_upsert_params import EmailLayoutUpsertParams as EmailLayoutUpsertParams
from .in_app_feed_template_param import InAppFeedTemplateParam as InAppFeedTemplateParam
from .message_type_upsert_params import MessageTypeUpsertParams as MessageTypeUpsertParams
from .message_type_variant_param import MessageTypeVariantParam as MessageTypeVariantParam
from .sms_channel_settings_param import SMSChannelSettingsParam as SMSChannelSettingsParam
from .workflow_activate_response import WorkflowActivateResponse as WorkflowActivateResponse
from .workflow_branch_step_param import WorkflowBranchStepParam as WorkflowBranchStepParam
from .workflow_validate_response import WorkflowValidateResponse as WorkflowValidateResponse
from .chat_channel_settings_param import ChatChannelSettingsParam as ChatChannelSettingsParam
from .commit_promote_all_response import CommitPromoteAllResponse as CommitPromoteAllResponse
from .commit_promote_one_response import CommitPromoteOneResponse as CommitPromoteOneResponse
from .push_channel_settings_param import PushChannelSettingsParam as PushChannelSettingsParam
from .translation_retrieve_params import TranslationRetrieveParams as TranslationRetrieveParams
from .translation_upsert_response import TranslationUpsertResponse as TranslationUpsertResponse
from .translation_validate_params import TranslationValidateParams as TranslationValidateParams
from .workflow_channel_step_param import WorkflowChannelStepParam as WorkflowChannelStepParam
from .email_channel_settings_param import EmailChannelSettingsParam as EmailChannelSettingsParam
from .email_layout_retrieve_params import EmailLayoutRetrieveParams as EmailLayoutRetrieveParams
from .email_layout_upsert_response import EmailLayoutUpsertResponse as EmailLayoutUpsertResponse
from .email_layout_validate_params import EmailLayoutValidateParams as EmailLayoutValidateParams
from .in_app_feed_channel_settings import InAppFeedChannelSettings as InAppFeedChannelSettings
from .message_type_retrieve_params import MessageTypeRetrieveParams as MessageTypeRetrieveParams
from .message_type_upsert_response import MessageTypeUpsertResponse as MessageTypeUpsertResponse
from .message_type_validate_params import MessageTypeValidateParams as MessageTypeValidateParams
from .workflow_throttle_step_param import WorkflowThrottleStepParam as WorkflowThrottleStepParam
from .message_type_text_field_param import MessageTypeTextFieldParam as MessageTypeTextFieldParam
from .translation_retrieve_response import TranslationRetrieveResponse as TranslationRetrieveResponse
from .translation_validate_response import TranslationValidateResponse as TranslationValidateResponse
from .email_layout_validate_response import EmailLayoutValidateResponse as EmailLayoutValidateResponse
from .guide_activation_location_rule import GuideActivationLocationRule as GuideActivationLocationRule
from .message_type_validate_response import MessageTypeValidateResponse as MessageTypeValidateResponse
from .workflow_trigger_workflow_step import WorkflowTriggerWorkflowStep as WorkflowTriggerWorkflowStep
from .in_app_feed_channel_settings_param import InAppFeedChannelSettingsParam as InAppFeedChannelSettingsParam
from .guide_activation_location_rule_param import GuideActivationLocationRuleParam as GuideActivationLocationRuleParam
from .workflow_trigger_workflow_step_param import WorkflowTriggerWorkflowStepParam as WorkflowTriggerWorkflowStepParam

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V2:
    workflow.Workflow.model_rebuild(_parent_namespace_depth=0)
    workflow_branch_step.WorkflowBranchStep.model_rebuild(_parent_namespace_depth=0)
    workflow_activate_response.WorkflowActivateResponse.model_rebuild(_parent_namespace_depth=0)
    workflow_upsert_response.WorkflowUpsertResponse.model_rebuild(_parent_namespace_depth=0)
    workflow_validate_response.WorkflowValidateResponse.model_rebuild(_parent_namespace_depth=0)
else:
    workflow.Workflow.update_forward_refs()  # type: ignore
    workflow_branch_step.WorkflowBranchStep.update_forward_refs()  # type: ignore
    workflow_activate_response.WorkflowActivateResponse.update_forward_refs()  # type: ignore
    workflow_upsert_response.WorkflowUpsertResponse.update_forward_refs()  # type: ignore
    workflow_validate_response.WorkflowValidateResponse.update_forward_refs()  # type: ignore
