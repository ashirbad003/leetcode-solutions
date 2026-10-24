class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # prefix[i] = number of days before month i+1
        prefix = [0]
        for d in days_in_month:
            prefix.append(prefix[-1] + d)

        def day_of_year(date: str) -> int:
            month, day = int(date[:2]), int(date[3:])
            return prefix[month - 1] + day

        start = max(day_of_year(arriveAlice), day_of_year(arriveBob))
        end = min(day_of_year(leaveAlice), day_of_year(leaveBob))

        return max(0, end - start + 1)