from my_worker import basic_task

if __name__ == "__main__":
    your_name = "Basic example"
    basic_task.delay(your_name)
