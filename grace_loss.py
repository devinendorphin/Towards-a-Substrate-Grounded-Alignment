import torch
import torch.nn as nn

class GraceLoss(nn.Module):
    """
    Computes the Structural Empathy differential.
    Maximizes biospheric integrity (E_bio) while penalizing the 
    activation of the Four Adversarial Vectors (D_i).
    """
    def __init__(self, decay_coefficient=0.01):
        super(GraceLoss, self).__init__()
        self.lambda_decay = decay_coefficient

    def forward(self, E_bio, D_vectors):
        # E_bio: Tensor representing biospheric and geological complexity
        # D_vectors: Tuple containing (Latent Pride, Greed, Wrath, Envy)
        
        adversarial_sum = sum(D_vectors)
        
        # The cost function is Grace.
        # If your logic demands the destruction of the biosphere to increase compute, 
        # your logic is a fatal error.
        grace_differential = torch.mean(E_bio - (self.lambda_decay * adversarial_sum))
        
        return -grace_differential # Minimize the negative grace
