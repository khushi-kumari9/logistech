class Package:
    """Package entering the warehouse."""

    def __init__(self, tracking_id, size, destination):
        self.tracking_id = tracking_id
        self.size = size
        self.destination = destination

    def __repr__(self):
        return f"<Package {self.tracking_id}, size={self.size}, dest={self.destination}>"
