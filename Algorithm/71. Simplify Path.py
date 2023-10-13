'''
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, 
convert it to the simplified canonical path.
In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, 
and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. 
For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:
- The path starts with a single slash '/'.
- Any two directories are separated by a single slash '/'.
- The path does not end with a trailing '/'.
- The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.

Example 1:
Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:
Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

Example 3:
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
'''
class Solution:
    def simplifyPath(self, path: str) -> str:
        '''
        這題需要使用stack
        先將給定的字串用'/'split分隔開成一個array

        '''
        stack=[]
        lstPath = path.split('/')

        # path="/home//foo/", lstPath=['home', '', 'foo', '']
        for _path in lstPath:
            # 先將前後的空字串消除，因為有可能遇到path="/home//foo   /"，這樣split後，會拿到"foo    "
            _path = _path.strip()

            # 如果是當前路徑或路經為空就跳過，因為有可能遇到兩個//的情況，//的情況split後就是空字串
            if not _path or _path == '.':
                continue
            
            # 如果是返回前一路徑，就pop最近一次加的路徑
            if _path == "..":
                if stack: stack.pop()
            else:
                stack.append(_path)
        
        # 從最近的路徑慢慢返回到根目錄
        res=""
        for _ in range(len(stack)):
            res = '/' + stack.pop() + res
        
        if not res:
            return '/'
        else:
            return res 

