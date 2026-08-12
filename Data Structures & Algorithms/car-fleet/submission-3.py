class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # [1, 4]
        # [4, 6]
        # [7, 8]
        # [10, 10]


        # [4, 1, 0, 7]
        # [6, 3, 1, 8]
        # [8, 5, 2, 9]
        # [10, 7, 3, 10]
        positionSpeeds = {}
        for i, p in enumerate(position):
            positionSpeeds[p] = speed[i]

        sortedPositions = sorted(position, reverse=True)

        # speed = distance / time
        # distance = (target - position)
        # speed = (target - position)/time
        # time = (target - position) / speed
        # print('sortedPositions', sortedPositions)

        fleets = []
        times = []
        referenceTime = None
        for i, position in enumerate(sortedPositions):
            time = (target - position) / positionSpeeds[position]
            times.append(time)
            # print('i', i)
            # print('times', times)
            # print('fleets', fleets)
            if referenceTime == None:
                referenceTime = time
            # print ('referenceTime', referenceTime)
            # print ('time', time)
            if i - 1 < 0 or referenceTime < time:
                # print('new fleet')
                fleets.append(1)
            else:
                # print('existing fleet')
                fleets[-1] += 1

            referenceTime = max(referenceTime, time)
        return len(fleets)

            # if not fleets:
            #     fleet = set()
            # else:
            #     fleet = fleets[-1]
            
            # previous greater or equal to current
            #     get existing fleet
            #     add to it

            # previous is less than or there is no previous
            #     create new fleet
            #     add to it
            

