
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visit_count = {}

        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)

            subdomains = domain.split('.')
            for i in range(len(subdomains)):
                subdomain = '.'.join(subdomains[i:])
                if subdomain in visit_count:
                    visit_count[subdomain] += count
                else:
                    visit_count[subdomain] = count

        result = []
        for subdomain, count in visit_count.items():
            result.append(f"{count} {subdomain}")

        return result