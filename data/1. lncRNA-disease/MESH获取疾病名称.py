import requests
import json

# 存储读取的原始疾病名称
disease_original = list()
# 存储未能匹配到 MESH 的原始疾病名称
no_mesh = list()
mesh_name = list()
original_name = list()

# 打开疾病名称原始文件
with open("E://vscode-git//keti//data//disease.csv") as file:
    for line in file:
        disease_original.append(str(line))



for i in disease_original:
    try:
        # 获取网页内容
        html = requests.get('https://meshb-prev.nlm.nih.gov/api/search/record?searchInField=allTerms&sort=&size=20&searchType=allWords&searchMethod=FullWord&q='+'\''+i+'\'')
        # 指定编码格式解码字符串，默认编码为字符串编码
        json_response = html.content.decode()
        # JSON转为字典
        dict_json = json.loads(json_response)
        print(dict_json['hits']['hits'][0]['_source']['DescriptorName']['String']['t'])
        original_name.append(i)
        mesh_name.append(dict_json['hits']['hits'][0]['_source']['DescriptorName']['String']['t'])
    except:
        try:
            # 获取网页内容
            html = requests.get('https://meshb-prev.nlm.nih.gov/api/search/record?searchInField=allTerms&sort=&size=20&searchType=allWords&searchMethod=FullWord&q='+'\''+i+'\'')
            json_response = html.content.decode()
        # JSON转为字典
            dict_json = json.loads(json_response)
            print(dict_json['hits']['hits'][0]['_source']['SupplementalRecordName']['String']['t'])
            original_name.append(i)
            mesh_name.append(dict_json['hits']['hits'][0]['_source']['SupplementalRecordName']['String']['t'])
        except:
            no_mesh.append(i)
print(len(no_mesh))

disease_name = list(zip(original_name, mesh_name))
file = open("E://vscode-git//keti//data//disease-mesh-test.txt", 'a')
for i in disease_name:
    file.write(str(i))
file.close()
print("保存文件成功")
file = open("E://vscode-git//keti//data//disease-nomesh-2.txt", 'a')
for i in no_mesh:
    file.write(str(i))
file.close()
print("保存文件成功")