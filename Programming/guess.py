#!/usr/bin/env python3

def guess():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('programming.hso-hacker.space', 9001))

    data = s.recv(1024).decode("utf-8")
    print(data)

    result = ""
    num = 0

    digits = list("0123456789abcdef")

    for i in range(47):
        for digit in digits:
            s.send((str(i) + " " + digit).encode())

            response = s.recv(1024).decode("utf-8").strip("\n")

            if response == "right":
                result += digit

                break

    print(result)

if __name__ == "__main__":
    guess()
  
