n = 5
arr1 = [0, 0, 0, 0, 0]
arr2 = [30, 1, 21, 17, 28]
answer = []


# def solution(n, arr1, arr2):
#     def convert(num, n):
#         i = 1
#         result = 0
#         while num != 0:
#             num, r = divmod(num, 2)
#             result += i * r
#             i = i * 10
#         result = str(result)
#         result = "0" * (n - len(result)) + result
#         return result

#     c_arr1 = []
#     c_arr2 = []
#     for i in range(len(arr1)):
#         temp = ""
#         c_arr1.append(convert(arr1[i], n))
#         c_arr2.append(convert(arr2[i], n))
#         for j in range(n):
#             if c_arr1[i][j] == "1" or c_arr2[i][j] == "1":
#                 temp += "#"
#             else:
#                 temp += " "
#         answer.append(temp)

#     return answer


# print(solution(n, arr1, arr2))
for i, j in zip(arr1, arr2):
    a12 = str(bin(i | j)[2:])
    a12 = a12.rjust(n, "0")
    a12 = a12.replace("1", "#")
    a12 = a12.replace("0", " ")
    answer.append(a12)

print(answer)
