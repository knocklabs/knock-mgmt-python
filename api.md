# Shared Types

```python
from knock_mapi.types import (
    MessageTypeBooleanField,
    MessageTypeButtonField,
    MessageTypeImageField,
    MessageTypeJsonField,
    MessageTypeMarkdownField,
    MessageTypeMultiSelectField,
    MessageTypeSelectField,
    MessageTypeTextareaField,
    MessageTypeURLField,
    PageInfo,
)
```

# Templates

Types:

```python
from knock_mapi.types import (
    ChatTemplate,
    EmailTemplate,
    InAppFeedTemplate,
    PushTemplate,
    RequestTemplate,
    SMSTemplate,
    WebhookTemplate,
    TemplatePreviewResponse,
)
```

Methods:

- <code title="post /v1/templates/preview">client.templates.<a href="./src/knock_mapi/resources/templates.py">preview</a>(\*\*<a href="src/knock_mapi/types/template_preview_params.py">params</a>) -> <a href="./src/knock_mapi/types/template_preview_response.py">TemplatePreviewResponse</a></code>

# EmailLayouts

Types:

```python
from knock_mapi.types import EmailLayout, EmailLayoutUpsertResponse, EmailLayoutValidateResponse
```

Methods:

- <code title="get /v1/email_layouts/{email_layout_key}">client.email_layouts.<a href="./src/knock_mapi/resources/email_layouts.py">retrieve</a>(email_layout_key, \*\*<a href="src/knock_mapi/types/email_layout_retrieve_params.py">params</a>) -> <a href="./src/knock_mapi/types/email_layout.py">EmailLayout</a></code>
- <code title="get /v1/email_layouts">client.email_layouts.<a href="./src/knock_mapi/resources/email_layouts.py">list</a>(\*\*<a href="src/knock_mapi/types/email_layout_list_params.py">params</a>) -> <a href="./src/knock_mapi/types/email_layout.py">SyncEntriesCursor[EmailLayout]</a></code>
- <code title="put /v1/email_layouts/{email_layout_key}">client.email_layouts.<a href="./src/knock_mapi/resources/email_layouts.py">upsert</a>(email_layout_key, \*\*<a href="src/knock_mapi/types/email_layout_upsert_params.py">params</a>) -> <a href="./src/knock_mapi/types/email_layout_upsert_response.py">EmailLayoutUpsertResponse</a></code>
- <code title="put /v1/email_layouts/{email_layout_key}/validate">client.email_layouts.<a href="./src/knock_mapi/resources/email_layouts.py">validate</a>(email_layout_key, \*\*<a href="src/knock_mapi/types/email_layout_validate_params.py">params</a>) -> <a href="./src/knock_mapi/types/email_layout_validate_response.py">EmailLayoutValidateResponse</a></code>

# Commits

Types:

```python
from knock_mapi.types import (
    Commit,
    CommitCommitAllResponse,
    CommitPromoteAllResponse,
    CommitPromoteOneResponse,
)
```

Methods:

- <code title="get /v1/commits/{id}">client.commits.<a href="./src/knock_mapi/resources/commits.py">retrieve</a>(id) -> <a href="./src/knock_mapi/types/commit.py">Commit</a></code>
- <code title="get /v1/commits">client.commits.<a href="./src/knock_mapi/resources/commits.py">list</a>(\*\*<a href="src/knock_mapi/types/commit_list_params.py">params</a>) -> <a href="./src/knock_mapi/types/commit.py">SyncEntriesCursor[Commit]</a></code>
- <code title="put /v1/commits">client.commits.<a href="./src/knock_mapi/resources/commits.py">commit_all</a>(\*\*<a href="src/knock_mapi/types/commit_commit_all_params.py">params</a>) -> <a href="./src/knock_mapi/types/commit_commit_all_response.py">CommitCommitAllResponse</a></code>
- <code title="put /v1/commits/promote">client.commits.<a href="./src/knock_mapi/resources/commits.py">promote_all</a>(\*\*<a href="src/knock_mapi/types/commit_promote_all_params.py">params</a>) -> <a href="./src/knock_mapi/types/commit_promote_all_response.py">CommitPromoteAllResponse</a></code>
- <code title="put /v1/commits/{id}/promote">client.commits.<a href="./src/knock_mapi/resources/commits.py">promote_one</a>(id) -> <a href="./src/knock_mapi/types/commit_promote_one_response.py">CommitPromoteOneResponse</a></code>

# Partials

Types:

```python
from knock_mapi.types import Partial, PartialUpsertResponse, PartialValidateResponse
```

Methods:

- <code title="get /v1/partials/{partial_key}">client.partials.<a href="./src/knock_mapi/resources/partials.py">retrieve</a>(partial_key, \*\*<a href="src/knock_mapi/types/partial_retrieve_params.py">params</a>) -> <a href="./src/knock_mapi/types/partial.py">Partial</a></code>
- <code title="get /v1/partials">client.partials.<a href="./src/knock_mapi/resources/partials.py">list</a>(\*\*<a href="src/knock_mapi/types/partial_list_params.py">params</a>) -> <a href="./src/knock_mapi/types/partial.py">SyncEntriesCursor[Partial]</a></code>
- <code title="put /v1/partials/{partial_key}">client.partials.<a href="./src/knock_mapi/resources/partials.py">upsert</a>(partial_key, \*\*<a href="src/knock_mapi/types/partial_upsert_params.py">params</a>) -> <a href="./src/knock_mapi/types/partial_upsert_response.py">PartialUpsertResponse</a></code>
- <code title="put /v1/partials/{partial_key}/validate">client.partials.<a href="./src/knock_mapi/resources/partials.py">validate</a>(partial_key, \*\*<a href="src/knock_mapi/types/partial_validate_params.py">params</a>) -> <a href="./src/knock_mapi/types/partial_validate_response.py">PartialValidateResponse</a></code>

# Translations

Types:

```python
from knock_mapi.types import (
    Translation,
    TranslationRetrieveResponse,
    TranslationUpsertResponse,
    TranslationValidateResponse,
)
```

Methods:

- <code title="get /v1/translations/{locale_code}">client.translations.<a href="./src/knock_mapi/resources/translations.py">retrieve</a>(locale_code, \*\*<a href="src/knock_mapi/types/translation_retrieve_params.py">params</a>) -> <a href="./src/knock_mapi/types/translation_retrieve_response.py">TranslationRetrieveResponse</a></code>
- <code title="get /v1/translations">client.translations.<a href="./src/knock_mapi/resources/translations.py">list</a>(\*\*<a href="src/knock_mapi/types/translation_list_params.py">params</a>) -> <a href="./src/knock_mapi/types/translation.py">SyncEntriesCursor[Translation]</a></code>
- <code title="put /v1/translations/{locale_code}">client.translations.<a href="./src/knock_mapi/resources/translations.py">upsert</a>(locale_code, \*\*<a href="src/knock_mapi/types/translation_upsert_params.py">params</a>) -> <a href="./src/knock_mapi/types/translation_upsert_response.py">TranslationUpsertResponse</a></code>
- <code title="put /v1/translations/{locale_code}/validate">client.translations.<a href="./src/knock_mapi/resources/translations.py">validate</a>(locale_code, \*\*<a href="src/knock_mapi/types/translation_validate_params.py">params</a>) -> <a href="./src/knock_mapi/types/translation_validate_response.py">TranslationValidateResponse</a></code>

# Workflows

Types:

```python
from knock_mapi.types import (
    Condition,
    ConditionGroup,
    Duration,
    SendWindow,
    Workflow,
    WorkflowAIAgentStep,
    WorkflowBatchStep,
    WorkflowBranchStep,
    WorkflowChatStep,
    WorkflowDelayStep,
    WorkflowEmailStep,
    WorkflowFetchStep,
    WorkflowInAppFeedStep,
    WorkflowPushStep,
    WorkflowRandomCohortStep,
    WorkflowSMSStep,
    WorkflowStep,
    WorkflowThrottleStep,
    WorkflowTriggerWorkflowStep,
    WorkflowUpdateDataStep,
    WorkflowUpdateObjectStep,
    WorkflowUpdateTenantStep,
    WorkflowUpdateUserStep,
    WorkflowWebhookStep,
    WorkflowRetrieveResponse,
    WorkflowActivateResponse,
    WorkflowRunResponse,
    WorkflowUpsertResponse,
    WorkflowValidateResponse,
)
```

Methods:

- <code title="get /v1/workflows/{workflow_key}">client.workflows.<a href="./src/knock_mapi/resources/workflows/workflows.py">retrieve</a>(workflow_key, \*\*<a href="src/knock_mapi/types/workflow_retrieve_params.py">params</a>) -> <a href="./src/knock_mapi/types/workflow_retrieve_response.py">WorkflowRetrieveResponse</a></code>
- <code title="get /v1/workflows">client.workflows.<a href="./src/knock_mapi/resources/workflows/workflows.py">list</a>(\*\*<a href="src/knock_mapi/types/workflow_list_params.py">params</a>) -> <a href="./src/knock_mapi/types/workflow.py">SyncEntriesCursor[Workflow]</a></code>
- <code title="put /v1/workflows/{workflow_key}/activate">client.workflows.<a href="./src/knock_mapi/resources/workflows/workflows.py">activate</a>(workflow_key, \*\*<a href="src/knock_mapi/types/workflow_activate_params.py">params</a>) -> <a href="./src/knock_mapi/types/workflow_activate_response.py">WorkflowActivateResponse</a></code>
- <code title="put /v1/workflows/{workflow_key}/run">client.workflows.<a href="./src/knock_mapi/resources/workflows/workflows.py">run</a>(workflow_key, \*\*<a href="src/knock_mapi/types/workflow_run_params.py">params</a>) -> <a href="./src/knock_mapi/types/workflow_run_response.py">WorkflowRunResponse</a></code>
- <code title="put /v1/workflows/{workflow_key}">client.workflows.<a href="./src/knock_mapi/resources/workflows/workflows.py">upsert</a>(workflow_key, \*\*<a href="src/knock_mapi/types/workflow_upsert_params.py">params</a>) -> <a href="./src/knock_mapi/types/workflow_upsert_response.py">WorkflowUpsertResponse</a></code>
- <code title="put /v1/workflows/{workflow_key}/validate">client.workflows.<a href="./src/knock_mapi/resources/workflows/workflows.py">validate</a>(workflow_key, \*\*<a href="src/knock_mapi/types/workflow_validate_params.py">params</a>) -> <a href="./src/knock_mapi/types/workflow_validate_response.py">WorkflowValidateResponse</a></code>

## Steps

Types:

```python
from knock_mapi.types.workflows import StepPreviewTemplateResponse
```

Methods:

- <code title="post /v1/workflows/{workflow_key}/steps/{step_ref}/preview_template">client.workflows.steps.<a href="./src/knock_mapi/resources/workflows/steps.py">preview_template</a>(step_ref, \*, workflow_key, \*\*<a href="src/knock_mapi/types/workflows/step_preview_template_params.py">params</a>) -> <a href="./src/knock_mapi/types/workflows/step_preview_template_response.py">StepPreviewTemplateResponse</a></code>

# MessageTypes

Types:

```python
from knock_mapi.types import (
    MessageType,
    MessageTypeTextField,
    MessageTypeVariant,
    MessageTypeUpsertResponse,
    MessageTypeValidateResponse,
)
```

Methods:

- <code title="get /v1/message_types/{message_type_key}">client.message_types.<a href="./src/knock_mapi/resources/message_types.py">retrieve</a>(message_type_key, \*\*<a href="src/knock_mapi/types/message_type_retrieve_params.py">params</a>) -> <a href="./src/knock_mapi/types/message_type.py">MessageType</a></code>
- <code title="get /v1/message_types">client.message_types.<a href="./src/knock_mapi/resources/message_types.py">list</a>(\*\*<a href="src/knock_mapi/types/message_type_list_params.py">params</a>) -> <a href="./src/knock_mapi/types/message_type.py">SyncEntriesCursor[MessageType]</a></code>
- <code title="put /v1/message_types/{message_type_key}">client.message_types.<a href="./src/knock_mapi/resources/message_types.py">upsert</a>(message_type_key, \*\*<a href="src/knock_mapi/types/message_type_upsert_params.py">params</a>) -> <a href="./src/knock_mapi/types/message_type_upsert_response.py">MessageTypeUpsertResponse</a></code>
- <code title="put /v1/message_types/{message_type_key}/validate">client.message_types.<a href="./src/knock_mapi/resources/message_types.py">validate</a>(message_type_key, \*\*<a href="src/knock_mapi/types/message_type_validate_params.py">params</a>) -> <a href="./src/knock_mapi/types/message_type_validate_response.py">MessageTypeValidateResponse</a></code>

# Auth

Types:

```python
from knock_mapi.types import AuthVerifyResponse
```

Methods:

- <code title="get /v1/whoami">client.auth.<a href="./src/knock_mapi/resources/auth.py">verify</a>() -> <a href="./src/knock_mapi/types/auth_verify_response.py">AuthVerifyResponse</a></code>

# APIKeys

Types:

```python
from knock_mapi.types import APIKeyExchangeResponse
```

Methods:

- <code title="post /v1/api_keys/exchange">client.api_keys.<a href="./src/knock_mapi/resources/api_keys.py">exchange</a>(\*\*<a href="src/knock_mapi/types/api_key_exchange_params.py">params</a>) -> <a href="./src/knock_mapi/types/api_key_exchange_response.py">APIKeyExchangeResponse</a></code>

# ChannelGroups

Types:

```python
from knock_mapi.types import ChannelGroup, ChannelGroupRule, ChannelGroupUpsertResponse
```

Methods:

- <code title="get /v1/channel_groups/{channel_group_key}">client.channel_groups.<a href="./src/knock_mapi/resources/channel_groups.py">retrieve</a>(channel_group_key) -> <a href="./src/knock_mapi/types/channel_group.py">ChannelGroup</a></code>
- <code title="get /v1/channel_groups">client.channel_groups.<a href="./src/knock_mapi/resources/channel_groups.py">list</a>(\*\*<a href="src/knock_mapi/types/channel_group_list_params.py">params</a>) -> <a href="./src/knock_mapi/types/channel_group.py">SyncEntriesCursor[ChannelGroup]</a></code>
- <code title="delete /v1/channel_groups/{channel_group_key}">client.channel_groups.<a href="./src/knock_mapi/resources/channel_groups.py">delete</a>(channel_group_key) -> None</code>
- <code title="put /v1/channel_groups/{channel_group_key}">client.channel_groups.<a href="./src/knock_mapi/resources/channel_groups.py">upsert</a>(channel_group_key, \*\*<a href="src/knock_mapi/types/channel_group_upsert_params.py">params</a>) -> <a href="./src/knock_mapi/types/channel_group_upsert_response.py">ChannelGroupUpsertResponse</a></code>

# Channels

Types:

```python
from knock_mapi.types import (
    Channel,
    ChannelEnvironmentSettings,
    ChatChannelSettings,
    EmailChannelSettings,
    InAppFeedChannelSettings,
    PushChannelSettings,
    SMSChannelSettings,
)
```

Methods:

- <code title="get /v1/channels/{channel_key}">client.channels.<a href="./src/knock_mapi/resources/channels.py">retrieve</a>(channel_key) -> <a href="./src/knock_mapi/types/channel.py">Channel</a></code>
- <code title="get /v1/channels">client.channels.<a href="./src/knock_mapi/resources/channels.py">list</a>(\*\*<a href="src/knock_mapi/types/channel_list_params.py">params</a>) -> <a href="./src/knock_mapi/types/channel.py">SyncEntriesCursor[Channel]</a></code>

# Members

Types:

```python
from knock_mapi.types import Member, MemberUser
```

Methods:

- <code title="get /v1/members/{id}">client.members.<a href="./src/knock_mapi/resources/members.py">retrieve</a>(id) -> <a href="./src/knock_mapi/types/member.py">Member</a></code>
- <code title="get /v1/members">client.members.<a href="./src/knock_mapi/resources/members.py">list</a>(\*\*<a href="src/knock_mapi/types/member_list_params.py">params</a>) -> <a href="./src/knock_mapi/types/member.py">SyncEntriesCursor[Member]</a></code>
- <code title="delete /v1/members/{id}">client.members.<a href="./src/knock_mapi/resources/members.py">delete</a>(id) -> None</code>

# Environments

Types:

```python
from knock_mapi.types import Environment
```

Methods:

- <code title="get /v1/environments/{environment_slug}">client.environments.<a href="./src/knock_mapi/resources/environments.py">retrieve</a>(environment_slug) -> <a href="./src/knock_mapi/types/environment.py">Environment</a></code>
- <code title="get /v1/environments">client.environments.<a href="./src/knock_mapi/resources/environments.py">list</a>(\*\*<a href="src/knock_mapi/types/environment_list_params.py">params</a>) -> <a href="./src/knock_mapi/types/environment.py">SyncEntriesCursor[Environment]</a></code>

# Variables

Types:

```python
from knock_mapi.types import Variable
```

Methods:

- <code title="get /v1/variables/{key}">client.variables.<a href="./src/knock_mapi/resources/variables.py">retrieve</a>(key) -> <a href="./src/knock_mapi/types/variable.py">Variable</a></code>
- <code title="get /v1/variables">client.variables.<a href="./src/knock_mapi/resources/variables.py">list</a>(\*\*<a href="src/knock_mapi/types/variable_list_params.py">params</a>) -> <a href="./src/knock_mapi/types/variable.py">SyncEntriesCursor[Variable]</a></code>

# Guides

Types:

```python
from knock_mapi.types import (
    Guide,
    GuideActivationURLPattern,
    GuideStep,
    GuideActivateResponse,
    GuideArchiveResponse,
    GuideUpsertResponse,
    GuideValidateResponse,
)
```

Methods:

- <code title="get /v1/guides/{guide_key}">client.guides.<a href="./src/knock_mapi/resources/guides.py">retrieve</a>(guide_key, \*\*<a href="src/knock_mapi/types/guide_retrieve_params.py">params</a>) -> <a href="./src/knock_mapi/types/guide.py">Guide</a></code>
- <code title="get /v1/guides">client.guides.<a href="./src/knock_mapi/resources/guides.py">list</a>(\*\*<a href="src/knock_mapi/types/guide_list_params.py">params</a>) -> <a href="./src/knock_mapi/types/guide.py">SyncEntriesCursor[Guide]</a></code>
- <code title="put /v1/guides/{guide_key}/activate">client.guides.<a href="./src/knock_mapi/resources/guides.py">activate</a>(guide_key, \*\*<a href="src/knock_mapi/types/guide_activate_params.py">params</a>) -> <a href="./src/knock_mapi/types/guide_activate_response.py">GuideActivateResponse</a></code>
- <code title="delete /v1/guides/{guide_key}">client.guides.<a href="./src/knock_mapi/resources/guides.py">archive</a>(guide_key) -> <a href="./src/knock_mapi/types/guide_archive_response.py">GuideArchiveResponse</a></code>
- <code title="put /v1/guides/{guide_key}">client.guides.<a href="./src/knock_mapi/resources/guides.py">upsert</a>(guide_key, \*\*<a href="src/knock_mapi/types/guide_upsert_params.py">params</a>) -> <a href="./src/knock_mapi/types/guide_upsert_response.py">GuideUpsertResponse</a></code>
- <code title="put /v1/guides/{guide_key}/validate">client.guides.<a href="./src/knock_mapi/resources/guides.py">validate</a>(guide_key, \*\*<a href="src/knock_mapi/types/guide_validate_params.py">params</a>) -> <a href="./src/knock_mapi/types/guide_validate_response.py">GuideValidateResponse</a></code>

# Branches

Types:

```python
from knock_mapi.types import Branch
```

Methods:

- <code title="post /v1/branches/{branch_slug}">client.branches.<a href="./src/knock_mapi/resources/branches.py">create</a>(branch_slug, \*\*<a href="src/knock_mapi/types/branch_create_params.py">params</a>) -> <a href="./src/knock_mapi/types/branch.py">Branch</a></code>
- <code title="get /v1/branches/{branch_slug}">client.branches.<a href="./src/knock_mapi/resources/branches.py">retrieve</a>(branch_slug, \*\*<a href="src/knock_mapi/types/branch_retrieve_params.py">params</a>) -> <a href="./src/knock_mapi/types/branch.py">Branch</a></code>
- <code title="get /v1/branches">client.branches.<a href="./src/knock_mapi/resources/branches.py">list</a>(\*\*<a href="src/knock_mapi/types/branch_list_params.py">params</a>) -> <a href="./src/knock_mapi/types/branch.py">SyncEntriesCursor[Branch]</a></code>
- <code title="delete /v1/branches/{branch_slug}">client.branches.<a href="./src/knock_mapi/resources/branches.py">delete</a>(branch_slug, \*\*<a href="src/knock_mapi/types/branch_delete_params.py">params</a>) -> None</code>

# Broadcasts

Types:

```python
from knock_mapi.types import (
    Broadcast,
    BroadcastRequest,
    BroadcastCancelResponse,
    BroadcastSendResponse,
    BroadcastUpsertResponse,
    BroadcastValidateResponse,
)
```

Methods:

- <code title="get /v1/broadcasts/{broadcast_key}">client.broadcasts.<a href="./src/knock_mapi/resources/broadcasts.py">retrieve</a>(broadcast_key, \*\*<a href="src/knock_mapi/types/broadcast_retrieve_params.py">params</a>) -> <a href="./src/knock_mapi/types/broadcast.py">Broadcast</a></code>
- <code title="get /v1/broadcasts">client.broadcasts.<a href="./src/knock_mapi/resources/broadcasts.py">list</a>(\*\*<a href="src/knock_mapi/types/broadcast_list_params.py">params</a>) -> <a href="./src/knock_mapi/types/broadcast.py">SyncEntriesCursor[Broadcast]</a></code>
- <code title="put /v1/broadcasts/{broadcast_key}/cancel">client.broadcasts.<a href="./src/knock_mapi/resources/broadcasts.py">cancel</a>(broadcast_key, \*\*<a href="src/knock_mapi/types/broadcast_cancel_params.py">params</a>) -> <a href="./src/knock_mapi/types/broadcast_cancel_response.py">BroadcastCancelResponse</a></code>
- <code title="put /v1/broadcasts/{broadcast_key}/send">client.broadcasts.<a href="./src/knock_mapi/resources/broadcasts.py">send</a>(broadcast_key, \*\*<a href="src/knock_mapi/types/broadcast_send_params.py">params</a>) -> <a href="./src/knock_mapi/types/broadcast_send_response.py">BroadcastSendResponse</a></code>
- <code title="put /v1/broadcasts/{broadcast_key}">client.broadcasts.<a href="./src/knock_mapi/resources/broadcasts.py">upsert</a>(broadcast_key, \*\*<a href="src/knock_mapi/types/broadcast_upsert_params.py">params</a>) -> <a href="./src/knock_mapi/types/broadcast_upsert_response.py">BroadcastUpsertResponse</a></code>
- <code title="put /v1/broadcasts/{broadcast_key}/validate">client.broadcasts.<a href="./src/knock_mapi/resources/broadcasts.py">validate</a>(broadcast_key, \*\*<a href="src/knock_mapi/types/broadcast_validate_params.py">params</a>) -> <a href="./src/knock_mapi/types/broadcast_validate_response.py">BroadcastValidateResponse</a></code>

# Audiences

Types:

```python
from knock_mapi.types import (
    Audience,
    AudienceCondition,
    DynamicAudience,
    StaticAudience,
    AudienceArchiveResponse,
    AudienceUpsertResponse,
    AudienceValidateResponse,
)
```

Methods:

- <code title="get /v1/audiences/{audience_key}">client.audiences.<a href="./src/knock_mapi/resources/audiences.py">retrieve</a>(audience_key, \*\*<a href="src/knock_mapi/types/audience_retrieve_params.py">params</a>) -> <a href="./src/knock_mapi/types/audience.py">Audience</a></code>
- <code title="get /v1/audiences">client.audiences.<a href="./src/knock_mapi/resources/audiences.py">list</a>(\*\*<a href="src/knock_mapi/types/audience_list_params.py">params</a>) -> <a href="./src/knock_mapi/types/audience.py">SyncEntriesCursor[Audience]</a></code>
- <code title="delete /v1/audiences/{audience_key}">client.audiences.<a href="./src/knock_mapi/resources/audiences.py">archive</a>(audience_key, \*\*<a href="src/knock_mapi/types/audience_archive_params.py">params</a>) -> <a href="./src/knock_mapi/types/audience_archive_response.py">AudienceArchiveResponse</a></code>
- <code title="put /v1/audiences/{audience_key}">client.audiences.<a href="./src/knock_mapi/resources/audiences.py">upsert</a>(audience_key, \*\*<a href="src/knock_mapi/types/audience_upsert_params.py">params</a>) -> <a href="./src/knock_mapi/types/audience_upsert_response.py">AudienceUpsertResponse</a></code>
- <code title="put /v1/audiences/{audience_key}/validate">client.audiences.<a href="./src/knock_mapi/resources/audiences.py">validate</a>(audience_key, \*\*<a href="src/knock_mapi/types/audience_validate_params.py">params</a>) -> <a href="./src/knock_mapi/types/audience_validate_response.py">AudienceValidateResponse</a></code>
