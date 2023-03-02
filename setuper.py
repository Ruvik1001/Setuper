# Можно добавить:
# 1. Проверка на архив -> распаковка
# 2. Формирование инструкции или подкачка файлов
#3. Вызов мктода подкачки файлов внешними модулями (метод формирования параметров)

from urllib import request
import os
import sys


def _download(params):
    if params['make']:
        os.mkdir(params['dir'])

    if params['name'].find('.') == -1:
        params['name'] += params['url'][params['url'].rfind('.'):]

    print("Try download information from " + params['url'] + "...")
    request.urlretrieve(url=params['url'], filename=(params['dir'] + '\\' + params['name']))


if __name__ == "__main__":
    name_params = ['url', 'dir', 'name', 'make']
    download_params = {
        name_params[0]: '',
        name_params[1]: '',
        name_params[2]: '',
        name_params[3]: False,
    }

    # noinspection PyBroadException
    try:
        if len(sys.argv[1:]) < 2:
            print("Params: ", name_params, sep='')

            key, data = '', ''
            while key != '-1':
                key, data = input('Enter key and data for params or <<-1 -1>> for end: ').split()
                download_params[key] = data

        elif len(sys.argv[1:]) < 2:
            raise Exception('Need 2 or more params')

        temp = []
        for param in sys.argv[1:]:
            temp.append(param)

        for i in range(min(len(temp), len(name_params))):
            download_params[name_params[i]] = temp[i]

        if len(download_params['name']) == 0:
            download_params['name'] = download_params['url'][download_params['url'].rfind('/') + 1:]

        download_params['make'] = bool(download_params['make'])

        print("Get for work:\n", download_params, sep="", end="\n\n")

    except Exception:
        print(name_params, " expected")
        sys.exit(sys.exc_info()[1])

    # noinspection PyBroadException
    try:
        _download(params=download_params)
    except Exception:
        sys.exit(sys.exc_info()[1])

    print("Download success!\n"
          "File save to: " + download_params['dir'] + "\\" + download_params['name'])
