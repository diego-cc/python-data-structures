from typing import List, Union

class BinarySearch:

    """
    Searches for an integer "n" in "l"
    Returns the index of "n" in "l" if found or None otherwise
    "start" and "end" are optional indexes to narrow down the search scope in "l"
    "start" is inclusive, "end" is exclusive
    If they are not specified, the entire list "l" will be scanned
    """
    @staticmethod
    def search(l:List[int], n:int, start:int = 0, end:int = 1)->Union[int, None]:
        if start > 0:
            l = l[start:]

        if end > 1:
            l = l[:end]

        l.sort()

        mid = len(l)//2
        tries = 1
        found = False

        print(f'Haystack: {l}')
        print(f'Needle: {n}\n')

        while l[mid] != n:    
            BinarySearch.print_iteration(l, mid, tries)       

            # break out of the loop if the needle is not found      
            if mid < 1:
                break 
            
            # too high, take the first half of the list
            if l[mid] > n:
                l = l[:len(l)//2]

            # too low, take the second half of the list
            else:
                start = len(l)//2 + 1

                if start >= len(l):
                    start = len(l)//2

                l = l[start:]            

            mid = len(l)//2    
            tries += 1                    

        if l[mid] == n:
            found = True
            BinarySearch.print_iteration(l, mid, tries)
        else:
            mid = None
        
        print(f'Found: {found}')
        return mid

    # Prints the current list, the element in the middle and number of tries up to this point
    @staticmethod
    def print_iteration(l:List[int], mid:int, tries:int)->None:
        print(f'Current haystack: {l}')
        print(f'Try: {l[mid]}')            
        print(f'Number of tries so far: {tries}\n')


if __name__ == "__main__":
    h = [2, 9, 5, 1, 10, 8, 3, 4, -1, 100, 32, -5, 7, 43, 20]
    n = 3

    BinarySearch.search(h, n)