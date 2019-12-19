'''
There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room.
Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.
Initially, all the rooms start locked (except for room 0).
You can walk back and forth between rooms freely.
Return true if and only if you can enter every room.

Example 1:
Input: [[1],[2],[3],[]]
Output: true
Explanation:  
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.

Example 2:
Input: [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can't enter the room with number 2.

Note:
1 <= rooms.length <= 1000
0 <= rooms[i].length <= 1000
The number of keys in all rooms combined is at most 3000.
'''
class Solution:
    
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.rooms = rooms
        n_rooms = len(rooms)
        # 방문한 적 없는 방들의 set
        self.unvisited_rooms = set(range(n_rooms))
        
        # 0번 방에서 시작해서 갈 수 있는 모든 방을 recursive하게 방문하면서, self.unvisited_rooms를 update한다.
        self.visitRooms(0)
        
        if len(self.unvisited_rooms) == 0:
            return True
        else:
            return False
        
        
    
    def visitRooms(self, room_number):
        '''
        room_number부터 시작해서 방문한 적 없는 (=self.unvisited_rooms에 있는) 모든 방들을 recursive하게 방문한다.
        '''
        if room_number in self.unvisited_rooms:
            self.unvisited_rooms.remove(room_number)
            keys = self.rooms[room_number]
            for key in keys:
                self.visitRooms(key)
