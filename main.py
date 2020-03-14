"""
Searches for distance between 2 friends 
Input is a list of friends and 2 friend names

Methods that must be tested(are these friends in a list)
Algorithms that must be implemented
	1) Basic search(if a friend list has these 2 friends)
	2) Compose a graph and then determine if we can calculate this dintance
		i) We could use Breadth first search or Depth First search
		ii) What if there is no directed graph that has this information --- Add a new node to this graph with the start being first node, then use the last one as distance

"""
class Start:

	def __init__(self):
		pass
	
	def user_exists(self, user_name, user_list):
		for friend in user_list:
			if user_name in friend[0]:
				return True

		return False
	
	def give_trivial_distance(self, friend_list, user_name):
		trivial_distance = 0

		base_friend_list = [list(t) for t in friend_list]
		if (any(user_name in sublist for sublist in base_friend_list)): ### found distance in friend list
			for friend in friend_list:
				if  user_name != friend[0]:
					try:
						trivial_distance = trivial_distance + friend[1]
					except Exception as expt:	
						print(str(expt))
				else:
					trivial_distance = trivial_distance + friend[1]
					break
		else:
			return None

		return trivial_distance

	def find_close_friend(self, friend_lists, user_A, user_B):

		shortest_distance = -1
		relative_distance = 0

		### Phase 1: Trivial distance

		a_b = None
		b_a = None
		for friend_list in friend_lists:
			if user_A == friend_list[0][0]: ### A's friend list
				a_b = self.give_trivial_distance(friend_list, user_B)
			if user_B == friend_list[0][0]: ### B's friend list
				b_a = self.give_trivial_distance(friend_list, user_A)

			if a_b is not None and b_a is not None:
				relative_distance = min(b_a, a_b)
			elif a_b is None:
					relative_distance = b_a
			else:
				relative_distance = a_b	

			if shortest_distance > relative_distance or shortest_distance == -1:
				shortest_distance = relative_distance

		### Phase 2: Generate graph


		return shortest_distance

if __name__ == "__main__":
	starting_point = Start()

	friend_lists = [
			[('A', 0), ('B', 13), ('C', 9),('D', 3)],
			[('B', 0),('C', 9), ('D', 4)],
			[('D', 0),('E', 4)]
		]
	print(starting_point.find_close_friend(friend_lists, 'A', 'B'))

	print(starting_point.user_exists('B',friend_lists))
	print(starting_point.user_exists('E',friend_lists))

