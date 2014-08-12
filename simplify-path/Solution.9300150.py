class Solution:

    def simplifyPath(self, path):
        folders = list(filter(None, path.split('/')))

        real_path = []
        for f in folders:
            if f == '.':
                continue
            elif f == '..':
                if real_path:
                    real_path.pop()
            else:
                real_path.append(f)

        return '/' + '/'.join(real_path)
