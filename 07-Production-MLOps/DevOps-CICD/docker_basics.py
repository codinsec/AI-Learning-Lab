"""
Docker for AI Applications
Containerizing AI models and services.
"""


def docker_concept():
    """Understanding Docker for AI."""
    print("=== Docker for AI ===")
    
    print("Docker: Containerize AI applications for consistent deployment")
    
    print("\nBenefits:")
    print("  - Consistent environments")
    print("  - Easy deployment")
    print("  - Isolation")
    print("  - Scalability")
    print("  - Reproducibility")
    
    print("\nUse cases:")
    print("  - Model serving APIs")
    print("  - Training pipelines")
    print("  - Data processing")
    print("  - Development environments")


def dockerfile_example():
    """Example Dockerfile for AI service."""
    print("\n=== Dockerfile Example ===")
    
    dockerfile = """
    # Base image with Python
    FROM python:3.10-slim
    
    # Set working directory
    WORKDIR /app
    
    # Install system dependencies
    RUN apt-get update && apt-get install -y \\
        build-essential \\
        && rm -rf /var/lib/apt/lists/*
    
    # Copy requirements
    COPY requirements.txt .
    
    # Install Python dependencies
    RUN pip install --no-cache-dir -r requirements.txt
    
    # Copy application code
    COPY . .
    
    # Expose port
    EXPOSE 8000
    
    # Run application
    CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
    """
    
    print("Example Dockerfile:")
    print(dockerfile)
    
    print("\nKey components:")
    print("  - Base image (Python)")
    print("  - System dependencies")
    print("  - Python dependencies")
    print("  - Application code")
    print("  - Port exposure")
    print("  - Startup command")


def docker_commands():
    """Essential Docker commands."""
    print("\n=== Docker Commands ===")
    
    commands = {
        "Build image": "docker build -t ai-service .",
        "Run container": "docker run -p 8000:8000 ai-service",
        "List images": "docker images",
        "List containers": "docker ps",
        "Stop container": "docker stop <container_id>",
        "View logs": "docker logs <container_id>",
        "Remove container": "docker rm <container_id>",
        "Remove image": "docker rmi <image_id>",
    }
    
    print("Essential commands:")
    for command, example in commands.items():
        print(f"  {command}: {example}")


def docker_compose():
    """Docker Compose for multi-container apps."""
    print("\n=== Docker Compose ===")
    
    print("Docker Compose: Manage multiple containers")
    
    compose_example = """
    version: '3.8'
    
    services:
      api:
        build: .
        ports:
          - "8000:8000"
        environment:
          - OPENAI_API_KEY=${OPENAI_API_KEY}
        volumes:
          - ./models:/app/models
      
      redis:
        image: redis:alpine
        ports:
          - "6379:6379"
      
      postgres:
        image: postgres:15
        environment:
          - POSTGRES_DB=ai_db
          - POSTGRES_USER=ai_user
          - POSTGRES_PASSWORD=ai_pass
        volumes:
          - postgres_data:/var/lib/postgresql/data
    
    volumes:
      postgres_data:
    """
    
    print("Example docker-compose.yml:")
    print(compose_example)
    
    print("\nCommands:")
    print("  docker-compose up: Start all services")
    print("  docker-compose down: Stop all services")
    print("  docker-compose logs: View logs")
    print("  docker-compose build: Rebuild images")


if __name__ == "__main__":
    docker_concept()
    dockerfile_example()
    docker_commands()
    docker_compose()
    
    print("\n=== Docker Best Practices ===")
    print("1. Use multi-stage builds for smaller images")
    print("2. Don't run as root")
    print("3. Use .dockerignore")
    print("4. Layer caching (order dependencies)")
    print("5. Use specific base image tags")
    print("6. Minimize image size")

