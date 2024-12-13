class Voting:
    def __init__(self):
        self.a_votes = 0
        self.b_votes = 0
        self.voter_ids = set()

    def vote(self, candidate, voter_id):
        if voter_id in self.voter_ids:
            return False
        else:
            self.voter_ids.add(voter_id)
            if candidate == 1:
                self.a_votes += 1
            elif candidate == 2:
                self.b_votes += 1
            return True

    def get_vote_count(self):
        return self.a_votes, self.b_votes

    def reset_votes(self):
        self.a_votes = 0
        self.b_votes = 0
        self.voter_ids.clear()
