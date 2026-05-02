import uuid
from typing import Any

import koza
from biolink_model.datamodel.pydanticmodel_v2 import (
    AgentTypeEnum,
    Association,
    KnowledgeLevelEnum,
    PhenotypicFeature,
)
from koza import KozaTransform


INFORES_UPHENO = "infores:upheno"


@koza.transform_record()
def transform_record(koza_transform: KozaTransform, row: dict[str, Any]) -> list:
    subject_phenotype = PhenotypicFeature(
        id=row["subject_id"],
        name=row["subject_label"] or None,
        category=["biolink:PhenotypicFeature"],
    )
    object_phenotype = PhenotypicFeature(
        id=row["object_id"],
        name=row["object_label"] or None,
        category=["biolink:PhenotypicFeature"],
    )
    association = Association(
        id=f"urn:uuid:{uuid.uuid4()}",
        subject=subject_phenotype.id,
        predicate="biolink:homologous_to",
        original_predicate=row["predicate_id"],
        object=object_phenotype.id,
        subject_category="biolink:PhenotypicFeature",
        object_category="biolink:PhenotypicFeature",
        category=["biolink:Association"],
        primary_knowledge_source=INFORES_UPHENO,
        knowledge_source="upheno-cross-species.sssom.tsv",
        has_attribute=[
            f'"mapping_justification":"{row["mapping_justification"]}"',
            f'"subject_source":"{row["subject_source"]}"',
            f'"object_source":"{row["object_source"]}"',
        ],
        knowledge_level=KnowledgeLevelEnum.prediction,
        agent_type=AgentTypeEnum.data_analysis_pipeline,
    )
    return [subject_phenotype, object_phenotype, association]
