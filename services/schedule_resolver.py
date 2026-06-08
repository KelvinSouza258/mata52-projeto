import heapq
import time

from models.activity import Activity
from services.sort import MergeSort


def greedy_classic(activities: list[Activity]) -> tuple[list[Activity], float]:
    t0 = time.perf_counter()

    sorted_acts = MergeSort.sort(activities, ":end_time")
    scheduled: list[Activity] = []

    for activity in sorted_acts:
        if not any(activity.overlaps(other) for other in scheduled):
            scheduled.append(activity)

    elapsed_ms = (time.perf_counter() - t0) * 1000
    return scheduled, elapsed_ms


def dp_weighted(activities: list[Activity]) -> tuple[list[Activity], float]:
    t0 = time.perf_counter()

    sorted_acts = MergeSort.sort(activities, ":start_time")

    if not sorted_acts:
        return [], (time.perf_counter() - t0) * 1000

    pq: list[tuple] = []
    max_weight = 0
    best_chain: list[Activity] = []
    seq = 0

    for activity in sorted_acts:
        while pq and pq[0][0] <= activity.start_time:
            _, weight, _, chain = heapq.heappop(pq)
            if weight > max_weight:
                max_weight = weight
                best_chain = chain

        heapq.heappush(
            pq,
            (
                activity.end_time,
                activity.weight + max_weight,
                seq,
                best_chain + [activity],
            ),
        )

        seq += 1

    while pq:
        _, weight, _, chain = heapq.heappop(pq)
        if weight > max_weight:
            max_weight = weight
            best_chain = chain

    elapsed_ms = (time.perf_counter() - t0) * 1000
    return best_chain, elapsed_ms
