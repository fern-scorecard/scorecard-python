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
        from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
        from opentelemetry.sdk.resources import SERVICE_NAME, Resource
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
    except ImportError as e:
        print(e)

    try:
        from openinference.instrumentation.bedrock import BedrockInstrumentor
        BedrockInstrumentor().instrument()
    except ImportError:
        pass

    try:
        from openinference.instrumentation.dspy import DSPyInstrumentor
        DSPyInstrumentor().instrument()
    except ImportError:
        pass

    try:
        from openinference.instrumentation.langchain import LangChainInstrumentor
        LangChainInstrumentor().instrument()
    except ImportError:
        pass

    try:
        from openinference.instrumentation.llama_index import LlamaIndexInstrumentor
        LlamaIndexInstrumentor().instrument()
    except ImportError:
        pass

    try:
        from openinference.instrumentation.mistralai import MistralAIInstrumentor
        MistralAIInstrumentor().instrument()
    except ImportError:
        pass

    try:
        from openinference.instrumentation.openai import OpenAIInstrumentor
        OpenAIInstrumentor().instrument()
    except ImportError:
        pass

    provider = TracerProvider(resource=Resource(attributes={SERVICE_NAME: name}))

    if debug:
        # Export the trace to the console.
        console_exporter = ConsoleSpanExporter()
        console_processor = BatchSpanProcessor(span_exporter=console_exporter)
        provider.add_span_processor(console_processor)

    # Export the trace to the Scorecard Telemetry server.
    from urllib.parse import urljoin
    base = scorecard_config.telemetry_url or "https://telemetry.getscorecard.ai"
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
