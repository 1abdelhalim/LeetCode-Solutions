from collections import defaultdict
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_graph = defaultdict(list)
        email_to_name = {}

        # Step 1: Build the graph
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                email_graph[first_email].append(email)
                email_graph[email].append(first_email)
                email_to_name[email] = name

        visited = set()
        result = []

        # Step 2: DFS to collect connected emails
        def dfs(email, collected):
            if email in visited:
                return
            visited.add(email)
            collected.append(email)
            for neighbor in email_graph[email]:
                dfs(neighbor, collected)

        # Step 3: Traverse all emails
        for email in email_to_name:
            if email not in visited:
                collected = []
                dfs(email, collected)
                result.append([email_to_name[email]] + sorted(collected))

        return result
