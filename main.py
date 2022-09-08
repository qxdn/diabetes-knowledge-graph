import os
import neomodel
import json
from model import (
    Disease,
    Class,
    Reason,
    Pathogenesis,
    Symptom,
    Test,
    Test_items,
    Test_Value,
    Drug,
    Frequency,
    Amount,
    Method,
    Treatment,
    Operation,
    ADE,
    Anatomy,
    Level,
    Duration,
)

NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "123456"
NEO4J_URL = "bolt://{}:{}@localhost:7687".format(NEO4J_USER, NEO4J_PASSWORD)

neomodel.config.DATABASE_URL = NEO4J_URL

jsonDir = './0521_new_format'

filelists = os.listdir(jsonDir)

for filename in filelists:
    filepath = os.path.join(jsonDir,filename)
    with open(filepath, "r", encoding="utf-8") as f:
        jsonobject = json.load(f)

    paragraphs = jsonobject["paragraphs"]
    for paragraph in paragraphs:
        for sentence in paragraph["sentences"]:
            entities = {}
            relations = {}
            with neomodel.db.transaction:
                for entity in sentence["entities"]:
                    '''
                    实体
                    '''
                    entityType = eval(entity["entity_type"])
                    results, meta = neomodel.db.cypher_query(
                        "MATCH (n:%s{name:'%s'}) RETURN n LIMIT 1"
                        % (entity["entity_type"], entity["entity"])
                    )
                    if 0 == len(results):
                        node = entityType(name=entity["entity"])
                        node.save()
                    else:
                        node = entityType.inflate(results[0][0])
                    entities[entity["entity_id"]] = node
                for relation in sentence["relations"]:
                    head = entities[relation['head_entity_id']]
                    tail = entities[relation['tail_entity_id']]
                    eval("head.{}".format(relation['relation_type'])).connect(tail)
            entities.clear()