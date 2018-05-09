# Undergraduate Blockchain Research

This repository is for my undergraduate research into blockchain technology.
The aim of this research is to create a multi-transactional blockchain to
emulate the transactional steps between a sugar cane grower and the sugar
milling company.

This research is being conducted under the patient supervision of
[Dr. Steven Gordon](https://handbook.cqu.edu.au/profiles/view/9836) at CQUniversity.

### Prerequisites

Python3

```
sudo apt-get install python3-pip python3-tk -y
```

Flask and requests

```
pip3 install Flask==0.12.2 requests==2.18.4
```

### Installing

Download a local copy of the [no-str/blockchain_research](https://github.com/no-str/blockchain_research) repository.

To create a local node, type the following termainal command from the location
you downloaded the repository to:

```
python3 blockchain.py -i "ip_address" -p "port_number"
```

For example, creating a local node on port 5010:

```
python3 blockchain.py -i 127.0.0.1 -p 5010
```

Additional nodes can be created in separate terminals using different port
numbers.

### Creating a Transaction

A transaction in this instance is the sending of a bin to another user. To create a transaction, type the following termainal command from the location
you downloaded the repository to:

```
python3 trans.py -r "recipient_ip_address" -p "port_number"
```

For example, to send a bin to a local node on port 5010:

```
python3 trans.py -r 127.0.0.1 -p 5010
```
Many transactions can be conducted.

### Mining a Block

Mining creates a block on the blockchain using all the currently unmined transactions. To mine a block, type the following termainal command from the location
you downloaded the repository to:

```
python3 mine.py -i "ip_address" -p "port_number"
```

For example, mining a block on your local node on port 5010:

```
python3 mine.py -i 127.0.0.1 -p 5010
```

### Authors

* **Scott Gibson** - [GitHub](https://github.com/no-str)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Daniel van Flymen for the initial python code. [GitHub](https://github.com/dvf/blockchain)
