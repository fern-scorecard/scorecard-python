from openai import OpenAI

from .patcher import monkey_patch_openai_chat_completions
from .tracer import (
    RunContextManager,
    ScorecardSessionManager,
    scorecard_function_tracer,
)

__all__ = [
    "scorecard_function_tracer",
    "scorecard_tracer",
    "ScorecardSessionManager",
    "RunContextManager",
]


def scorecard_tracer(client: OpenAI) -> OpenAI:
    monkey_patch_openai_chat_completions(client)
    return client
