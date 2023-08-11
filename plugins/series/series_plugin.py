#! /usr/bin/env python3

import os
import sys


def main():
    episodes = list()
    movie_id = None
    current_episode = 0
    if os.path.exists("progress.txt"):
        with open("progress.txt", "r") as file:
            current_episode = int(file.readline().strip())

    with open("episodes.csv", "r") as file:
        for line in file:
            episodes.append(line)

    while True:
        request = input().split(";")
        if request[0] == "0":
            with open("progress.txt", "w") as file:
                file.write(str(current_episode))
            break

        elif request[0] == "add":
            print(f"movie;{episodes[current_episode].strip()}")
            while True:
                response = input().split(";")
                if response[0] == "movie_id":
                    movie_id = int(response[1])
                    break

        elif request[0] == "quit":
            if all([request[1] == "", int(request[2].strip()) == movie_id]):
                if current_episode < len(episodes) - 1:
                    current_episode += 1
                    print("update")


if __name__ == "__main__":
    os.chdir(sys.path[0])
    main()
