import sys

import pandas as pd


def main():
    print("sys.argv = " + str(sys.argv))
    file_name = sys.argv[1]
    df = pd.read_csv(file_name)
    df.rename(
        columns={
            "Student ID": "id", "Human Score #1": "score", "Student Text Response": "text"
        },
        inplace=True
    )
    df.to_csv("test3_reformatted.csv", index=False)


if __name__ == "__main__":
    main()
