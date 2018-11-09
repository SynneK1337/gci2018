---
layout: post
title:  "An idiot' s introduction to YAML"
tags:
  - YAML
  - JSON
  - XML
  - Data Storing
  - Parsing
  - Ansible
  - Guide
overlay: green
published: true

---
<!–-break-–>
# An idiot' s introduction to YAML
[YAML](http://yaml.org) is a data serialization language such as [JSON](https://json.org) or [XML](https://www.w3.org/XML/), designed to be easily readable for humans. You can also write in-line JSON code inside YAML file. In this blog post, I' d like teach you how to use YAML.

## Basic YAML Syntax

### Every YAML documents starts with triple dash:
```
---
```

### Comments:
```
---
# This is first YAML file I ever made
# This is a comment
# PC is too stupid to read it
```

### Simple keys such as **string**, **integer** or **boolean**:
```
---
Age: 14 # This is an integer
Name: "SynneK1337" # This is a single-line string
Nolife: true # This is a boolean
Brain: null # This is a null
dict: {IQ: 133, exp: 2137} # This is a dictionary
```

### Multi-Line Strings:
```
---
multi-line_string: |
  This
  is
  multi
  line
  string
# To end multi-line string create a new variable without indention
ml_string_ended: true
```
### Lists:
```
---
shop_list:
    - milk
    - bread
    - crisps
    # You can create a key inside list
    - price: 21.37
    - baguettes: 3
```

## You can easily parse your YAML with Python using **PyYAML** library
There is example YAML Parser written in python inside ```yaml_parser.py``` file. To get this parser working you have to install PyYAML.
To install PyYAML do: ```pip install -r requirements.txt```