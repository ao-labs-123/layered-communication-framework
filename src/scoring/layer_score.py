from .score_config import LAYER_SCORE

def get_layer_score(layer: str) -> int:
    return LAYER_SCORE.get(layer, 0)