from .score_config import STANCE_SCORE

def get_stance_score(stance: str) -> int:
    return STANCE_SCORE.get(stance, 0)
