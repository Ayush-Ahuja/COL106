'''
    Python file to implement the class CrewMate
'''
import heap


class CrewMate:
    '''
    Class to implement a crewmate
    '''
    
    def __init__(self):
        '''
        Arguments:
            None
        Returns:
            None
        Description:
            Initializes the crewmate
        '''
        
        # Write your code here
        self.treasure_list = []
    
    # Add more methods if required
    def insert_treasure(self, treasure):
        self.treasure_list.append(treasure)

    def update_comp_time(self):
        heap1 = heap.Heap()
        for i in range(len(self.treasure_list)):
            curr_treasure = self.treasure_list[i]
            curr_treasure_key = ((curr_treasure.arrival_time + curr_treasure.size), curr_treasure.id)
            heap1.insert((curr_treasure_key, curr_treasure)) 
            if i == (len(self.treasure_list)-1):
                time_taken = 0
                while not heap1.is_empty():
                    extracted_key, extracted_element = heap1.extract()
                    time_taken += (extracted_key[0] - extracted_element.arrival_time)
                    extracted_element.completion_time = curr_treasure.arrival_time + time_taken                   
            else:
                next_treasure = self.treasure_list[(i+1)]
                next_interval = next_treasure.arrival_time - curr_treasure.arrival_time
                left_interval = next_interval
                while not heap1.is_empty() and left_interval:
                    top_key ,top_element = heap1.top()
                    if top_key[0] - top_element.arrival_time > left_interval:
                        heap1.update_top(((top_key[0]-left_interval, top_key[1]), top_element))
                        left_interval = 0
                    else:
                        extracted_key, extracted_element = heap1.extract()
                        left_interval -= (extracted_key[0] - extracted_element.arrival_time)
                        extracted_element.completion_time = curr_treasure.arrival_time + (next_interval - left_interval)

    def is_lazy(self):
        return len(self.treasure_list) == 0