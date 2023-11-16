from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
  """
  Returns:
    the set of nodes reachable from start_node
  """
  result = set()
  visited = set()
  frontier = [start_node]

  while frontier:
      current_node = frontier.pop(0)
      if current_node not in visited:
          visited.add(current_node)
          result.add(current_node)
          frontier.extend(graph[current_node] - visited)

  return result
  

def connected(graph):
  """
  Returns:
    True if the graph is connected, False otherwise
  """
  if not graph:
      return False  # Empty graph is not considered connected

  start_node = next(iter(graph))  # Pick the first node randomly, as it doesn't matter which one
  reachable_nodes = reachable(graph, start_node)

  return len(reachable_nodes) == len(graph)




def n_components(graph):
  """
  Returns:
  the number of connected components in the graph
  """
  if not graph:
      return 0  # Empty graph has zero components

  visited = set()
  components = 0

  for node in graph:
      if node not in visited:
          reachable_nodes = reachable(graph, node)
          visited.update(reachable_nodes)
          components += 1

  return components
