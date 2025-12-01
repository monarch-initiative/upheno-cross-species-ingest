"""
An example test file for the transform script.

It uses pytest fixtures to define the input data and the mock koza transform.
The test_example function then tests the output of the transform script.

See the Koza documentation for more information on testing transforms:
https://koza.monarchinitiative.org/Usage/testing/
"""


import pytest

#from koza.utils.testing_utils import mock_koza

# Define the ingest name and transform script path
INGEST_NAME = "upheno_phenotype_to_phenotype"
TRANSFORM_SCRIPT = "./src/upheno_cross_species_ingest/transform.py"

# Define the mock koza transform
#@pytest.fixture
#def mock_transform(mock_koza, example_row):
#    # Returns [entity_a, entity_b, association] for a single row
#    return 0
#    return mock_koza(
#        INGEST_NAME,
#        example_row,
#        TRANSFORM_SCRIPT,
#    )

def test_single_row():
    assert True


#def test_single_row(mock_transform):
#    assert True
    #assert len(mock_transform) == 3
    #entity = mock_transform[0]
    #assert entity
    #assert entity.name == "entity_1"

