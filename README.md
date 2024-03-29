### Paper: 

This is the offical repository of our paper 
 [REBench: Microbenchmarking Framework for Relation Extraction Systems](https://papers.dice-research.org/2022/ISWC_REBench/public.pdf)
 
## REBench: Microbenchmarking Framework for Relation Extraction Systems

REBench is Relation Extraction (RE) Microbenchmarks generation framework which is able to generate customized RE benchmarks . The framework is flexible enough to generate benchmarks of varying sizes and according to the user-defined criteria on the most important RE features to be considered for Relation extraction benchmarking. The generation of benchmarks is achieved by selecting prototypical queries (of a user-defined size and specialized selection criteria) using different clustering algorithms.
### REBench Tutorial
For further details about REBench, RELD, REBench-cli and other related material see our wikis [here](https://github.com/dice-group/REBench/wiki)
### REBench Source Code 
Due to large size of the source code, we have made the code externally available from [here](https://hobbitdata.informatik.uni-leipzig.de/REBench/REBench-cli.zip). Unzip the folder which contains 4 -- Agglomerative, commons-math3, FEASIBLE, QALDBench-Generator -- java projects. REBench-Generator is the main project from where benchmarks can be generated. Note this project requires the other 3 project to be included in the build path. Also all the jar files in the lib folder of FEASIBLE and Agglomerative need to be added into the main project.

### RELD-RDF Dataset
REBench uses RELD-RDF dataset for generating the benchmarks. The RELD-RDF dataset can be downloaded from [here](https://hobbitdata.informatik.uni-leipzig.de/RELD/) in both TTL and JSON-LD format. The online endpoint is also available from [here](http://reld.cs.upb.de:8890/sparql)

 ### Generating Benchmarks from CLI
Download the folder [REBench-cli](https://hobbitdata.informatik.uni-leipzig.de/REBench/REBench-cli.zip) which contains a runable jar REBench.jar, and comtomized benchmark generation query file personalized-query.txt. While using the RELD-RDF locally then you can find the instruction on RELD [homepage](https://manzoorali29.github.io/index.html) to run a local Virtuoso instance otherwise you can use the online endpoint. For step by step guide use our project wikis [here](https://github.com/dice-group/REBench/wiki/REBench-cli-in-Action)
From the folder run the following commands to generate benchmarks of your choice: 
```html
### DBSCAN+Kmeans++ Format ### 
 java -jar REBench.jar -m <method> -n <noRelations> -i <maxNoIterations> -t <noTrialRun> -e <endpointUrl> -q <queryPersonalized> -r <radius> -p <minPts> -o <outputFile>
An example format: 
java -jar REBench.jar   -m db+km++   -n 10   -i 10   -t 10   -e http://localhost:8890/sparql   -q personalized-query.txt   -r 1   -p 1   -o db+km++-10re-benchmark.ttl

### Kmeans++ Format ### 
 java -jar REBench.jar -m <method> -n <noRelations> -i <maxNoIterations> -t <noTrialRun> -e <endpointUrl> -q <queryPersonalized> -o <outputFile>
An example format: 
java -jar REBench.jar   -m km++   -n 10   -i 10   -t 10   -e http://localhost:8890/sparql   -q personalized-query.txt   -o km++-10re-benchmark.ttl


### FEASIBLE Format ### 
 java -jar REBench.jar -m <method> -n <noRelations> -e <endpointUrl> -q <queryPersonalized> -o <outputFile>
An example format: 
java -jar REBench.jar   -m feasible   -n 10  -e http://localhost:8890/sparql   -q personalized-query.txt   -o feasible-10re-benchmark.ttl


### Agglomerative Format ### 
 java -jar REBench.jar -m <method> -n <noRelations> -e <endpointUrl> -q <queryPersonalized> -o <outputFile>
An example format: 
java -jar REBench.jar   -m agglomerative   -n 10  -e http://localhost:8890/sparql   -q personalized-query.txt   -o agglomerative-10re-benchmark.ttl


### FEASIBLE-Exemplars Format ### 
 java -jar REBench.jar -m <method> -n <noRelations> -e <endpointUrl> -q <queryPersonalized> -o <outputFile>
An example format: 
java -jar REBench.jar   -m feasible-exmp   -n 10  -e http://localhost:8890/sparql   -q personalized-query.txt   -o feasible-exmp-10re-benchmark.ttl


### Random Selection Format ### 
 java -jar REBench.jar -m <method> -n <noRelations> -e <endpointUrl> -q <queryPersonalized> -o <outputFile>
An example format: 
java -jar REBench.jar   -m random   -n 10  -e http://localhost:8890/sparql   -q personalized-query.txt   -o random-10re-benchmark.ttl

Where

noRelations = Number of relations in the benchmark
maxNoIterations = Maximum number of iterations for the KMeans++ clustering algorithm. In our evaluation we used maxNoIterations = 10. 
noTrialRun = Number of trial run for the KMeans++ clustering algorithm. In our evaluation we used noTrialRun = 10.
endpointURL = The endpoint URL hosting the RELD dataset containing more than 800 relations. The benchmarks are generated from these relations. 
queryPersonalized = The personalized query for costum benchmark generation
radius = Radius for the queries to be considered as outliers. In our evaluation we used radius = 1
minPts = Minimum points or queries in a cluster. In our evaluation we used min. points = 1
outputFile = The output TTL file where the resulting benchmark will be printed

```
### Generating Benchmarks from Source 
Download the source code from [here](https://hobbitdata.informatik.uni-leipzig.de/benchmarks-data/QALDGen-Source.7z). Unzip the folder which contains 4 -- Agglomerative, commons-math3, FEASIBLE, QALDBench-Generator -- java projects. REBench-Generator is the main project from where benchmarks can be generated. Note this project requires the other 3 project to be included in the build path. Also all the jar files in the lib folder of FEASIBLE and Agglomerative need to be added into the main project.

### Cite
If you use our resources please cite our paper:

```
@inproceedings{ali2022rebench,
  added-at = {2022-08-02T13:01:29.000+0200},
  author = {Ali, Manzoor and Saleem, Muhammad and Ngomo, Axel-Cyrille Ngonga},
  biburl = {https://www.bibsonomy.org/bibtex/2951662997ba515410cd197dcea9174d8/dice-research},
  booktitle = {{ISWC}},
  interhash = {90812a30271e3c79a98f1969a87b3630},
  intrahash = {951662997ba515410cd197dcea9174d8},
  keywords = {3dfed ali dice ngonga porque raki saleem sfb901 speaker},
  publisher = {Springer},
  timestamp = {2022-08-02T13:30:17.000+0200},
  title = {REBench: Microbenchmarking Framework for Relation Extraction Systems},
  url = {https://papers.dice-research.org/2022/ISWC_REBench/public.pdf},
  year = 2022
}
```


### Developers
  * [Manzoor Ali](https://dice-research.org/ManzoorAli) (DICE, University of Paderborn)
  * [Muhammad Saleem](https://sites.google.com/site/saleemsweb/) (AKSW, University of Leipzig) 
  * [Axel-Cyrille Ngonga Ngomo](https://dice-research.org/AxelCyrilleNgongaNgomo) (DICE, University of Paderborn)
