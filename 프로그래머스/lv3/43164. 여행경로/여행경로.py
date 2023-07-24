# dfs 
# 1 - 1. 경로를 저장할 배열 선언하기
# 1 - 2. 방문 여부를 체크할 배열 선언하기

# 출발지 ICN 을 배열에 넣기
# tickets 배열 중에 출발지가 같은 곳 찾기
# 방문한 곳인지 확인
# 방문하지 않은 곳이면 도착지를 배열에 넣고 출발지를 도착지로 변경하기
# 3~5번을 반복하며 경로 배열이 일정 길이가 되면 저장하기
# def solution(tickets):
#     route = []
#     visited = [0] * len(tickets)
#     route.append(tickets[0][0])
#     print(visited, route)


def solution(tickets):

    def dfs(departure: str, path: list):
        if len(path) == n + 1:
            return path

        if airports.get(departure):
            for entrance in airports.get(departure):
                if visited[departure][entrance] == 0:
                    continue

                visited[departure][entrance] -= 1
                new_path = path + [entrance]
                result = dfs(entrance, new_path)
                if result:
                    return result
                visited[departure][entrance] += 1


    n = len(tickets)
    tickets.sort(key = lambda x:x[1])
    answer = []
    airports = dict()
    visited = dict()

    for departure, entrance in tickets:
        if airports.get(departure):
            airports[departure].append(entrance)
        else:
            airports.setdefault(departure, [entrance])

    for departure, entrances in airports.items():
        for entrance in entrances:
            if visited.get(departure):
                if visited[departure].get(entrance):
                    visited[departure][entrance] += 1
                else:
                    visited[departure][entrance] = 1
            else:
                visited.setdefault(departure, {entrance: 1})

    answer = dfs("ICN", ["ICN"])
    return answer
