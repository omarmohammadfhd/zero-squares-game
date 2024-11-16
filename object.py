class Cup:
    def __init__(self, color, goal , is_reach , frame_color):
        self.color = color.strip().lower()
        self.goal = goal
        self.is_reach = is_reach
        self.frame_color = frame_color

