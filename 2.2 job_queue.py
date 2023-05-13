class JobPriorityQueue:
    def __init__(self, n):
        self.workers = n
        self.finish_time = []
        self.assigned_jobs = []
        for i in range(self.workers):
            self.finish_time.append([i, 0])

    def siftDown(self, i):
        min_index = i
        left = 2 * i + 1
        if left < self.workers:
            if (self.finish_time[left][1] < self.finish_time[min_index][1] or
                (self.finish_time[left][1] == self.finish_time[min_index][1] and self.finish_time[left][0] < self.finish_time[min_index][0])):
                min_index = left

        right = 2 * i + 2
        if right < self.workers:
            if (self.finish_time[right][1] < self.finish_time[min_index][1] or 
                (self.finish_time[right][1] == self.finish_time[min_index][1] and self.finish_time[right][0] < self.finish_time[min_index][0])):
                min_index = right

        if min_index != i:
            self.finish_time[i], self.finish_time[min_index] = self.finish_time[min_index], self.finish_time[i]
            self.siftDown(min_index)

    def assignJob(self, job):
        will_free = self.finish_time[0]
        self.assigned_jobs.append([will_free[0], will_free[1]])
        self.finish_time[0][1] += job
        self.siftDown(0)


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = [int(x) for x in input().split()]
    assert len(jobs) == n_jobs

    queue = JobPriorityQueue(n_workers)
    for job in jobs:
        queue.assignJob(job)

    for job in queue.assigned_jobs:
        print(job[0], job[1])


if __name__ == "__main__":
    main()
