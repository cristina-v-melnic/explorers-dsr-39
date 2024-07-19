from kedro.pipeline import Pipeline, node, pipeline

from .nodes import get_train_data, get_model, get_pred


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=get_train_data,
                inputs=["train_data","labels"],
                outputs=["data_clean_dt", "X", "y"],
                name="pipeline_part1",
            ),
            node(
                func=get_model,
                inputs=["X","y","params:feats"],
                outputs="model",
                name="model",
            ),
            node(
                func=get_pred,
                inputs=["model","test_data","params:feats"],
                outputs="results",
                name="pred",
            )
        ]
    )
