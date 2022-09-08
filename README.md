# 糖尿病知识图谱搭建

在老板的建议下尝试知识图谱搭建，使用公开数据搭建糖尿病知识图谱

# 数据来源
天池[中文糖尿病科研文献实体关系数据集DiaKG](https://tianchi.aliyun.com/dataset/dataDetail?dataId=88836)

# 效果
![图谱](/assert/total.png)

![糖尿病](/assert/diabetes.png)

![糖尿病发病机制](/assert/pathogenesis.png)

# 缺点

- 未做知识融合

# neomodel和py2neo
感觉neomodel虽然看起来很方便，但是实际使用的时候，要预先定义各个类和关系，而且继承的子类的查询存在一堆问题，有时候甚至不如直接写cypher