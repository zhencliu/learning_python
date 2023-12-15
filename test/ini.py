from configparser import ConfigParser


if __name__ == '__main__':
    parser = ConfigParser()
    try:
        parser.read('file.json')
    except Exception as e:
        print('error')
    else:
        for sec in parser.sections():
            print(dict(parser[sec]))
