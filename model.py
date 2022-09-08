import neomodel
from neomodel import StructuredNode,UniqueIdProperty,StringProperty,Relationship

class BaseModel(StructuredNode):
    __abstract_node__ = True

    id_ = UniqueIdProperty()
    name_ = StringProperty(db_property='name',unique_index=True)

    @property
    def name(self):
        return self.name_

    @name.setter
    def name(self,value):
        self.name_ = value


class Disease(BaseModel):
    '''
    疾病
    '''
    Test_items_Disease = Relationship('Test_items','检查指标')
    Treatment_Disease = Relationship('Treatment','非药治疗')
    Class_Disease = Relationship('Class','疾病的分期分型')
    Anatomy_Disease = Relationship('Anatomy','部位')
    Drug_Disease = Relationship('Drug','药物')
    Reason_Disease = Relationship('Reason','病因')
    Symptom_Disease = Relationship('Symptom','临床表现')
    Operation_Disease = Relationship('Operation','手术')
    Test_Disease = Relationship('Test','检验方法')
    Pathogenesis_Disease = Relationship('Pathogenesis','发病机制')
    ADE_Disease = Relationship('ADE','不良反应')


class Class(BaseModel):
    '''
    疾病的分期分型
    '''
    Class_Disease = Relationship('Disease','疾病的分期分型')

class Reason(BaseModel):
    '''
    病因
    '''
    Reason_Disease = Relationship('Disease','病因')

class Pathogenesis(BaseModel):
    '''
    发病机制
    '''
    Pathogenesis_Disease = Relationship('Disease','发病机制')

class Symptom(BaseModel):
    '''
    临床表现
    '''
    Symptom_Disease = Relationship('Disease','临床表现')

class Test(BaseModel):
    '''
    检验方法
    '''
    Test_Disease = Relationship('Disease','检验方法')

class Test_items(BaseModel):
    '''
    检查指标
    '''
    Test_items_Disease = Relationship('Disease','检查指标')

class Test_Value(BaseModel):
    '''
    检查指标值
    '''
    pass

class Drug(BaseModel):
    '''
    药物名称
    '''
    Drug_Disease = Relationship('Disease','药物')
    ADE_Drug = Relationship('ADE','不良反应')
    Amount_Drug = Relationship("Amount",'用药剂量')
    Method_Drug = Relationship('Method','用药方法')
    Frequency_Drug = Relationship('Frequency','用药频率')
    Duration_Drug = Relationship('Duration','持续时间')

class Frequency(BaseModel):
    '''
    用药频率
    '''
    Frequency_Drug = Relationship('Drug','用药频率')

class Amount(BaseModel):
    '''
    用药剂量
    '''
    Amount_Drug = Relationship("Drug",'用药剂量')

class Method(BaseModel):
    '''
    用药方法
    '''
    Method_Drug = Relationship('Drug','用药方法')

class Treatment(BaseModel):
    '''
    非药物治疗
    '''
    Treatment_Disease = Relationship('Disease','非药治疗')

class Operation(BaseModel):
    '''
    手术
    '''
    Operation_Disease = Relationship('Disease','手术')

class ADE(BaseModel):
    '''
    不良反应
    '''
    ADE_Drug = Relationship('Drug','不良反应')
    ADE_Disease = Relationship('Disease','不良反应')

class Anatomy(BaseModel):
    '''
    部位
    '''
    Anatomy_Disease = Relationship('Disease','部位')

class Level(BaseModel):
    pass

class Duration(BaseModel):
    '''
    持续时间
    '''
    Duration_Drug = Relationship('Drug','持续时间')