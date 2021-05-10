class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []
        
        for log in logs:
            ID = log.split()[1] #skips over identifier, and checks log.  if log contains num, then its a dig, else letter
            if ID.isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        letters.sort(key = lambda x: x.split()[0])
        letters.sort(key = lambda x: x.split()[1:])
        result = letters + digits
        return result
        