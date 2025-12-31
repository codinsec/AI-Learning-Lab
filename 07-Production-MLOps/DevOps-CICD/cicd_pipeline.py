"""
CI/CD Pipeline for AI
Automating testing and deployment.
"""


def cicd_concept():
    """Understanding CI/CD for AI."""
    print("=== CI/CD for AI ===")
    
    print("CI/CD: Continuous Integration and Continuous Deployment")
    
    print("\nCI (Continuous Integration):")
    print("  - Automatically test code changes")
    print("  - Run linting and type checking")
    print("  - Run unit tests")
    print("  - Build Docker images")
    
    print("\nCD (Continuous Deployment):")
    print("  - Automatically deploy to production")
    print("  - Canary deployments")
    print("  - Rolling updates")
    print("  - Rollback on failure")


def github_actions_example():
    """GitHub Actions CI/CD example."""
    print("\n=== GitHub Actions CI/CD ===")
    
    workflow_yaml = """
    name: CI/CD Pipeline
    
    on:
      push:
        branches: [ main ]
      pull_request:
        branches: [ main ]
    
    jobs:
      test:
        runs-on: ubuntu-latest
        steps:
        - uses: actions/checkout@v3
        
        - name: Set up Python
          uses: actions/setup-python@v4
          with:
            python-version: '3.10'
        
        - name: Install dependencies
          run: |
            pip install -r requirements.txt
            pip install pytest black mypy
        
        - name: Lint
          run: black --check .
        
        - name: Type check
          run: mypy .
        
        - name: Test
          run: pytest
        
      build:
        needs: test
        runs-on: ubuntu-latest
        steps:
        - uses: actions/checkout@v3
        
        - name: Build Docker image
          run: docker build -t ai-service:${{ github.sha }} .
        
        - name: Push to registry
          run: docker push ai-service:${{ github.sha }}
      
      deploy:
        needs: build
        runs-on: ubuntu-latest
        if: github.ref == 'refs/heads/main'
        steps:
        - name: Deploy to production
          run: |
            kubectl set image deployment/ai-service \\
              ai-service=ai-service:${{ github.sha }}
    """
    
    print("Example GitHub Actions workflow:")
    print(workflow_yaml)
    
    print("\nPipeline stages:")
    print("  1. Test: Lint, type check, unit tests")
    print("  2. Build: Create Docker image")
    print("  3. Deploy: Update Kubernetes deployment")


def canary_deployment():
    """Canary deployment strategy."""
    print("\n=== Canary Deployment ===")
    
    print("Canary: Gradually roll out new version to subset of users")
    
    print("\nProcess:")
    print("  1. Deploy new version to small percentage (e.g., 5%)")
    print("  2. Monitor metrics (latency, errors, cost)")
    print("  3. If metrics good, increase percentage (10%, 25%, 50%)")
    print("  4. Continue until 100%")
    print("  5. If metrics bad, rollback")
    
    print("\nBenefits:")
    print("  - Low risk (only affects small subset)")
    print("  - Early detection of issues")
    print("  - Easy rollback")
    print("  - Gradual validation")
    
    print("\nImplementation:")
    print("  - Use Kubernetes with multiple deployments")
    print("  - Use service mesh (Istio) for traffic splitting")
    print("  - Monitor metrics at each stage")
    print("  - Automated promotion/rollback")


def testing_strategy():
    """Testing strategy for AI systems."""
    print("\n=== Testing Strategy ===")
    
    print("Testing AI systems:")
    
    test_types = {
        "Unit tests": "Test individual functions",
        "Integration tests": "Test API endpoints",
        "Model tests": "Test model outputs (accuracy, latency)",
        "Prompt tests": "Test prompt variations",
        "Security tests": "Test for injection attacks",
        "Load tests": "Test under high load",
    }
    
    for test_type, description in test_types.items():
        print(f"  {test_type}: {description}")
    
    print("\nAI-specific challenges:")
    print("  - Non-deterministic outputs")
    print("  - Expensive to run (API costs)")
    print("  - Hard to assert correctness")
    print("  - Need for golden datasets")
    
    print("\nBest practices:")
    print("  - Mock LLM calls in unit tests")
    print("  - Use deterministic models for testing")
    print("  - Test prompt variations")
    print("  - Monitor production metrics")


if __name__ == "__main__":
    cicd_concept()
    github_actions_example()
    canary_deployment()
    testing_strategy()
    
    print("\n=== CI/CD Best Practices ===")
    print("1. Automate all testing")
    print("2. Build Docker images in CI")
    print("3. Use canary deployments")
    print("4. Monitor after deployment")
    print("5. Have rollback plan")
    print("6. Test in staging first")

