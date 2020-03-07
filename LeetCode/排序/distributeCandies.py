def distributeCandies(candies, num_people):
    """
    :type candies: int
    :type num_people: int
    :rtype: List[int]
    """
    list = [0] * num_people
    j = 1
    k = 0
    for i in range(1,num_people*num_people+1):
        if i <= num_people:
            if candies <= i:
                list[i - 1] = candies
                # print("hello")
                break
            list[i - 1] = i
            candies -= i

        if i > num_people:
            if candies <= j*num_people+ (i-j*num_people):
                list[i - j*num_people-1] += candies
                #print("hee")
                break
            list[i-j*num_people-1] += j*num_people+ (i-j*num_people)
            candies -= j*num_people+ (i-j*num_people)
            k += 1
            if k == num_people :
                j += 1
                k = 0
    return list

if __name__ == "__main__":
    print(distributeCandies(60,3))