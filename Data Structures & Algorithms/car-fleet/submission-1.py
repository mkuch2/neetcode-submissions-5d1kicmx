class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet_times = []
        pairs = [(p, s) for p, s in zip(position, speed)]

        sorted_pairs = sorted(pairs, reverse=True)

        for (p, s) in sorted_pairs:
            time_remaining = (target - p) / s

            if not fleet_times or fleet_times[-1] < time_remaining:
                fleet_times.append(time_remaining)
        
        return len(fleet_times)
            


                





