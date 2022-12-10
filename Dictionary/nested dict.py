dict1={
    "class":{
            "student":{
                "name":"xyx",
                "marks":{
                    "python":100,
                    "web":90
                }
            }
        }
    }

print(dict1.get("class",{}).get("student",{}).get("marks",{}).get("web"))

print(dict1.get("class",{}).get("student",{}).get("marks",{}).get("python"))