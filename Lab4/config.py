class Config:
    AVAILABLE_PAGES = 50
    NUM_OF_PROCESSES = 20
    LEN_OF_PROCESSES = 100
    MIN_FRAMES = 6
    MAX_FRAMES = 11

    @staticmethod
    def validate(self):
        if self.MIN_FRAMES < self.LEN_OF_PROCESSES:
            raise ValueError('Minimal number of frames cannot be lesser than length of processes.')
