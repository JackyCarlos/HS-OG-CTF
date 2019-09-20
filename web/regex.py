import re
import requests


def regexEmails(data):
    words = data.split(" ")

    mailAdresses = []

    for i in words:
        if re.findall(r"^[0-9a-f]+@[0-9a-f]+.de$", i):
            mailAdresses.append(i)

    print(mailAdresses)

    concatenateAdresses = ""

    for i in mailAdresses:
        concatenateAdresses += i + "|"

    return concatenateAdresses[:-1]


def main():
    session = requests.session()
    words = session.get('https://web.hso-hacker.space/regex/').text

    emailadresses = regexEmails(words)

    print(emailadresses + '\n\n\n')

    post = session.post('https://web.hso-hacker.space/regex/', data={'emaillist': emailadresses, 'submit': 'Submit'})

    flag = re.findall(r'flag_[0-9a-f]{40}_', post.text)
    print(flag[0])


if __name__ == '__main__':
    main()
