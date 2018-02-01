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
sudo apt-get install python3-pip -y
```

Flask and requests

```
pip3 install Flask==0.12.2 requests==2.18.4
```

Postman

```
wget https://dl.pstmn.io/download/latest/linux64 -O postman.tar.gz
sudo tar -xzf postman.tar.gz -C /opt
rm postman.tar.gz
sudo ln -s /opt/Postman/Postman /usr/bin/postman
```

### Installing

Download a local copy of blockchain.py.
To create a local node, type the following termainal command from the location
you downloaded blockchain.py to:

```
python3 blockchain.py -p "port_number"
```

For example, creating a local node on port 5010:

```
python3 blockchain.py -p 5010
```

Additional nodes can be created in separate terminals using different port
numbers.

### Authors

* **Scott Gibson** - [GitHub](https://github.com/no-str)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Daniel van Flymen for the initial python code. [GitHub](https://github.com/dvf/blockchain)
* Mark Siebert for the Postman installaion. [BlueMatador](https://blog.bluematador.com/posts/postman-how-to-install-on-ubuntu-1604/?utm_source=hootsuite&utm_medium=twitter&utm_campaign=)
