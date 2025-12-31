"""
FastAPI Model Serving
Building production-ready API endpoints for AI models.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import time


# Pydantic models for request/response
class ChatRequest(BaseModel):
    message: str
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 100


class ChatResponse(BaseModel):
    response: str
    tokens_used: int
    latency_ms: float


def create_fastapi_app():
    """Create FastAPI app for model serving."""
    print("=== FastAPI Model Serving ===")
    
    app = FastAPI(title="AI Model API", version="1.0.0")
    
    @app.get("/health")
    async def health_check():
        """Health check endpoint."""
        return {"status": "healthy", "service": "ai-model-api"}
    
    @app.post("/chat", response_model=ChatResponse)
    async def chat(request: ChatRequest):
        """
        Chat endpoint for LLM inference.
        In production, this would call your actual model.
        """
        start_time = time.time()
        
        # Simulate model inference
        # In production: response = model.generate(request.message)
        response_text = f"Response to: {request.message[:50]}..."
        tokens_used = len(response_text.split())
        
        latency_ms = (time.time() - start_time) * 1000
        
        return ChatResponse(
            response=response_text,
            tokens_used=tokens_used,
            latency_ms=latency_ms
        )
    
    print("FastAPI app structure:")
    print("  - Health check endpoint")
    print("  - Chat endpoint with request/response models")
    print("  - Error handling")
    print("  - Type validation with Pydantic")
    
    return app


def streaming_responses():
    """Server-Sent Events (SSE) for streaming."""
    print("\n=== Streaming Responses (SSE) ===")
    
    print("Streaming allows sending tokens as they're generated:")
    
    print("""
    from sse_starlette.sse import EventSourceResponse
    
    @app.post("/chat/stream")
    async def chat_stream(request: ChatRequest):
        async def generate():
            # Simulate streaming tokens
            tokens = ["Hello", " there", "!", " How", " can", " I", " help?"]
            for token in tokens:
                yield {"data": token}
                await asyncio.sleep(0.1)  # Simulate generation delay
        
        return EventSourceResponse(generate())
    """)
    
    print("\nBenefits:")
    print("  - Lower perceived latency")
    print("  - Better user experience")
    print("  - Can cancel mid-generation")
    
    print("\nUse cases:")
    print("  - Chat interfaces")
    print("  - Long responses")
    print("  - Real-time applications")


def error_handling():
    """Error handling in production APIs."""
    print("\n=== Error Handling ===")
    
    print("Production APIs need robust error handling:")
    
    print("""
    from fastapi import HTTPException
    
    @app.post("/chat")
    async def chat(request: ChatRequest):
        try:
            # Validate input
            if len(request.message) > 2000:
                raise HTTPException(
                    status_code=400,
                    detail="Message too long (max 2000 characters)"
                )
            
            # Call model
            response = model.generate(request.message)
            return response
            
        except ModelError as e:
            raise HTTPException(
                status_code=503,
                detail="Model service unavailable"
            )
        except Exception as e:
            # Log error
            logger.error(f"Unexpected error: {e}")
            raise HTTPException(
                status_code=500,
                detail="Internal server error"
            )
    """)
    
    print("\nBest practices:")
    print("  - Validate all inputs")
    print("  - Handle model errors gracefully")
    print("  - Return appropriate HTTP status codes")
    print("  - Log errors for debugging")
    print("  - Don't expose internal errors to users")


def rate_limiting():
    """Rate limiting for API protection."""
    print("\n=== Rate Limiting ===")
    
    print("Rate limiting prevents abuse:")
    
    print("""
    from slowapi import Limiter, _rate_limit_exceeded_handler
    from slowapi.util import get_remote_address
    
    limiter = Limiter(key_func=get_remote_address)
    app.state.limiter = limiter
    
    @app.post("/chat")
    @limiter.limit("10/minute")
    async def chat(request: ChatRequest):
        # Endpoint limited to 10 requests per minute per IP
        return response
    """)
    
    print("\nRate limiting strategies:")
    print("  - Per IP address")
    print("  - Per user/API key")
    print("  - Per endpoint")
    print("  - Token-based (cost-based)")
    
    print("\nBenefits:")
    print("  - Prevents abuse")
    print("  - Controls costs")
    print("  - Ensures fair usage")


if __name__ == "__main__":
    create_fastapi_app()
    streaming_responses()
    error_handling()
    rate_limiting()
    
    print("\n=== FastAPI Best Practices ===")
    print("1. Use Pydantic for request/response validation")
    print("2. Implement health checks")
    print("3. Add streaming for better UX")
    print("4. Handle errors gracefully")
    print("5. Implement rate limiting")
    print("6. Add logging and monitoring")
    print("7. Use async/await for I/O operations")

