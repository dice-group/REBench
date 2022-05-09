# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from rdflib import Graph, URIRef
from rdflib.namespace import RDFS, SKOS
from SPARQLWrapper import SPARQLWrapper, JSON

with open('readme.txt', 'w') as file:
    sparql = SPARQLWrapper(
        "http://reld.cs.upb.de:8890/sparql"
    )
    sparql.setReturnFormat(JSON)
    f = open("benchmarks/relations.txt", "r")
    for x in f:
        query = "SELECT  distinct ?txt ?sublable ?objlable ?rlbl where {"+x+" <https://reld.dice-research.org/schema/hasSentence> ?sent. "+x+" rdfs:label ?rlbl.  ?sent <https://reld.dice-research.org/schema/hasText> ?txt. ?sent <https://reld.dice-research.org/schema/hasObject> ?obj. ?obj rdfs:label ?objlable. ?sent <https://reld.dice-research.org/schema/hasSubject> ?sub. ?sub rdfs:label ?sublable. }"
        sparql.setQuery(query)
        try:
            ret = sparql.queryAndConvert()
            # final_dict = {}
            # relation_list = []
            for r in ret["results"]["bindings"]:
            #    relation_list.append(r['sublable']["value"])
              #   relation_list.append(r['rlbl']["value"])
              #  relation_list.append(r['objlable']["value"])
                
                # final_dict["text"] = r['txt']["value"]
                #final_dict["triple_list"] = relation_list
            # final_list.append(final_dict)
                file.write(r['rlbl']["value"]+"\t"+ r['txt']["value"] +"\t" + r['sublable']["value"] +"\t" + r['objlable']["value"]+"\n")
    
    # close the file
                #print(r['rlbl']["value"]+"\t"+ r['txt']["value"] +"\t" + r['sublable']["value"] +"\t" + r['objlable']["value"])
        except Exception as e:
            print(e)
    file.close()        


import json
file1 = open('readme.txt', 'r')
Lines = file1.readlines()
 

# tmp = ""
# dict_inside = {}
# triple_list = []
# for line in Lines:
#     line = line.split("\t")
#     text = line[1]
#     triple = [line[2],line[0],line[3]]
#     if text == tmp:
#         triple_list.append(triple)
#     else:
#         triple_list.append(triple)
#         dict_inside["text"] = text
#         dict_inside["triple_list"] = triple_list
#         final_list.append(dict_inside)
#         tmp = text
#         triple_list = []
#         dict_inside = {}

# Strips the newline character
count = 0
final_list = []
for line in Lines:
    triple = []
    dict_both = {}
    line = line.split("\t")
    tmp = line[1]
    if tmp != line[1]:
        pass
    triple.append(line[2])
    if line[0] == "place_of_death":    
        triple.append("/people/deceased_person/"+line[0])
        if count >100:
            continue
    if line[0] == "country":    
        triple.append("/location/administrative_division/country")
        if count >200:
            continue
    if line[0] == "company":    
        triple.append("/business/person/company")
        if count >300:
            continue
    if line[0] == "religion":    
        triple.append("/people/person/religion")
        if count >400:
            continue
    if line[0] == "ethnicity":    
        triple.append("/people/person/ethnicity")
        if count >500:
            continue
    if line[0] == "advisors":    
        triple.append("/business/company/advisors")
        if count >600:
            continue
    if line[0] == "geographic_distribution":    
        triple.append("/people/ethnicity/geographic_distribution")
        if count >700:
            continue
    if line[0] == "people":    
        triple.append("/people/ethnicity/people")
        if count >800:
            continue
    if line[0] == "profession":    
        triple.append("/people/person/profession")
        if count >900:
            continue
    if line[0] == "industry":    
        triple.append("/business/company/industry")
        if count >1000:
            continue
    triple.append(line[3].strip('\n'))
    dict_both['text'] = str(line[1])
    dict_both['triple_list'] = [triple]
    final_list.append(dict_both)
    count = count + 1



print(final_list[0])
with open('data2.txt', 'w') as file:
    for l in final_list:
        file.write("%s\n" % l)
    
    file.close()