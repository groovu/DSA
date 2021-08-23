class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        def dfs(remain, path, results):

            if remain < 0:
                return
            elif remain == 0:
                results.append(path)
                return
            else:
                for i in range(len(candidates)):
                    print(path)
                    if (path != [] and candidates[i] < path[len(path) - 1]):
                        print("empty")
                    else:
                        dfs(remain - candidates[i], path + [candidates[i]], results)
        
        dfs(target, [], results)
        x = set()
        for i in x:
            x.add(set(i))
        print(x)
        return results