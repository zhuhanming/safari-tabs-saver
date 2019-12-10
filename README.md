# Safari Tabs Saver

Safari Tabs Saver is a Python script written to allow Safari users to create backups of their currently open tabs. Due to the lack of accessible or free Safari tab manager extensions, this script aims to better the lives of tab hoarders.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for your usage.

### Prerequisites

To run this script, you simply need Python and this repository on your local machine. You can get a copy of this repository by running the following command in your command line.

*With SSH*
```
git clone git@github.com:zhuhanming/safari-tabs-saver.git
```

*With HTTPS*
```
git clone https://github.com/zhuhanming/safari-tabs-saver.git
```

### Installing

To install the dependencies required for this script, simply navigate into the directory you just cloned and run the following command in your command line. You may also choose to start a Python virtual environment before running the command.

```
pip install -r requirements.txt
```


## Running the script

Simply run the following command:

```
python safari-tabs-saver.py
```

### Viewing your backups

Your backups are saved into the backups folder. Simply navigate to the backups folder and open the latest exported html file.  

You can open saved tabs one by one by clicking the saved tab title, or open the entire window in one go by click the bolded text at the end of each window's tabs.

## Built With

* [Python](https://www.python.org) - Language used
* [safari-open-pages.py](https://gist.github.com/aleks-mariusz/cc27b21f2c5b91fbd285) - Fetches open tabs in Safari
* [Normalize.css](https://necolas.github.io/normalize.css/) - Normalises view in exported HTML file

## Contributing

1. Fork it (<https://github.com/zhuhanming/safari-tabs-saver/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -m 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## Authors

* **Zhu Hanming** - *Extended [aleks-mariusz](https://www.github.com/aleks-mariusz)'s original code* - [zhuhanming](https://github.com/zhuhanming) (see [Acknowledgements](#acknowledgements) below)

See also the list of [contributors](https://github.com/zhuhanming/safari-tabs-saver/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Original script to fetch open tabs in Safari by [aleks-mariusz](https://www.github.com/aleks-mariusz) can be found [here](https://gist.github.com/aleks-mariusz/cc27b21f2c5b91fbd285)
