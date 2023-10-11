class River:
    def __init__(self, depth_map):
        self.depth_map = depth_map

    def calculate_mean_depth(self):
        total_depth = sum(sum(row) for row in self.depth_map)
        square_feet_count = len(self.depth_map) * len(self.depth_map[0])
        mean_depth = total_depth / square_feet_count
        return mean_depth

def main():
    # Create a depth map representing the river. You can replace this with your actual data.
    river_depth_map = [
        [2, 3, 4, 5],
        [3, 4, 5, 6],
        [4, 5, 6, 7],
        [5, 6, 7, 8]
    ]

    river = River(river_depth_map)
    mean_depth = river.calculate_mean_depth()

    print(f"The mean depth of the river is {mean_depth} feet.")

if __name__ == "__main__":
    main()
