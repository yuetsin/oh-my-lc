#!/usr/bin/env python


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        stats = [] * n

        max_t = 0
        for log in logs:
            idd, tag, time = log.split(':')

            int_time = int(time)
            int_id = int(idd)
            if not int_id in stats:
                stats.update({
                    int_id: {}
                })
            stats[int_id][tag] = int_time

            max_t = max(max_t, int_time)

        all_times = [0] * (max_t + 1)

        print(stats)

        for k, v in stats.items():
            for i in range(v['start'], v['end'] + 1):
                all_times[i] = k

        results = [0] * n
        for i in all_times:
            results[i] += 1

        return results
