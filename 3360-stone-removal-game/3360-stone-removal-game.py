class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones = n
        remove = 10
        alice_turn = True

        while stones >= remove:
            stones -= remove
            remove -= 1
            alice_turn = not alice_turn

        return not alice_turn