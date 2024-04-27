# Problem: Turtle vs. Rabbit Race: Optimal Trainings - https://codeforces.com/contest/1933/problem/E

t
for _ in range(t):
    num_tracks = int(input())
    track_lengths = [0] + [int(length) for length in input().split()]
    for i in range(1, num_tracks + 1):
        track_lengths[i] += track_lengths[i - 1]

    num_queries = int(input())
    for _ in range(num_queries):
        start, increase = [int(x) for x in input().split()]
        lower_bound = start
        upper_bound = num_tracks
        pick = start
        while lower_bound <= upper_bound:
            mid = (lower_bound + upper_bound) // 2
            if track_lengths[mid] - track_lengths[start - 1] <= increase:
                pick = mid
                lower_bound = mid + 1
            else:
                upper_bound = mid - 1

        if pick < num_tracks and track_lengths[pick + 1] - track_lengths[start - 1] - increase <= increase - (track_lengths[pick] - track_lengths[start - 1]):
            pick += 1

        print(pick, end=" ")
    print("")
