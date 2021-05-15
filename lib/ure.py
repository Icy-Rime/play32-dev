import re

def __process_regex(regex_str):
    regex_str = regex_str.replace("\\b", "")
    regex_str = regex_str.replace("\\B", "")
    regex_str = regex_str.replace("\\r", "r")
    regex_str = regex_str.replace("\\n", "n")
    regex_str = regex_str.replace("\\t", "t")
    regex_str = regex_str.replace("\r", "\\r")
    regex_str = regex_str.replace("\n", "\\n")
    regex_str = regex_str.replace("\t", "\\t")
    return regex_str

def compile(regex_str, flags=None):
    regex_str = __process_regex(regex_str)
    return re.compile(regex_str)

def match(regex_str, string):
    regex_str = __process_regex(regex_str)
    return re.match(regex_str, string)

def search(regex_str, string):
    regex_str = __process_regex(regex_str)
    return re.search(regex_str, string)

def sub(regex_str, replace, string, count=0, flags=0):
    regex_str = __process_regex(regex_str)
    return re.sub(regex_str, replace, string, count)
