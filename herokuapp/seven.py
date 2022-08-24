'''
Просматривая локальную сеть одной компании, вы составляете список IP-адресов (разумеется, это IPv7; IPv6 слишком ограничен). Вы хотите выяснить, какие IP-адреса поддерживают TLS (transport-layer snooping).
IP поддерживает TLS, если он имеет Autonomous Bridge Bypass Annotation, или ABBA.  ABBA - это любая четырех символьная последовательность, состоящая из пары двух разных символов, за которыми следует обратная пара, например xyyx или abba.  Однако IP также не должен иметь ABBA внутри любых последовательностей гиперсетей, которые заключены в квадратные скобки.
Например:
- abba[mnop]qrst поддерживает TLS (abba вне квадратных скобок).
- abcd[bddb]xyyx не поддерживает TLS (bddb находится внутри квадратных скобок, хотя xyyx находится вне квадратных скобок).
- aaaa[qwer]tyui не поддерживает TLS (aaaa недопустимо; внутренние символы должны быть другими).
- ioxxoj[asdfgh]zxcvbn поддерживает TLS (oxxo находится вне квадратных скобок, хотя он находится внутри более крупной строки).
Сколько IP-адресов в вашем списке (доступном по кнопке Данные) поддерживают TLS?
'''
import re

def testing():
    assert checking_TLS('abba[mnop]qrst') == True
    assert checking_TLS('abcd[bddb]xyyx') == False
    assert checking_TLS('aaaa[qwer]tyui') == False
    assert checking_TLS('ioxxoj[asdfgh]zxcvbn') == True


def checking_ABBA(ip_list:list) -> bool:
    pattern_ABBA = r'(\w)(?=(\w))\2{2}\1'
    for ip in ip_list:
        if list(filter(lambda x: x[0] != x[1], re.findall(pattern_ABBA, ip))):
            return True


def checking_TLS(ip:str) -> bool:
    pattern = r'\[\w+\]'
    block_lost = re.findall(pattern, ip)
    norm_lost = re.split(pattern, ip)
    if checking_ABBA(block_lost):
        return False
    if checking_ABBA(norm_lost):
        print(ip)
        return True
    return False


def main():
    testing()

    with open(r'C:\my\Python_project\random_tasks\herokuapp\07.txt', 'r') as f:
        ip_list = f.read().split('\n')[:-1]

    print(len([ip for ip in ip_list if checking_TLS(ip)]))


if __name__ == '__main__':
    main()
