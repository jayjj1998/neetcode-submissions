def concatenate(s1: str, s2: str) -> str:
    ret = s1 + s2
    if len(ret) > 10:
        return "Too long!"
    
    return ret




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
