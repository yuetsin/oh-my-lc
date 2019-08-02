class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        list1 = [int(v_str) for v_str in version1.split('.')]
        list2 = [int(v_str) for v_str in version2.split('.')]
        counter = 0
        while True:
            if len(list1) > counter and len(list2) > counter:
                v_id1 = list1[counter]
                v_id2 = list2[counter]
                if v_id1 == v_id2:
                    counter += 1
                    continue
                elif v_id1 < v_id2:
                    return -1
                else:
                    return 1
            else:
                if len(list1) > counter:
                    if list1[counter] == 0:
                        counter += 1
                        continue
                    else:
                        return 1
                elif len(list2) > counter:
                    if list2[counter] == 0:
                        counter += 1
                        continue
                    else:
                        return -1
                else:
                    return 0
