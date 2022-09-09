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
                    # 需要注意这里要是 属性的实际名
                    node = entityType.nodes.first_or_none(name_=entity["entity"])
                    if None==node:
                        node = entityType(name=entity["entity"])
                        node.save()
                    entities[entity["entity_id"]] = node
                for relation in sentence["relations"]:
                    head = entities[relation['head_entity_id']]
                    tail = entities[relation['tail_entity_id']]
                    eval("head.{}".format(relation['relation_type'])).connect(tail)
            entities.clear()