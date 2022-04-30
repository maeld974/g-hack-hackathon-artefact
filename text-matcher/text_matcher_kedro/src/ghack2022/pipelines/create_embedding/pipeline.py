from kedro.pipeline import Pipeline, node

from .nodes import *

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=create_embedding,
                inputs="food_carbon_df",
                outputs="embeddings_np",
                name="create_embedding",
                tags="preprocesing",
            )
        ]
    )