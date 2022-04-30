"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline
from ghack2022.pipelines import create_embedding
from ghack2022.pipelines import compute_similarity

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    comp_emb = create_embedding.create_pipeline()
    comp_sim = compute_similarity.create_pipeline()
    
    return {"__default__": comp_emb + comp_sim}
