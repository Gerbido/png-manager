from networkx.utils.backends import _dispatch

def cytoscape_data(G, name: str = "name", ident: str = "id"): ...
@_dispatch
def cytoscape_graph(data, name: str = "name", ident: str = "id"): ...
