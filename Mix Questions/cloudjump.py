'''hacker rank '''


'''A child is playing a cloud hopping game. In this game, there are sequentially numbered clouds that can be thunderheads or cumulus clouds. The character must jump from cloud to cloud until it reaches the start again.

There is an array of clouds,  and an energy level . The character starts from  and uses  unit of energy to make a jump of size  to cloud . If it lands on a thundercloud, , its energy () decreases by  additional units. The game ends when the character lands back on cloud .

Given the values of , , and the configuration of the clouds as an array , determine the final value of  after the game ends.'''


'''The indices of the path are . The energy level reduces by  for each jump to . The character landed on one thunderhead at an additional cost of  energy units. The final energy level is .

Note: Recall that  refers to the modulo operation. In this case, it serves to make the route circular. If the character is at  and jumps , it will arrive at .

Function Description

Complete the jumpingOnClouds function in the editor below.

jumpingOnClouds has the following parameter(s):

int c[n]: the cloud types along the path
int k: the length of one jump
Returns

int: the energy level remaining.
Input Format'''


def jumpingOnClouds(c, k):
    i = k % n     #we are checking where is i from starting position

    e = 100      #since we have only 0 and 1 in array so what ever at c[i] if its 1 automatically 2 will be multiplied and 1 is added
                 # if it is 0 then 2*c[i] will be zero and by default 1 is only added for travesal
    e -= c[i] * 2 + 1  # in first jump
    while i != 0: # we run the loop till it reaches to start position thats y i==0
        i = (i + k) % n # from current postion we are keep incrementing k thats y
                        # it is i+k but we also checking that where it is from start whether crossing or not that position
        e -= c[i] * 2 + 1 #if it reaches start i becomes zero then loop will end but not then keep incrementing
    return e


if __name__ == '__main__':


    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    print(result)
