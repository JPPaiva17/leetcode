class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0
        while (read < len(chars)):
            actualLetter = chars[read]
            counter = 0
            while(read < len(chars) and chars[read] == actualLetter):
                counter += 1
                read += 1
            chars[write] = actualLetter
            write += 1
            if counter > 1:
                for digito in str(counter):
                    chars[write] = digito
                    write += 1
        return write

