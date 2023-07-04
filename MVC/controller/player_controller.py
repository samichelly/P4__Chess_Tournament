class Players_Manager:
    def check_id_unicity(self, players_loaded):
        test_id = []
        try:
            for i in players_loaded["playertable"]:
                test_id.extend(i.keys())
            return test_id
        except TypeError:
            return None
