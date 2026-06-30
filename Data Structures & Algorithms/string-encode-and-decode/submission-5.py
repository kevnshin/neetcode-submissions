class Solution:

    def encode(self, strs: List[str]) -> str:
        print("attempting to encode:", strs)

        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        print("encoded:", result)

        return result

    def decode(self, s: str) -> List[str]:
        print("attempting to decode:", s)
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
                print ("found ", currentIntStr, " long string. which is:", s[start:end])
                result.append(s[start:end])
                i = end
                currentIntStr = ""
            else:
                i += 1
        print("decoded:", result)
        return result
    
    def isInt(self, c: str) -> bool:
        try:
            cInt = int(c)
            return True
        except:
            return False
