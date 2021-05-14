class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        results = defaultdict(int)
        for i in cpdomains:
            i = list(i.split(" "))
            n = int(i[0])
            web = i[1].split(".")
            for i in range(len(web)):
                results[".".join(web[i:])] += n
                
        return ["{} {}".format(count, name) for name, count in results.items()]

        