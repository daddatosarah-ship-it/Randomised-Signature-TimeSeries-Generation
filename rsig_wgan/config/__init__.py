import yaml
import torch.nn as nn
from typing import Any
from pathlib import Path
from omegaconf import OmegaConf

def load_config() -> dict[str, Any]:
    """
    return: 
        Dictionary with the config
    """
    
    #vediamo se esiste nella directory un file chiamato config.yml
    try:
        config = OmegaConf.load(Path(__file__).parent / "config.yml")   #OmegaConf libreria più evoluta rispetto a yaml,permette di accedere ai campi come attributi 
        return config
    except FileNotFoundError:
        print(f"Error: The file at config.yml was not found.")
        return None
    except yaml.YAMLError as e:
        print(f"Error reading YAML file: {e}")
        return None
    
activation_mapping = {"Sigmoid": nn.Sigmoid(), "Tanh": nn.Tanh()}   #Serve per mappare un nome stringa preso dal file config.yml a una vera attivazione PyTorch
    
__all__ = ["load_config", "activation_mapping"]   #quando qualcuno fa: from rsig_wgan.config import * verranno importati solo questi due simboli


