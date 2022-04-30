from kedro.pipeline import Pipeline, node

from .nodes import *

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=compute_similarity,
                inputs=["input_text", "food_carbon_df", "embeddings_np"],
                outputs="df_food_category",
                name="compute_similarity",
                tags="compute_similarity",
            )
        ]
    )