from matplotlib import cm


DEFAULT_CMAP = 'inferno'


def get_color(x: float, cmap_name: str = DEFAULT_CMAP):
    """Get color from the given color map.
    """
    return cm.get_cmap(cmap_name)(x)
