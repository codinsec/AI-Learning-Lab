"""
Kubernetes Basics for AI
Deploying AI services on Kubernetes.
"""


def kubernetes_concept():
    """Understanding Kubernetes."""
    print("=== Kubernetes for AI ===")
    
    print("Kubernetes: Container orchestration platform")
    
    print("\nBenefits:")
    print("  - Auto-scaling")
    print("  - Load balancing")
    print("  - Self-healing")
    print("  - Rolling updates")
    print("  - Resource management")
    
    print("\nUse cases:")
    print("  - Production deployments")
    print("  - High availability")
    print("  - Auto-scaling")
    print("  - Multi-region")
    
    print("\nKey concepts:")
    print("  - Pod: Smallest deployable unit")
    print("  - Service: Network access to pods")
    print("  - Deployment: Manages pod replicas")
    print("  - ConfigMap: Configuration data")
    print("  - Secret: Sensitive data")


def deployment_example():
    """Example Kubernetes deployment."""
    print("\n=== Kubernetes Deployment ===")
    
    deployment_yaml = """
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: ai-service
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: ai-service
      template:
        metadata:
          labels:
            app: ai-service
        spec:
          containers:
          - name: ai-service
            image: ai-service:latest
            ports:
            - containerPort: 8000
            resources:
              requests:
                memory: "2Gi"
                cpu: "1"
              limits:
                memory: "4Gi"
                cpu: "2"
            env:
            - name: OPENAI_API_KEY
              valueFrom:
                secretKeyRef:
                  name: api-secrets
                  key: openai-key
    """
    
    print("Example deployment:")
    print(deployment_yaml)
    
    print("\nKey features:")
    print("  - Replicas: 3 instances")
    print("  - Resource limits")
    print("  - Environment variables from secrets")
    print("  - Auto-restart on failure")


def service_example():
    """Kubernetes service for load balancing."""
    print("\n=== Kubernetes Service ===")
    
    service_yaml = """
    apiVersion: v1
    kind: Service
    metadata:
      name: ai-service
    spec:
      selector:
        app: ai-service
      ports:
      - protocol: TCP
        port: 80
        targetPort: 8000
      type: LoadBalancer
    """
    
    print("Example service:")
    print(service_yaml)
    
    print("\nService types:")
    print("  - ClusterIP: Internal access")
    print("  - NodePort: External access via node")
    print("  - LoadBalancer: Cloud load balancer")
    print("  - Ingress: HTTP/HTTPS routing")


def auto_scaling():
    """Horizontal Pod Autoscaler."""
    print("\n=== Auto-Scaling ===")
    
    hpa_yaml = """
    apiVersion: autoscaling/v2
    kind: HorizontalPodAutoscaler
    metadata:
      name: ai-service-hpa
    spec:
      scaleTargetRef:
        apiVersion: apps/v1
        kind: Deployment
        name: ai-service
      minReplicas: 2
      maxReplicas: 10
      metrics:
      - type: Resource
        resource:
          name: cpu
          target:
            type: Utilization
            averageUtilization: 70
    """
    
    print("Horizontal Pod Autoscaler:")
    print(hpa_yaml)
    
    print("\nScaling triggers:")
    print("  - CPU utilization")
    print("  - Memory usage")
    print("  - Custom metrics")
    print("  - Request rate")
    
    print("\nBenefits:")
    print("  - Scale up during high load")
    print("  - Scale down to save costs")
    print("  - Automatic adjustment")


if __name__ == "__main__":
    kubernetes_concept()
    deployment_example()
    service_example()
    auto_scaling()
    
    print("\n=== Kubernetes Best Practices ===")
    print("1. Use resource requests and limits")
    print("2. Set up health checks (liveness/readiness)")
    print("3. Use ConfigMaps for configuration")
    print("4. Use Secrets for sensitive data")
    print("5. Implement auto-scaling")
    print("6. Use rolling updates")
    print("7. Monitor resource usage")

