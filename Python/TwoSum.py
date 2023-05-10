def TwoSum(nums: list, target: int) -> list:
    sum_set = {}
    
    for i, num in enumerate(nums):
        if target - num in sum_set:
            return [i, sum_set[target-num]]
        sum_set[num] = i


if __name__ == '__main__':
    lista = [1, 2, 3, 4]
    print(TwoSum(lista, 7))