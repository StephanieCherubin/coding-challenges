class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = ['[.]' if i in '.' else i for i in address]
        address = ''.join(address)
        return address
