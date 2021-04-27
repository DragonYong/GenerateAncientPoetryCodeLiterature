### RNN基本结构与Char RNN文本生成

===========================
#### 00-项目信息
```
作者：TuringEmmy
时间:2021-04-12 10:27:01
详情：RNN基本结构与Char RNN文本生成，包括故事生成，代码生成英文文本生成
```
#### 01-环境依赖
```
ubuntu18.04
python3.7
tensorflow1.14
```
#### 02-部署步骤
##### 训练

```
sh scripts/gen_code_train.sh    
sh scripts/gen_en_train.sh    
sh scripts/poem_train.sh

```

##### 测试
```
sh scripts/gen_code_test.sh
sh scripts/gen_en_test.sh
sh scripts/poem_test.sh
```

#### 03-目录结构描述
```
.
├── data
│   ├── jay.csv
│   ├── jay.txt
│   ├── jpn.txt
│   ├── linux.txt
│   ├── poetry.csv
│   ├── poetry.txt
│   └── shakespeare.txt
├── model.py
├── __pycache__
│   ├── model.cpython-36.pyc
│   └── read_utils.cpython-36.pyc
├── readme.md
├── read_utils.py
├── requirements.txt
├── sample.py
├── scripts
│   ├── gen_code_test.sh
│   ├── gen_code_train.sh
│   ├── gen_en_test.sh
│   ├── gen_en_train.sh
│   ├── poem_test.sh
│   └── poem_train.sh
├── test.py
└── train.py
```


#### 04-版本更新
##### V1.0.0 版本内容更新
- 包含RNN英文文本生成
- 古诗生成
- 代码生成