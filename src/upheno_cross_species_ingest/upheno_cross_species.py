import koza

from typing import Any

from biolink_model.datamodel.pydanticmodel_v2 import (
    PhenotypicFeature,
    Association,
    KnowledgeLevelEnum,
    AgentTypeEnum,
)  # Replace * with any necessary data classes from the Biolink Model

from koza.model.graphs import KnowledgeGraph
from bmt.pydantic import build_association_knowledge_sources
from bmt.pydantic import entity_id

INFORES_UPHENO = "infores:upheno"

@koza.transform_record(tag=None)
def transform_upheno(
        koza_transform: koza.KozaTransform,
        row: dict[str, Any]
) -> KnowledgeGraph | None:
    #if(row['subject_source']=="obo:upheno" or row['object_source']=="obo:upheno"):
    #    continue
    
    subject_phenotype_entity = PhenotypicFeature(
        id=row["subject_id"],
        name=row["subject_label"],
        category=["biolink:PhenotypicFeature"],
    )
    object_phenotype_entity = PhenotypicFeature(
        id=row["object_id"],
        name=row["object_label"],
        category=["biolink:PhenotypicFeature"],
    )
    association = Association(
        id=entity_id(),
        subject=subject_phenotype_entity.id,
        predicate="biolink:homologous_to",
        original_predicate=row["predicate_id"],
        object=object_phenotype_entity.id,
        subject_category="biolink:PhenotypicFeature",
        object_category="biolink:PhenotypicFeature",
        category=["biolink:Association"],
        primary_knowledge_source="infores:upheno",
        knowledge_source="upheno-cross-species.sssom.tsv",
        has_attribute=[f'"mapping_justification":"{row["mapping_justification"]}"',f'"subject_source":"{row["subject_source"]}"',f'"object_source":"{row["object_source"]}"'],
        knowledge_level=KnowledgeLevelEnum.prediction,
        agent_type=AgentTypeEnum.data_analysis_pipeline ,
    )
    return KnowledgeGraph(nodes=[subject_phenotype_entity,object_phenotype_entity], edges=[association])