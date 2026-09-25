class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        def parse(i):
            # returns (set_of_words, next_index) parsing one comma-separated group
            groups = []       # list of sets to union
            current = [set()] # list of sets to concatenate (product)
            current[0].add("")

            while i < len(expression) and expression[i] != '}':
                c = expression[i]
                if c == '{':
                    inner, i = parse(i + 1)  # skips past matching '}'
                    current.append(inner)
                elif c == ',':
                    groups.append(current)
                    current = [set()]
                    current[0].add("")
                    i += 1
                else:  # lowercase letter
                    current.append({c})
                    i += 1

            groups.append(current)
            i += 1  # skip the '}' (or reach end of string)

            # union of groups, each group is a cartesian-product concatenation
            result = set()
            for g in groups:
                prod = {""}
                for s in g:
                    prod = {a + b for a in prod for b in s}
                result |= prod
            return result, i

        words, _ = parse(0)
        return sorted(words)