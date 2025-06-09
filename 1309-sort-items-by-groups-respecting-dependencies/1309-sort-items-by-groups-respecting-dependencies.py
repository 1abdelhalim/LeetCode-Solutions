class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        groupMap = defaultdict(list)

        for i in range(n):
            if group[i]==-1:
                groupMap[str(i)+'*'].append(i)
            else:
                groupMap[group[i]].append(i)

        groupGraph = defaultdict(set)
        itemGraph = defaultdict(list)

        for i in range(n):
            for b in beforeItems[i]:
                itemGraph[i].append(b)
                if group[i]!=group[b]:
                    x = str(i)+'*' if group[i]==-1 else group[i]
                    y = str(b)+'*' if group[b]==-1 else group[b]
                    groupGraph[x].add(y)


        def dfs(node,res,visited,graph):
            if node in visited:
                return visited[node]

            visited[node] = True
            for nei in graph[node]:
                if dfs(nei,res,visited,graph):
                    return True

            visited[node] = False
            res.append(node)
            return False

        groupOrder = []
        visited = {}
        for i in groupMap:
            if dfs(i,groupOrder,visited,groupGraph):
                return []

        res = []
        visited ={}
        for g in groupOrder:
            for item in groupMap[g]:
                if dfs(item,res,visited,itemGraph):
                    return []

        return res

                

        

        