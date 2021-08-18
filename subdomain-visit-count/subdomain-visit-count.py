class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dictionary = {}
        results = []
        for i in cpdomains:
            count= i.split(" ")
            # print('count:', count[0])
            result = count[1].split(".")
            # print('result:', result)

            while len(result) > 0:
                subdomain = ".".join(result)
                if subdomain in dictionary:
                    dictionary[subdomain] += int(count[0])
                    result.pop(0)
                else:
                    dictionary[subdomain] = int(count[0])
                    result.pop(0)

        for k,v in dictionary.items():
            results.append(str(v)+ " " + k)
        return results