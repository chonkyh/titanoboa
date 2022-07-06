class lrudict(dict):
    def __init__(self, n, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.n = n
      
    def __getitem__(self, k):
        val = super().__getitem__(k)
        del self[k]
        super().__setitem__(k, val)
        return val
      
    def __setitem__(self, k, val):
        if len(self) == self.n:
            del self[next(iter(self))]
        super().__setitem__(k, val)
