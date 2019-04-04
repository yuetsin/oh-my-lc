class Solution:
    def simplifyPath(self, path: str) -> str:
        pathlist = path.split('/')
        prev = None
        ptr = 0
        while ptr < len(pathlist):
            if ptr < 0:
                ptr += 1
                continue
            print("len = %d， ptr = %d" % (len(pathlist), ptr))
            string = pathlist[ptr]
            if string == '' or string == '.':
                del pathlist[ptr]
            elif string == '..':
                try:
                    del pathlist[ptr - 1]
                    del pathlist[ptr - 1]
                    ptr -= 1
                except:
                    pass
            else:
                ptr += 1
        return '/' + '/'.join(pathlist)