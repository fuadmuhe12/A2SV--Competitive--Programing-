from collections import defaultdict

class Solution:
    def findDuplicate(self, paths):
        content_dict = defaultdict(list)

        for path in paths:
            parts = path.split()
            directory = parts[0]
            files = parts[1:]

            for file in files:
                name, content = file.split('(')
                content_dict[content[:-1]].append(directory + '/' + name)

        result = [group for group in content_dict.values() if len(group) > 1]
        return result
