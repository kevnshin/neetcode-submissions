class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        positionSpeeds = {}
        for i, p in enumerate(position):
            positionSpeeds[p] = speed[i]

        sortedPositions = sorted(position, reverse=True)

        fleets = []
        times = []
        referenceTime = None
        for i, position in enumerate(sortedPositions):
            time = (target - position) / positionSpeeds[position]
            times.append(time)

            if referenceTime == None:
                referenceTime = time

            if i - 1 < 0 or referenceTime < time:
                fleets.append(1)
            else:
                fleets[-1] += 1

            referenceTime = max(referenceTime, time)
        return len(fleets)

