# Sermon

Cross platform serial communication desktop interface

# :construction: TODO
- [x] Port listing
- [x] Comms options
- [ ] Port Opening
- [ ] Port read
- [ ] Port write

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

```bash
git clone https://github.com/eeshiken/Sermon.git
```

### Prerequisites

What things you need to install the software and how to install them

- Python == 3.6.7
- PyQt5 == 5.11.3
- pyserial == 3.4

### Installing

A step by step series of examples that tell you how to get a development env running

> Tested on Ubuntu 18.04

Make sure python3 is installed on your system

```bash
sudo apt install python3 python3-pip
```

Navigate into the cloned repository and install the requirements

```bash
cd Sermon
python3 -m pip install -r requirements.txt
```

Run program to ensure no errors (while in the Sermon directory)

```bash
# Sermon/
python3 -m sermon.main
```

Test system by connecting a serial device (e.g Arduino). Clicking refresh should display the name of the connected device in the drop-down.

## Built With

* [Qt](http://doc.qt.io/) - The base framework used
* [PyQt](https://www.riverbankcomputing.com/software/pyqt/intro) - Development language used
* [PySerial](https://pythonhosted.org/pyserial/index.html) - Used to communicate with serial devices

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/eeshiken/Sermon/tags). 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
