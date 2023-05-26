#!/usr/bin/env python
# coding: utf-8

# In[1]:


class BankersAlgorithm:
    def __init__(self, available, max_matrix, allocation_matrix):
        self.num_processes = len(max_matrix)
        self.num_resources = len(available)
        self.available = available
        self.max_matrix = max_matrix
        self.allocation_matrix = allocation_matrix
        self.need_matrix = self.calculate_need_matrix()

    def calculate_need_matrix(self):
        need_matrix = []
        for i in range(self.num_processes):
            need = []
            for j in range(self.num_resources):
                need.append(self.max_matrix[i][j] - self.allocation_matrix[i][j])
            need_matrix.append(need)
        return need_matrix

    def is_safe_state(self, request, process_id):
        work = self.available[:]
        finish = [False] * self.num_processes
        need = self.need_matrix[process_id]

        if all(request[i] <= need[i] for i in range(self.num_resources)):
            if all(request[i] <= work[i] for i in range(self.num_resources)):
                for i in range(self.num_resources):
                    work[i] -= request[i]
                    self.allocation_matrix[process_id][i] += request[i]
                    need[i] -= request[i]

                while True:
                    can_finish = False
                    for i in range(self.num_processes):
                        if not finish[i] and all(need[j] <= work[j] for j in range(self.num_resources)):
                            for j in range(self.num_resources):
                                work[j] += self.allocation_matrix[i][j]
                            finish[i] = True
                            can_finish = True
                            break
                    if not can_finish:
                        break

                if all(finish):
                    return True
                else:
                    for i in range(self.num_resources):
                        work[i] += self.allocation_matrix[process_id][i]
                        self.allocation_matrix[process_id][i] -= request[i]
                        need[i] += request[i]
        return False


# Example usage
if __name__ == "__main__":
    available_resources = [3, 3, 2]  # Number of available instances of each resource
    max_matrix = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]  # Maximum resource needs of each process
    allocation_matrix = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]  # Allocated resources for each process

    banker = BankersAlgorithm(available_resources, max_matrix, allocation_matrix)

    # Example request
    request_process_id = 1
    request_resources = [1, 0, 2]
    if banker.is_safe_state(request_resources, request_process_id):
        print("Request is safe. Performing allocation.")
        banker.available = [available_resources[i] - request_resources[i] for i in range(len(available_resources))]
        banker.allocation_matrix[request_process_id] = [allocation_matrix[request_process_id][i] + request_resources[i]
                                                        for i in range(len(available_resources))]
        banker.need_matrix[request_process_id] = [banker.need_matrix[request_process_id][i] - request_resources[i]
                                                  for i in range(len(available_resources))]
    else:
        print("Request is unsafe. Allocation denied.")


# In[ ]:




