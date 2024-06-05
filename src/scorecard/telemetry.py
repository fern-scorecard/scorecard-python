from importlib.metadata import metadata
import sys


# pylint: disable=import-outside-toplevel
def setup(name, scorecard_config, debug=False):
    """
    Sets up a default telemetry configuration for Scorecard.
    Parameters:
        - name: string. The name of the service. e.g. your application name
        - scorecard_config.telemetry_url: string.
        Your tracing endpoint. e.g. https://telemetry.getscorecard.ai
        - scorecard_config.telemetry_key: string.
        You can get this value from https://app.getscorecard.ai/settings
        - debug: bool. Whether or not to log traces to the console.
    """

    try:
        from opentelemetry import trace
        from opentelemetry.exporter.otlp.proto.http.trace_exporter import (
            OTLPSpanExporter,
        )
        from opentelemetry.sdk.resources import SERVICE_NAME, Resource
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import (
            BatchSpanProcessor,
            ConsoleSpanExporter,
        )
    except ModuleNotFoundError:
        available_extras = metadata("scorecard-ai").get_all("Provides-Extra")
        output_string = ""
        if available_extras is not None:
            available_extras = "".join(
                map(lambda extra: f"- {extra}\n", available_extras)
            )
            output_string = f"\n\nAvailable extras:\n{available_extras}"

        print(
            f'In order to use Scorecard telemetry, be sure to install the correct PEP 508 extras. For example:\n\npip install scorecard-ai[telemetry,instrument-openai]\npoetry add scorecard-ai --extras "telemetry instrument-openai"{output_string}'
        )

        output_exception = ModuleNotFoundError(name="scorecard-ai[telemetry]")
        output_exception.msg = f"{output_exception.name} not installed."
        sys.tracebacklimit = 0
        raise output_exception from None

    try:
        from openinference.instrumentation.bedrock import BedrockInstrumentor

        BedrockInstrumentor().instrument()
    except ModuleNotFoundError:
        pass

    try:
        from openinference.instrumentation.dspy import DSPyInstrumentor

        DSPyInstrumentor().instrument()
    except ModuleNotFoundError:
        pass

    try:
        from openinference.instrumentation.langchain import LangChainInstrumentor

        LangChainInstrumentor().instrument()
    except ModuleNotFoundError:
        pass

    try:
        from openinference.instrumentation.llama_index import LlamaIndexInstrumentor

        LlamaIndexInstrumentor().instrument()
    except ModuleNotFoundError:
        pass

    try:
        from openinference.instrumentation.mistralai import MistralAIInstrumentor

        MistralAIInstrumentor().instrument()
    except ModuleNotFoundError:
        pass

    try:
        from openinference.instrumentation.openai import OpenAIInstrumentor

        OpenAIInstrumentor().instrument()
    except ModuleNotFoundError:
        pass

    provider = TracerProvider(resource=Resource(attributes={SERVICE_NAME: name}))

    if debug:
        # Export the trace to the console.
        console_exporter = ConsoleSpanExporter()
        console_processor = BatchSpanProcessor(span_exporter=console_exporter)
        provider.add_span_processor(console_processor)

    # Export the trace to the Scorecard Telemetry server.
    from urllib.parse import urljoin

    base = scorecard_config.telemetry_url or "https://telemetry.getscorecard.ai:4318"
    otlp_exporter = OTLPSpanExporter(
        endpoint=urljoin(base, "/v1/traces"),
        headers={"Authorization": f"Bearer {scorecard_config.telemetry_key}"},
    )
    otlp_processor = BatchSpanProcessor(span_exporter=otlp_exporter)
    provider.add_span_processor(otlp_processor)

    trace.set_tracer_provider(provider)
    tracer = trace.get_tracer(
        instrumenting_module_name=__name__, tracer_provider=provider
    )

    return tracer
