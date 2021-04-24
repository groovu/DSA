from collections import OrderedDict
##from lru import LRU doesn't work in LC
class LRUCache(OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return - 1
        
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False)

# Scratch Work
# class LRUCache:
#     def __init__(self, capacity: int):
#         # what is the def of last used?  If I add 1, then 2.  1 is the LRU even though we haven't gotten any items.  (assumption)
#         #container that holds "key", and LRU score?
#         #not going to use an actual key:value store since I want the keys to be dynamic. (get rid of LRU key, replace)
#         #or I could you a key:value store, and drop the key if it's LRU
#         # yeah that sounds easier.  key: int, val: score.
#         # put
#         # whenever I put a key, I set the score to max (capacity?)
#         # as new keys added and retrieved, I can decay all keys by 1.
#         # key with the lowest value == LRU.
#         # get
#         # if key exists, bump score to max, decay all scores by 1.
#         # if DNE, return -1.
#         # note: lru-dict is a library that already does this.
#         # correction: we're also storing values with keys, so we need to somehow store value and the score.
#         # use a tuple for the value?  key:(value, score)
#         # nope, tuples are not mutable, use a list.  key:[value, score]
#         self.cap = capacity;
#         self.cache = {} #empty dict
        
#     def get(self, key: int) -> int:
#         val = self.cache.get(key);
#         if val == None:
#             return -1
#         else:
#             #iterate through all keys, decrement keys != get key by 1.
#             #set get key value to max.
#             self.decrement();
#             self.cache[key] = [val, self.cap]
#             return val
        

#     def put(self, key: int, value: int) -> None:
#         curCap = len(self.cache.keys())
#         if curCap < self.cap: # cache has space to add item
#             self.decrement()
#             self.cache[key] = [value, self.cap]
#         else: # curCap >= cap; evict.
#             minKey = self.findLRU();
#             self.cache.pop(minKey)
#             self.decrement()
#             self.cache[key] = [value, self.cap]
            
    
#     def decrement(self) -> None:
#         for key in self.cache.keys():
#             self.cache[key][1] -= 1
    
#     def findLRU(self) -> int:
#         #naive method
#         curMin = math.inf
#         curKey = None
#         for key in self.cache.keys():
#             if self.cache[key][1] > curMin:
#                 curMin = self.cache[key][1];
#                 curKey = key;
#         return curKey;

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Weird!  So my implementation works as expected on PythonTutor, but not on Leetcode.
# And the solutions in Leetcode just import a module to make it work.  Sorta cheating imo.

