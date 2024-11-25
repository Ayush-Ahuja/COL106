'''
    This file contains the class definition for the StrawHat class.
'''

import crewmate
import heap
import treasure

class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        
        self._working_crewmates = []
        L = []
        for i in range(m):
            new_crewmate = crewmate.CrewMate()
            L.append((0, i, new_crewmate))
        self._crew_heap = heap.Heap(init_array=L)

    
    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        extracted_key, extracted_id, extracted_element = self._crew_heap.extract()
        extracted_element.insert_treasure(treasure)
        if extracted_key == 0:
            self._working_crewmates.append(extracted_element)
        if extracted_key > treasure.arrival_time:
            self._crew_heap.insert(((extracted_key + treasure.size), extracted_id, extracted_element))
        else:
            self._crew_heap.insert(((treasure.arrival_time + treasure.size), extracted_id, extracted_element))
        
    
    def get_completion_time(self):
        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their ids after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        total_treasure_list = []
        for crewmate1 in self._working_crewmates:
            crewmate1.update_comp_time()
            for treasure1 in crewmate1.treasure_list:
                total_treasure_list.append(treasure1)

        total_treasure_list.sort(key=lambda x: x.id)
        return total_treasure_list

    
    # You can add more methods if required