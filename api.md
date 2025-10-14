# Shared Types

```python
from knock_mapi.types import PageInfo
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
)
```

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
    WorkflowBatchStep,
    WorkflowBranchStep,
    WorkflowChannelStep,
    WorkflowDelayStep,
    WorkflowFetchStep,
    WorkflowStep,
    WorkflowThrottleStep,
    WorkflowTriggerWorkflowStep,
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
from knock_mapi.types import ChannelGroup, ChannelGroupRule
```

Methods:

- <code title="get /v1/channel_groups">client.channel_groups.<a href="./src/knock_mapi/resources/channel_groups.py">list</a>(\*\*<a href="src/knock_mapi/types/channel_group_list_params.py">params</a>) -> <a href="./src/knock_mapi/types/channel_group.py">SyncEntriesCursor[ChannelGroup]</a></code>

# Channels

Types:

```python
from knock_mapi.types import (
    Channel,
    ChatChannelSettings,
    EmailChannelSettings,
    InAppFeedChannelSettings,
    PushChannelSettings,
    SMSChannelSettings,
)
```

Methods:

- <code title="get /v1/channels">client.channels.<a href="./src/knock_mapi/resources/channels.py">list</a>(\*\*<a href="src/knock_mapi/types/channel_list_params.py">params</a>) -> <a href="./src/knock_mapi/types/channel.py">SyncEntriesCursor[Channel]</a></code>

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

- <code title="get /v1/variables">client.variables.<a href="./src/knock_mapi/resources/variables.py">list</a>(\*\*<a href="src/knock_mapi/types/variable_list_params.py">params</a>) -> <a href="./src/knock_mapi/types/variable.py">SyncEntriesCursor[Variable]</a></code>

# Guides

Types:

```python
from knock_mapi.types import (
    Guide,
    GuideStep,
    GuideActivateResponse,
    GuideUpsertResponse,
    GuideValidateResponse,
)
```

Methods:

- <code title="get /v1/guides/{guide_key}">client.guides.<a href="./src/knock_mapi/resources/guides.py">retrieve</a>(guide_key, \*\*<a href="src/knock_mapi/types/guide_retrieve_params.py">params</a>) -> <a href="./src/knock_mapi/types/guide.py">Guide</a></code>
- <code title="get /v1/guides">client.guides.<a href="./src/knock_mapi/resources/guides.py">list</a>(\*\*<a href="src/knock_mapi/types/guide_list_params.py">params</a>) -> <a href="./src/knock_mapi/types/guide.py">SyncEntriesCursor[Guide]</a></code>
- <code title="put /v1/guides/{guide_key}/activate">client.guides.<a href="./src/knock_mapi/resources/guides.py">activate</a>(guide_key, \*\*<a href="src/knock_mapi/types/guide_activate_params.py">params</a>) -> <a href="./src/knock_mapi/types/guide_activate_response.py">GuideActivateResponse</a></code>
- <code title="put /v1/guides/{guide_key}">client.guides.<a href="./src/knock_mapi/resources/guides.py">upsert</a>(guide_key, \*\*<a href="src/knock_mapi/types/guide_upsert_params.py">params</a>) -> <a href="./src/knock_mapi/types/guide_upsert_response.py">GuideUpsertResponse</a></code>
- <code title="put /v1/guides/{guide_key}/validate">client.guides.<a href="./src/knock_mapi/resources/guides.py">validate</a>(guide_key, \*\*<a href="src/knock_mapi/types/guide_validate_params.py">params</a>) -> <a href="./src/knock_mapi/types/guide_validate_response.py">GuideValidateResponse</a></code>
