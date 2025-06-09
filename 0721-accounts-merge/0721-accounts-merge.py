class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        email_name = {}

        for acc in accounts:
            name = acc[0]
            first = acc[1]
            for email in acc[1:]:
                graph[first].append(email)
                graph[email].append(first)
                email_name[email] = name

        visited = set()
        result = []

        def dfs(email, curr):
            if email in visited:
                return
            visited.add(email)
            curr.append(email)
            for neighbor in graph[email]:
                dfs(neighbor, curr)

        for email in email_name:
            if email not in visited:
                curr = []
                dfs(email, curr)
                result.append([email_name[email]] + sorted(curr))

        return result
