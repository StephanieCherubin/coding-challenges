def countSegments(s):
    '''You are given a string s, return the number of segments in the string. A segment is defined to be a contiguous sequence of non-space characters.'''

    
    # return len(s.split())
    
    
    ssplit = s.split()
    return (len(ssplit))
    
    
print(countSegments("Hello, my name is John")) #5
print(countSegments("Hello")) # 1
print(countSegments("love live! mu'sic forever")) # 4
print(countSegments("Of all the gin joints in all the towns in all the world,   ")) #13
print(countSegments(", , , ,        a, eaefa"))
