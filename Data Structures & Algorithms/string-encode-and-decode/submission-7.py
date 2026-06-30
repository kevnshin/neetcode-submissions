class Solution:

    def encode(self, strs: List[str]) -> str:

        result = ""
        for s in strs:
            length = len(s)
            result += f"{length}#{s}"
        return result

    def decode(self, s: str) -> List[str]:
        result:List[str] = []
        i:int = 0
        length:int = len(s)
        currentIntStr:str = ""
        # foundDelimiter:bool = True #start true for first case
        while i < length:
            #delimiter path
            if self.isInt(s[i]):
                currentIntStr += s[i]

            if s[i] == "#":
                start = i + 1
                end = start + int(currentIntStr)
                result.append(s[start:end])
                i = end
                currentIntStr = ""
            else:
                i += 1
        return result
    
    def isInt(self, c: str) -> bool:
        try:
            cInt = int(c)
            return True
        except:
            return False
