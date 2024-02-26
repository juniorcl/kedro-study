"""
This is a boilerplate pipeline 'test'
generated using Kedro 0.19.1
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import return_greeting


def create_pipeline(**kwargs) -> Pipeline:
    
    return pipeline(
        [
            node(
                func=return_greeting, 
                inputs=None, 
                outputs="my_salutation"
            )
        ]
    )
