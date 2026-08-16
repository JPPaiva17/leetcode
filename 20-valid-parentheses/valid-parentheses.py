class Solution:
    def isValid(self, s: str) -> bool:
        mapeamento = {')': '(', '}': '{', ']': '['}
        pilha = []
        
        for caractere in s:
            if caractere in mapeamento:
                topo = pilha.pop() if pilha else '#'
                
                if mapeamento[caractere] != topo:
                    return False
            else:
                pilha.append(caractere)
        
        return not pilha