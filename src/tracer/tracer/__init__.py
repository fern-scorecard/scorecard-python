from openai import OpenAI

from .patcher import monkey_patch_openai_chat_completions
from .tracer import scorecard_function_tracer, ScorecardSessionManager, RunContextManager
from .database import TestSet, TestCase

__all__ = ['scorecard_function_tracer', 
           'scorecard_tracer', 
           'ScorecardSessionManager', 
           'RunContextManager']


def scorecard_tracer(client: OpenAI) -> OpenAI:
    monkey_patch_openai_chat_completions(client)
    return client
