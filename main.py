nodes =[
    "Warszawa", "Onet", "Newsweek", "Fakt", "Auto Świat", 
    "Forbes", "Business Insider", "Komputer Świat", 
    "Przegląd Sportowy", "Plejada", "NOIZZ"
]
dependencies_data =[
    ("Warszawa", "Onet"), ("Warszawa", "Newsweek"), ("Warszawa", "Fakt"),
    ("Onet", "Forbes"), ("Forbes", "Business Insider"), 
    ("Newsweek", "Business Insider"), ("Auto Świat", "Komputer Świat"),
    ("Fakt", "Plejada"), ("Plejada", "NOIZZ")
]
edges_data =[
    ("Warszawa", "Onet", 4), ("Warszawa", "Newsweek", 6), 
    ("Warszawa", "Fakt", 4), ("Warszawa", "Auto Świat", 5),
    ("Onet", "Forbes", 7), ("Onet", "Przegląd Sportowy", 3),
    ("Newsweek", "Business Insider", 8), ("Newsweek", "Forbes", 5),
    ("Auto Świat", "Komputer Świat", 4),
    ("Komputer Świat", "Przegląd Sportowy", 6), ("Komputer Świat", "Fakt", 3),
    ("Fakt", "Plejada", 5), ("Fakt", "Onet", 6),
    ("Forbes", "Business Insider", 4), ("Forbes", "Auto Świat", 3),
    ("Przegląd Sportowy", "Business Insider", 5), ("Przegląd Sportowy", "Auto Świat", 4),
    ("Plejada", "NOIZZ", 6),
    ("NOIZZ", "Newsweek", 5), ("NOIZZ", "Przegląd Sportowy", 4),
    ("Business Insider", "Komputer Świat", 2)
]


def saved_the_world() -> None:
    N = len(nodes)
    name_to_id = {name: i for i, name in enumerate(nodes)}
    
    INF = float('inf')
    dist = [[INF] * N for _ in range(N)]
    deps = [0] * N

    for u, v in dependencies_data:
        deps[name_to_id[v]] |= (1 << name_to_id[u])

    for u, v, cost in edges_data:
        dist[name_to_id[u]][name_to_id[v]] = cost
    
    dp = [[INF] * N for _ in range(1 << N)]
    parent = [[-1] * N for _ in range(1 << N)]
    
    start_id = name_to_id["Warszawa"]
    dp[1 << start_id][start_id] = 0  
    
    for mask in range(1 << N):
      for u in range(N):
          
          if (mask & (1 << u)) and dp[mask][u] != INF:
              
              for v in range(N):
                    if not (mask & (1 << v)):
                      if dist[u][v] != INF:
                          if (mask & deps[v]) == deps[v]:
                              
                              new_mask = mask | (1 << v)
                              new_cost = dp[mask][u] + dist[u][v]
                              
                              if new_cost < dp[new_mask][v]:
                                  dp[new_mask][v] = new_cost
                                  parent[new_mask][v] = u

    visited = (1 << N) - 1  
    best_cost = INF
    last_node = -1
    
    for i in range(N):
        if dp[visited][i] < best_cost:
            best_cost = dp[visited][i]
            last_node = i

    if best_cost == INF:
        print("IMPOSSIBLE")
    else:
        print(f"Best way costs {best_cost}")


def main():
    saved_the_world()


if __name__ == "__main__":
    main()