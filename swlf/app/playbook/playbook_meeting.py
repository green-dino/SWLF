import pandas as pd

class MeetingScheduler:
    def __init__(self, meeting_days):
        self.meeting_days = meeting_days
        self.votes = {day: {"Yes": 0, "No": 0, "IfNeedBe": 0} for day in meeting_days}
        self.weights = {"Yes": 1, "No": -1, "IfNeedBe": 0}

    def print_votes(self):
        print("Meeting Day\tYes\tNo\tIf Need Be")
        for day in self.meeting_days:
            print(f"{day}\t\t{self.votes[day]['Yes']}\t{self.votes[day]['No']}\t{self.votes[day]['IfNeedBe']}")

    def get_user_vote(self):
        print("Vote for a meeting day:")
        for index, day in enumerate(self.meeting_days, start=1):
            print(f"{index}. {day}")

        choice = input("Enter the number of your choice (1-5): ")
        return self.meeting_days[int(choice) - 1] if choice.isdigit() and 1 <= int(choice) <= len(self.meeting_days) else None

    def vote(self, user_day, user_vote):
        if user_vote in self.weights:
            self.votes[user_day][user_vote] += self.weights[user_vote]
        else:
            print("Invalid vote. Please enter Yes, No, or IfNeedBe.")

    def run_voting(self):
        while True:
            self.print_votes()
            user_day = self.get_user_vote()

            if user_day:
                user_vote = input("Vote (Yes, No, IfNeedBe): ").strip()
                self.vote(user_day, user_vote)

            another_vote = input("Do you want to continue voting (yes/no)? ").strip().lower()
            
            if another_vote != "yes":
                break

        print("Voting results:")
        self.print_votes()
        self.save_voting_data()
        self.analyze_data()

    def save_voting_data(self):
        voting_data = []
        for day in self.meeting_days:
            voting_data.append([day, self.votes[day]['Yes'], self.votes[day]['No'], self.votes[day]['IfNeedBe']])

        df = pd.DataFrame(voting_data, columns=["Meeting Day", "Yes", "No", "If Need Be"])
        df.to_csv("voting_data.csv", index=False)
        print("Voting data has been saved to voting_data.csv")

    def analyze_data(self):
        total_votes = {day: self.votes[day]['Yes'] + self.votes[day]['No'] + self.votes[day]['IfNeedBe'] for day in self.meeting_days}
        most_preferred_day = max(total_votes, key=total_votes.get)
        least_preferred_day = min(total_votes, key=total_votes.get)

        print("Data Analysis:")
        print(f"Most Preferred Day: {most_preferred_day}")
        print(f"Least Preferred Day: {least_preferred_day}")
        print("Total Votes per Day:")
        for day, total in total_votes.items():
            print(f"{day}: {total}")

if __name__ == "__main__":
    meeting_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    scheduler = MeetingScheduler(meeting_days)
    scheduler.run_voting()
