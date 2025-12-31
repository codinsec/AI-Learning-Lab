"""
Pretraining vs Fine-tuning
Understanding transfer learning and adaptation.
"""

import torch
import torch.nn as nn


def pretrained_model_example():
    """Using a pretrained model."""
    print("=== Pretrained Model ===")
    
    # Simulate a pretrained model (in practice, load from torchvision, etc.)
    class PretrainedModel(nn.Module):
        def __init__(self):
            super(PretrainedModel, self).__init__()
            # Pretrained layers (frozen)
            self.feature_extractor = nn.Sequential(
                nn.Linear(100, 50),
                nn.ReLU(),
                nn.Linear(50, 25)
            )
            # Task-specific head
            self.classifier = nn.Linear(25, 10)
        
        def forward(self, x):
            features = self.feature_extractor(x)
            output = self.classifier(features)
            return output
    
    model = PretrainedModel()
    
    # Freeze pretrained layers (don't update during fine-tuning)
    for param in model.feature_extractor.parameters():
        param.requires_grad = False
    
    print("Pretrained layers (frozen):")
    for name, param in model.named_parameters():
        if 'feature_extractor' in name:
            print(f"  {name}: requires_grad={param.requires_grad}")
    
    print("\nTask-specific layers (trainable):")
    for name, param in model.named_parameters():
        if 'classifier' in name:
            print(f"  {name}: requires_grad={param.requires_grad}")


def fine_tuning_example():
    """Fine-tuning a pretrained model."""
    print("\n=== Fine-tuning ===")
    
    class PretrainedModel(nn.Module):
        def __init__(self):
            super(PretrainedModel, self).__init__()
            self.features = nn.Sequential(
                nn.Linear(100, 50),
                nn.ReLU(),
                nn.Linear(50, 25)
            )
            self.classifier = nn.Linear(25, 10)
    
    model = PretrainedModel()
    
    # Strategy 1: Freeze all, train only classifier
    print("Strategy 1: Freeze pretrained, train only classifier")
    for param in model.features.parameters():
        param.requires_grad = False
    
    # Strategy 2: Unfreeze last layer, train classifier + last feature layer
    print("\nStrategy 2: Unfreeze last feature layer")
    # Unfreeze last layer of features
    for param in list(model.features.parameters())[-2:]:  # Last layer
        param.requires_grad = True
    
    # Strategy 3: Full fine-tuning (unfreeze all)
    print("\nStrategy 3: Full fine-tuning (unfreeze all)")
    for param in model.parameters():
        param.requires_grad = True
    
    print("\nFine-tuning strategies:")
    print("1. Freeze all: Fast, less flexible")
    print("2. Unfreeze last layers: Balanced")
    print("3. Full fine-tuning: Slow, most flexible")


def lora_concept():
    """LoRA (Low-Rank Adaptation) concept."""
    print("\n=== LoRA (Low-Rank Adaptation) ===")
    
    # LoRA: Instead of updating all weights, add small trainable matrices
    class LoRALayer(nn.Module):
        def __init__(self, original_layer, rank=4):
            super(LoRALayer, self).__init__()
            self.original = original_layer
            # Freeze original weights
            for param in self.original.parameters():
                param.requires_grad = False
            
            # LoRA matrices (much smaller)
            in_features = original_layer.in_features
            out_features = original_layer.out_features
            self.lora_A = nn.Parameter(torch.randn(rank, in_features))
            self.lora_B = nn.Parameter(torch.zeros(out_features, rank))
        
        def forward(self, x):
            # Original output
            original_out = self.original(x)
            # LoRA adaptation: x @ A^T @ B^T
            lora_out = torch.matmul(torch.matmul(x, self.lora_A.T), self.lora_B.T)
            return original_out + lora_out
    
    # Example: Adapt a linear layer
    original_layer = nn.Linear(100, 50)
    lora_layer = LoRALayer(original_layer, rank=4)
    
    print(f"Original layer parameters: {sum(p.numel() for p in original_layer.parameters())}")
    print(f"LoRA parameters: {sum(p.numel() for p in lora_layer.lora_A.parameters()) + sum(p.numel() for p in lora_layer.lora_B.parameters())}")
    print("\nLoRA benefits:")
    print("- Much fewer parameters to train")
    print("- Faster training")
    print("- Less memory usage")
    print("- Can adapt large models efficiently")


def inference_vs_training():
    """Inference vs Training differences."""
    print("\n=== Inference ≠ Training ===")
    
    model = nn.Sequential(
        nn.Linear(10, 20),
        nn.ReLU(),
        nn.Linear(20, 5)
    )
    
    x = torch.randn(1, 10)
    
    # Training mode
    model.train()
    print("Training mode:")
    print(f"  Dropout active: {hasattr(model, 'dropout')}")
    print(f"  BatchNorm uses batch statistics")
    print(f"  Gradients computed")
    
    with torch.enable_grad():
        y_train = model(x)
        print(f"  Output requires grad: {y_train.requires_grad}")
    
    # Inference mode
    model.eval()
    print("\nInference mode:")
    print(f"  Dropout inactive (if present)")
    print(f"  BatchNorm uses running statistics")
    print(f"  No gradients computed")
    
    with torch.no_grad():
        y_inference = model(x)
        print(f"  Output requires grad: {y_inference.requires_grad}")
        print(f"  Memory efficient, faster")
    
    print("\nKey differences:")
    print("Training: model.train(), gradients, dropout, batch statistics")
    print("Inference: model.eval(), no gradients, no dropout, running statistics")


if __name__ == "__main__":
    pretrained_model_example()
    fine_tuning_example()
    lora_concept()
    inference_vs_training()

