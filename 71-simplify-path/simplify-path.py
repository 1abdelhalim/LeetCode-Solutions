class Solution:
    def simplifyPath(self, path: str) -> str:
        n = len(path)
        stack = []
        sett = {".", "", ".."}

        path = path.split("/")

        for ch in path:
            if stack and ch == "..":
                stack.pop()
            elif ch not in sett:
                stack.append(ch)

        return "/" + "/".join(stack)
        