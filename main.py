
"""importing modules"""
import sort as st


if __name__ == "__main__":
    st.read_file()
    order = input("choose either ascending or descending:")

    column = input("choose either sequence,size or priority: ")

    st.sort(column, order)
