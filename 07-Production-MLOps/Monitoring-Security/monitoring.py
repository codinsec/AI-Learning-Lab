"""
Monitoring AI Systems
Tracking latency, tokens, costs, and performance.
"""


def langsmith_tracing():
    """LangSmith for tracing LLM calls."""
    print("=== LangSmith Tracing ===")
    
    print("LangSmith: Observability platform for LLM applications")
    
    print("\nWhat it tracks:")
    print("  - All LLM calls (inputs, outputs)")
    print("  - Latency per call")
    print("  - Token usage")
    print("  - Costs")
    print("  - Errors")
    print("  - Chain/tool execution")
    
    print("\nBenefits:")
    print("  - Debug issues quickly")
    print("  - Optimize prompts")
    print("  - Monitor costs")
    print("  - Track performance")
    print("  - A/B test prompts")
    
    print("\nImplementation:")
    print("""
    from langsmith import traceable
    
    @traceable
    def my_llm_function(prompt):
        response = llm.generate(prompt)
        return response
    """)


def latency_metrics():
    """Tracking latency metrics."""
    print("\n=== Latency Metrics ===")
    
    print("Key latency metrics to track:")
    
    metrics = {
        "P50 (median)": "50% of requests faster than this",
        "P95": "95% of requests faster than this",
        "P99": "99% of requests faster than this",
        "Average": "Mean latency across all requests",
        "Max": "Slowest request",
    }
    
    for metric, description in metrics.items():
        print(f"  {metric}: {description}")
    
    print("\nWhat affects latency:")
    print("  - Model size (larger = slower)")
    print("  - Input length (longer = slower)")
    print("  - Output length (longer = slower)")
    print("  - GPU/CPU load")
    print("  - Network latency (API calls)")
    
    print("\nOptimization:")
    print("  - Use smaller models when possible")
    print("  - Limit max_tokens")
    print("  - Use caching")
    print("  - Optimize prompts")


def token_metrics():
    """Tracking token usage."""
    print("\n=== Token Metrics ===")
    
    print("Token metrics to monitor:")
    
    print("\nPer request:")
    print("  - Input tokens")
    print("  - Output tokens")
    print("  - Total tokens")
    print("  - Cost per request")
    
    print("\nAggregated:")
    print("  - Total tokens per day/week/month")
    print("  - Average tokens per request")
    print("  - Cost per user")
    print("  - Cost per endpoint")
    
    print("\nWhy it matters:")
    print("  - Directly affects costs")
    print("  - Helps optimize prompts")
    print("  - Identifies expensive operations")
    print("  - Budget planning")
    
    print("\nOptimization:")
    print("  - Shorter prompts")
    print("  - Limit max_tokens")
    print("  - Cache common queries")
    print("  - Use cheaper models when appropriate")


def cost_monitoring():
    """Cost monitoring and optimization."""
    print("\n=== Cost Monitoring ===")
    
    print("Track costs at multiple levels:")
    
    print("\nGranularity:")
    print("  - Per request")
    print("  - Per user")
    print("  - Per endpoint")
    print("  - Per model")
    print("  - Per day/week/month")
    
    print("\nCost components:")
    print("  - Input tokens (prompt)")
    print("  - Output tokens (response)")
    print("  - Model pricing (varies by model)")
    print("  - Infrastructure (GPU, compute)")
    
    print("\nCost optimization:")
    print("  - Use cheaper models when possible")
    print("  - Shorter prompts")
    print("  - Limit response length")
    print("  - Cache responses")
    print("  - Batch requests when possible")
    print("  - Monitor and alert on spikes")
    
    print("\nAlerting:")
    print("  - Daily/weekly cost reports")
    print("  - Alerts on cost spikes")
    print("  - Budget thresholds")
    print("  - Per-user cost limits")


def performance_monitoring():
    """Performance monitoring best practices."""
    print("\n=== Performance Monitoring ===")
    
    print("Key metrics to monitor:")
    
    metrics = {
        "Latency": "Response time (P50, P95, P99)",
        "Throughput": "Requests per second",
        "Error rate": "Percentage of failed requests",
        "Token usage": "Input/output tokens",
        "Cost": "Cost per request/user",
        "GPU utilization": "GPU usage percentage",
        "Memory usage": "GPU/CPU memory",
    }
    
    for metric, description in metrics.items():
        print(f"  {metric}: {description}")
    
    print("\nMonitoring tools:")
    print("  - LangSmith: LLM-specific")
    print("  - Prometheus: Metrics collection")
    print("  - Grafana: Visualization")
    print("  - Custom dashboards")
    
    print("\nBest practices:")
    print("  - Set up alerts for anomalies")
    print("  - Track trends over time")
    print("  - Compare different models/configs")
    print("  - Monitor in production")
    print("  - Regular reviews")


if __name__ == "__main__":
    langsmith_tracing()
    latency_metrics()
    token_metrics()
    cost_monitoring()
    performance_monitoring()
    
    print("\n=== Monitoring Best Practices ===")
    print("1. Track all LLM calls (LangSmith)")
    print("2. Monitor latency (P50, P95, P99)")
    print("3. Track token usage and costs")
    print("4. Set up alerts for anomalies")
    print("5. Regular cost reviews")
    print("6. A/B test prompts and measure impact")

