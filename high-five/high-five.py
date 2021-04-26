from operator import itemgetter

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        ids = {}
        # iterate through items and create dict with id:[scores]
        for i in items:
            if i[0] not in ids:
                ids[i[0]] = [i[1]]
            else:
                ids[i[0]].append(i[1])
                
        returnList = []
        for i in ids:
            ids[i].sort(reverse = True)
            top5 = ids[i][:5] # grab 0 to 4
            returnList.append([i, sum(top5)//5])
        returnList.sort()
        return returnList
