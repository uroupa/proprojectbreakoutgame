# def check_win(n_list):
#     for n in n_list:
#         if not n.isvisible():
#             return True
#         else:
#             return False


items = [1, 2, 1]
print(all(n >= 1 for n in items))
