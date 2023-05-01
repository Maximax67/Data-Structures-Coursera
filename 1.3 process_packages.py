from collections import namedtuple, deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = deque(maxlen=size)

    def process(self, request):
        while len(self.finish_time) > 0:
            if self.finish_time[0] <= request.arrived_at:
                self.finish_time.popleft()
            else:
                break
        n = len(self.finish_time)
        if self.size == n:
            return Response(True, -1)

        start_time = 0
        if n == 0:
            start_time = request.arrived_at
        else:
            start_time = self.finish_time[n - 1]

        self.finish_time.append(start_time + request.time_to_process)
        return Response(False, start_time)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


if __name__ == "__main__":
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)
