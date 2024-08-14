# Reference
## Testset
<details><summary><code>client.testset.<a href="src/scorecard/testset/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve Testset metadata without Testcase data
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scorecard import Scorecard

client = Scorecard(
    api_key="YOUR_API_KEY",
)
client.testset.get(
    testset_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**testset_id:** `int` — The ID of the Testset to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.testset.<a href="src/scorecard/testset/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a Testset
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scorecard import Scorecard

client = Scorecard(
    api_key="YOUR_API_KEY",
)
client.testset.delete(
    testset_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**testset_id:** `int` — The ID of the Testset to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.testset.<a href="src/scorecard/testset/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new Testset
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scorecard import Scorecard

client = Scorecard(
    api_key="YOUR_API_KEY",
)
client.testset.create(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A description for the testset.
    
</dd>
</dl>

<dl>
<dd>

**using_retrieval:** `typing.Optional[bool]` — Whether or not the testset uses retrieval.
    
</dd>
</dl>

<dl>
<dd>

**custom_schema:** `typing.Optional[CustomSchema]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.testset.<a href="src/scorecard/testset/client.py">read_schema</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read the schema of a Testset
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scorecard import Scorecard

client = Scorecard(
    api_key="YOUR_API_KEY",
)
client.testset.read_schema(
    testset_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**testset_id:** `int` — The ID of the Testset to retrieve the schema from.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.testset.<a href="src/scorecard/testset/client.py">get_testcases</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all Testcases from a Testset
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scorecard import Scorecard

client = Scorecard(
    api_key="YOUR_API_KEY",
)
client.testset.get_testcases(
    testset_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**testset_id:** `int` — The Testset ID to retrieve testcases from.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The offset to start from.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of testcases to return.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Testcase
<details><summary><code>client.testcase.<a href="src/scorecard/testcase/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new Testcase
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scorecard import Scorecard

client = Scorecard(
    api_key="YOUR_API_KEY",
)
client.testcase.create(
    testset_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**testset_id:** `int` — The ID of the Testset to create the Testcase in.
    
</dd>
</dl>

<dl>
<dd>

**user_query:** `typing.Optional[str]` — The user query to be executed.
    
</dd>
</dl>

<dl>
<dd>

**context:** `typing.Optional[str]` — The context to be used while generating the testcase.
    
</dd>
</dl>

<dl>
<dd>

**ideal:** `typing.Optional[str]` — The ideal response to the user query.
    
</dd>
</dl>

<dl>
<dd>

**custom_inputs:** `typing.Optional[
    typing.Dict[str, typing.Optional[TestcaseCreateParamsCustomInputsValue]]
]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_labels:** `typing.Optional[
    typing.Dict[str, typing.Optional[TestcaseCreateParamsCustomLabelsValue]]
]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.testcase.<a href="src/scorecard/testcase/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve Testcase data
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scorecard import Scorecard

client = Scorecard(
    api_key="YOUR_API_KEY",
)
client.testcase.get(
    testcase_id=1,
    testset_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**testcase_id:** `int` — The ID of the Testcase to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**testset_id:** `int` — The ID of the Testset to retrieve the Testcase from.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.testcase.<a href="src/scorecard/testcase/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a Testcase
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scorecard import Scorecard

client = Scorecard(
    api_key="YOUR_API_KEY",
)
client.testcase.delete(
    testcase_id=1,
    testset_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**testcase_id:** `int` — The ID of the Testcase to delete.
    
</dd>
</dl>

<dl>
<dd>

**testset_id:** `int` — The ID of the Testset to delete the Testcase from.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Testrecord
<details><summary><code>client.testrecord.<a href="src/scorecard/testrecord/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve Testrecord metadata
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scorecard import Scorecard

client = Scorecard(
    api_key="YOUR_API_KEY",
)
client.testrecord.get(
    testrecord_id=1,
    run_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**testrecord_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.testrecord.<a href="src/scorecard/testrecord/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new Testrecord
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scorecard import Scorecard

client = Scorecard(
    api_key="YOUR_API_KEY",
)
client.testrecord.create(
    run_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `int` — The ID of the Run to create the Testrecord in.
    
</dd>
</dl>

<dl>
<dd>

**testset_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**testcase_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**user_query:** `typing.Optional[str]` — The user query that was executed for the testrecord.
    
</dd>
</dl>

<dl>
<dd>

**context:** `typing.Optional[str]` — The context that was used while generating the testrecord.
    
</dd>
</dl>

<dl>
<dd>

**response:** `typing.Optional[str]` — The response generated by the model.
    
</dd>
</dl>

<dl>
<dd>

**ideal:** `typing.Optional[str]` — The ideal response.
    
</dd>
</dl>

<dl>
<dd>

**custom_inputs:** `typing.Optional[
    typing.Dict[str, typing.Optional[TestrecordCreateParamsCustomInputsValue]]
]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_outputs:** `typing.Optional[
    typing.Dict[str, typing.Optional[TestrecordCreateParamsCustomOutputsValue]]
]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_labels:** `typing.Optional[
    typing.Dict[str, typing.Optional[TestrecordCreateParamsCustomLabelsValue]]
]` 
    
</dd>
</dl>

<dl>
<dd>

**prompt:** `typing.Optional[str]` — The prompt used to generate the response.
    
</dd>
</dl>

<dl>
<dd>

**model_params:** `typing.Optional[
    typing.Dict[str, typing.Optional[TestrecordCreateParamsModelParamsValue]]
]` — The model parameters used to generate the response.
    
</dd>
</dl>

<dl>
<dd>

**model_debug_info:** `typing.Optional[
    typing.Dict[str, typing.Optional[TestrecordCreateParamsModelDebugInfoValue]]
]` — Debug information generated by Scorecard during the execution of the testrecord.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Run
<details><summary><code>client.run.<a href="src/scorecard/run/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new Run
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scorecard import Scorecard

client = Scorecard(
    api_key="YOUR_API_KEY",
)
client.run.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**testset_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**scoring_config_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**model_params:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Optional. The model parameters to use for this run.
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**prompt_template:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**metrics:** `typing.Optional[typing.Sequence[int]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.run.<a href="src/scorecard/run/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a Run metadata
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scorecard import Scorecard

client = Scorecard(
    api_key="YOUR_API_KEY",
)
client.run.get(
    run_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `int` — The id of the run to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.run.<a href="src/scorecard/run/client.py">update_status</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the status of a run.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scorecard import Scorecard

client = Scorecard(
    api_key="YOUR_API_KEY",
)
client.run.update_status(
    run_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `int` — The id of the run to update.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[RunStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Score
<details><summary><code>client.score.<a href="src/scorecard/score/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a score
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scorecard import Scorecard

client = Scorecard(
    api_key="YOUR_API_KEY",
)
client.score.create(
    run_id=1,
    testrecord_id=1,
    metric_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `int` — The ID of the run that created the testrecord to be scored.
    
</dd>
</dl>

<dl>
<dd>

**testrecord_id:** `int` — The ID of the testrecord to be scored.
    
</dd>
</dl>

<dl>
<dd>

**metric_id:** `int` — The ID of the metric
    
</dd>
</dl>

<dl>
<dd>

**int_score:** `typing.Optional[int]` — Specify integer scores.
    
</dd>
</dl>

<dl>
<dd>

**binary_score:** `typing.Optional[bool]` — Specify boolean scores.
    
</dd>
</dl>

<dl>
<dd>

**reasoning:** `typing.Optional[str]` — The reasoning for the assigned score.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.score.<a href="src/scorecard/score/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a score
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scorecard import Scorecard

client = Scorecard(
    api_key="YOUR_API_KEY",
)
client.score.update(
    run_id=1,
    testrecord_id=1,
    score_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `int` — The run ID that created the test record to be scored.
    
</dd>
</dl>

<dl>
<dd>

**testrecord_id:** `int` — The ID of the testrecord whose score will be updated.
    
</dd>
</dl>

<dl>
<dd>

**score_id:** `int` — The ID of the score to be updated.
    
</dd>
</dl>

<dl>
<dd>

**int_score:** `typing.Optional[int]` — The new integer score to assign.
    
</dd>
</dl>

<dl>
<dd>

**binary_score:** `typing.Optional[bool]` — The new boolean score to assign.
    
</dd>
</dl>

<dl>
<dd>

**reasoning:** `typing.Optional[str]` — The reasoning for the score update.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## RunMetric
<details><summary><code>client.run_metric.<a href="src/scorecard/run_metric/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve metrics associated with a run
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scorecard import Scorecard

client = Scorecard(
    api_key="YOUR_API_KEY",
)
client.run_metric.get(
    run_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `int` — The id of the run to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Traces
<details><summary><code>client.traces.<a href="src/scorecard/traces/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve trace spans
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scorecard import Scorecard

client = Scorecard(
    api_key="YOUR_API_KEY",
)
client.traces.get(
    trace_id="trace_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**trace_id:** `str` — The ID of the trace to retrieve spans from.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Prompt
<details><summary><code>client.prompt.<a href="src/scorecard/prompt/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Two types of prompts can be created - a root prompt or a child prompt (aka Prompt Version in app).

        A root prompt can be created by providing the `name` param, and it will always be tagged as prod.

        A child prompt can be created by providing the `parent_id` param. Note that the `name` param in this case will be ignored as all descendents from a root prompt would share the root's name. `is_prod` can also be provided to configure whether a child should be tagged as prod.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scorecard import Scorecard

client = Scorecard(
    api_key="YOUR_API_KEY",
)
client.prompt.create(
    prompt_template="<system>\nYou are a helpful assistant. Use the provided context to answer the user's query.\n\nContext: {context}\n</system>\n\n<user>\n{user_query}\n</user>",
    parent_id="7ac3cbd5-3b99-4e72-97f3-9cd2e749cace",
    description="Description of the prompt",
    model_params={
        "param1": "value1",
        "param2": 0.1,
        "param3": 100,
        "param4": True,
    },
    is_prod=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**prompt_template:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**model_params:** `typing.Optional[
    typing.Dict[str, typing.Optional[PromptCreateParamsModelParamsValue]]
]` 
    
</dd>
</dl>

<dl>
<dd>

**is_prod:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prompt.<a href="src/scorecard/prompt/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a prompt by id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scorecard import Scorecard

client = Scorecard(
    api_key="YOUR_API_KEY",
)
client.prompt.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the prompt to get.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prompt.<a href="src/scorecard/prompt/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a root prompt and all of its children.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scorecard import Scorecard

client = Scorecard(
    api_key="YOUR_API_KEY",
)
client.prompt.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the root prompt to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prompt.<a href="src/scorecard/prompt/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a prompt.

        `is_prod` tags the provided prompt as the production prompt within the prompt graph.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scorecard import Scorecard

client = Scorecard(
    api_key="YOUR_API_KEY",
)
client.prompt.update(
    id="id",
    is_prod=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the prompt to update.
    
</dd>
</dl>

<dl>
<dd>

**is_prod:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prompt.<a href="src/scorecard/prompt/client.py">get_by_name</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a prod prompt by name
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scorecard import Scorecard

client = Scorecard(
    api_key="YOUR_API_KEY",
)
client.prompt.get_by_name(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name of the prompt.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

