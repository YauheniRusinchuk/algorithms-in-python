import compare_str

def sub_str(s,substr):
    for i in range(0,len(s)-len(substr)):
        if compare_str.compare(s[i:i+len(substr)],substr):
            print(i)


sub_str('onesupertwo', 'one')            
