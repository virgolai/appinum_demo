# -*- coding=utf-8 -*-
import yaml
import inspect


def getData(funcname):

    fileInfo = inspect.stack()[1]
    fileName = fileInfo.filename
    dotIndex = fileName.rfind(".")
    underlineIndex = fileName.rfind("_")
    fileName = fileName[underlineIndex:dotIndex]

    with open('./data/data'+fileName+'.yml', 'r', encoding="utf8") as f:
        data = yaml.load(f)

    # 1 先将我们获取到的所有数据都存放在一个变量当中
    tmpdata = data[funcname]

    # 2 所以此时我们需要使用循环走进它的内心。
    res_arr = list()
    for value in tmpdata.values():
        tmp_arr = list()
        for j in value.values():
            tmp_arr.append(j)

        res_arr.append(tmp_arr)

    return res_arr


# print( getData("search","test_fn3") )

"""
    最外层有一个空的大盒子
        1 {"username": "小明", "password": "xiaoming123"}
          {"username": "小红", "password": "xiaohong123"}
          
        2 { "小明","xiaoming123","小红","xiaohong123" }
            ["小明","xiaoming123","小红","xiaohong123" ]
            
        3 最终大盒子里放的就是： ["小明","xiaoming123","小红","xiaohong123" ]
    
    {
        "test_fn3_1": {
            "username": "小明", 
            "password": "xiaoming123"
        }, 
        "test_fn3_2": {
            "username": "小红", 
            "password": "xiaohong123"
        }
    }

"""