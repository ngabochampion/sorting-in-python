""" This module is for reading a file and sorting the data containing in that file and then
create new files that will hold the sorted data
 """

FINAL_ITEMS = []


def read_file():
    """this function is just for reading the file"""
    try:
        with open('items.txt', 'r') as data:
            for word in data:
                changed_item = {}
                line = word.replace('\n', '')
                item_list = line.strip().split(' ')
                changed_item["sequence"] = int(item_list[0])
                changed_item["size"] = int(item_list[1])
                changed_item["priority"] = item_list[2]
                FINAL_ITEMS.append(changed_item)
            return

    except FileNotFoundError:
        print('file not found')


def create_file(file_column, file_data):
    """this function is  for creating files which will hold our sorting data"""
    file_name = str(f"order_by_{file_column}.txt")
    with open(file_name, 'w')as output_file:
        final_txt = ""
        for data in file_data:
            sequence = data["sequence"]
            size = data["size"]
            priority = data["priority"]
            next_line = str(f"{sequence} {size} {priority} \n")
            final_txt = str(f"{final_txt}") + next_line
        output_file.write(final_txt)


def sort(file_column, file_data):
    """this function is for sorting our given data """
    if file_data == "ascending":
        sorting = sorted(FINAL_ITEMS, key=lambda i: i[file_column])
        create_file(file_column, sorting)

    file_data = "descending"
    sorting_desc = sorted(FINAL_ITEMS, key=lambda f: f[file_column], reverse=True)
    create_file(file_column, sorting_desc)
