class Solution:

    def compareVersion(self, version1, version2):
        version1 = list(map(int, version1.split(".")))
        version2 = list(map(int, version2.split(".")))
        max_length = max(len(version1), len(version2))
        version1.extend([0] * (max_length - len(version1)))
        version2.extend([0] * (max_length - len(version2)))

        if version1 > version2:
            return 1
        if version1 < version2:
            return -1
        return 0
